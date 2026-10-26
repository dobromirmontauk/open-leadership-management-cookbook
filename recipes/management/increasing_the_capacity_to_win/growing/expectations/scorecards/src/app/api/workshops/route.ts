import {env} from 'cloudflare:workers';
import {validateCard,flatten,report} from '../../../lib/scorecards';
export const dynamic='force-dynamic';
const json=(x:any,status=200)=>Response.json(x,{status,headers:{'Cache-Control':'no-store'}});
const token=()=>crypto.randomUUID()+crypto.randomUUID();
const hash=async(s:string)=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)))).map(x=>x.toString(16).padStart(2,'0')).join('');
async function db(){if(!env.DB)throw Error('Session database is unavailable. Please try again.');return env.DB;}
export async function GET(req:Request){try{
 const u=new URL(req.url),id=u.searchParams.get('id')?.toUpperCase(),key=req.headers.get('Authorization')?.replace(/^Bearer /,'')||'';
 if(!id||!/^[A-F0-9]{32}$/.test(id))return json({error:'Enter the complete 32-character session ID.'},400);
 const d=await db(),s:any=await d.prepare('SELECT * FROM workshops WHERE id=?').bind(id).first();if(!s)return json({error:'Session not found. Check the code.'},404);
 const people=JSON.parse(s.people),card=JSON.parse(s.card),h=key?await hash(key):'',host=h===s.host_hash,p=people.find((p:any)=>p.hash&&p.hash===h);
 const base:any={id:s.id,title:s.title,card,people:people.map((p:any)=>({id:p.id,name:p.name,claimed:!!p.hash})),slide:s.slide,revealed:!!s.revealed,host,me:p?.id||null};
 if(host){const rows=await d.prepare('SELECT rater,COUNT(*) as count FROM ratings WHERE workshop=? GROUP BY rater').bind(id).all();base.progress=rows.results;}
 if(p){const r:any=await d.prepare('SELECT rater,target,item,value,note FROM ratings WHERE workshop=? AND rater=?').bind(id,p.id).all();base.ratings=r.results;
 if(s.revealed){const all:any=await d.prepare('SELECT rater,target,item,value FROM ratings WHERE workshop=? AND target=?').bind(id,p.id).all();base.report=report(card,all.results,p.id);}}
 return json(base);
 }catch(e:any){return json({error:e.message},500)}}
export async function POST(req:Request){try{
 if(Number(req.headers.get('content-length')||0)>300000)return json({error:'Scorecard is too large.'},413);
 const b:any=await req.json(),d=await db();
 if(b.action==='create'){
 const card=validateCard(b.card),names=(b.names||[]).map((n:any)=>typeof n==='string'?n.trim():'').filter(Boolean);
 if(names.length<2||names.length>40||names.some((n:string)=>n.length>80)||new Set(names.map((n:string)=>n.toLowerCase())).size!==names.length)return json({error:'Add 2–40 participants with distinct names (up to 80 characters each).'},400);
 const id=Array.from(crypto.getRandomValues(new Uint8Array(16))).map(v=>v.toString(16).padStart(2,'0')).join('').toUpperCase();const hostKey=token();const people=names.map((name:string,i:number)=>({id:'p'+i,name,hash:null}));
 await d.prepare('INSERT INTO workshops (id,host_hash,title,card,people,slide,revealed,created) VALUES (?,?,?,?,?,0,0,?)').bind(id,await hash(hostKey),String(b.title||card.title+' workshop').slice(0,150),JSON.stringify(card),JSON.stringify(people),new Date().toISOString()).run();return json({id,hostKey});
 }
 const id=String(b.id||'').toUpperCase();let s:any=await d.prepare('SELECT * FROM workshops WHERE id=?').bind(id).first();if(!s)return json({error:'Session not found.'},404);
 const people=JSON.parse(s.people),card=JSON.parse(s.card),key=req.headers.get('Authorization')?.replace(/^Bearer /,'')||'',h=key?await hash(key):'',host=h===s.host_hash,p=people.find((p:any)=>p.hash===h&&p.hash);
 if(b.action==='join'){
 if(s.revealed)return json({error:'This session has ended.'},409);
 const chosen=people.find((p:any)=>p.id===b.person);if(!chosen||chosen.hash)return json({error:'This seat has already been claimed. Use the original device or ask the facilitator to release it.'},409);
 const participantKey=token();chosen.hash=await hash(participantKey);
 const update=await d.prepare('UPDATE workshops SET people=? WHERE id=? AND people=?').bind(JSON.stringify(people),id,s.people).run();if(!update.meta.changes)return json({error:'Someone just joined. Please try again.'},409);
 return json({key:participantKey,person:chosen.id});
 }
 if(b.action==='control'){
 if(!host)return json({error:'Facilitator link required.'},403);
 if(b.revealed!==undefined)await d.prepare('UPDATE workshops SET revealed=? WHERE id=?').bind(b.revealed?1:0,id).run();
 if(Number.isInteger(b.slide)&&b.slide>=0&&b.slide<flatten(card).length)await d.prepare('UPDATE workshops SET slide=? WHERE id=?').bind(b.slide,id).run();return json({ok:true});
 }
 if(b.action==='release'){
 if(!host)return json({error:'Facilitator link required.'},403);
 const chosen=people.find((p:any)=>p.id===b.person);if(!chosen)return json({error:'Unknown participant.'},400);chosen.hash=null;
 // Keep the original seat's ratings: a rejoining participant resumes the same work.
 const update=await d.prepare('UPDATE workshops SET people=? WHERE id=? AND people=?').bind(JSON.stringify(people),id,s.people).run();if(!update.meta.changes)return json({error:'Roster changed; try again.'},409);return json({ok:true});
 }
 if(b.action==='rate'){
 if(!p)return json({error:'Join the session first.'},403);if(s.revealed)return json({error:'Results are released. Ratings are locked.'},409);
 if(!people.some((q:any)=>q.id===b.target)||!flatten(card).some(x=>x.item.id===b.item)||(b.value!==null&&(!Number.isInteger(b.value)||b.value<1||b.value>5)))return json({error:'Choose a score from 1–5, or not enough evidence.'},400);
 await d.prepare('INSERT INTO ratings (workshop,rater,target,item,value,note) VALUES (?,?,?,?,?,?) ON CONFLICT(workshop,rater,target,item) DO UPDATE SET value=excluded.value,note=excluded.note').bind(id,p.id,b.target,b.item,b.value,String(b.note||'').slice(0,1500)).run();return json({ok:true});
 }
 return json({error:'Unknown action.'},400);
 }catch(e:any){return json({error:e.message},400)}}
