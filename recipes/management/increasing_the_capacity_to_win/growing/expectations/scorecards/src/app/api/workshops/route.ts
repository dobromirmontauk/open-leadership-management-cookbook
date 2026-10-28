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
 const base:any={id:s.id,title:s.title,card,people:people.map((p:any)=>({id:p.id,name:p.name,claimed:!!p.hash})),slide:s.slide,reviewSection:s.review_section??-1,reviewedThrough:s.reviewed_through??-1,revealed:!!s.revealed,host,me:p?.id||null};
 if(host){
 const all:any=await d.prepare('SELECT rater,target,item,value FROM ratings WHERE workshop=?').bind(id).all();
 base.moderatorReports=base.reviewedThrough>=0?people.map((person:any)=>({person:person.id,name:person.name,sections:report(card,all.results,person.id).slice(0,base.reviewedThrough+1)})):[];
 const rows=await d.prepare('SELECT rater,COUNT(*) as count FROM ratings WHERE workshop=? GROUP BY rater').bind(id).all();base.progress=rows.results;}
 if(p){const r:any=await d.prepare('SELECT rater,target,item,value,note FROM ratings WHERE workshop=? AND rater=?').bind(id,p.id).all();base.ratings=r.results;
 const all:any=await d.prepare('SELECT rater,target,item,value FROM ratings WHERE workshop=? AND target=?').bind(id,p.id).all();
 const personal=report(card,all.results,p.id);
 base.sectionReports=personal.slice(0,base.reviewedThrough+1);
 if(s.revealed)base.report=personal;}
 return json(base);
 }catch(e:any){return json({error:e.message},500)}}
export async function POST(req:Request){try{
 if(Number(req.headers.get('content-length')||0)>300000)return json({error:'Scorecard is too large.'},413);
 const b:any=await req.json(),d=await db();
 if(b.action==='create'){
 const card=validateCard(b.card),names=(b.names||[]).map((n:any)=>typeof n==='string'?n.trim():'').filter(Boolean);
 if(names.length>40||names.some((n:string)=>n.length>80)||new Set(names.map((n:string)=>n.toLowerCase())).size!==names.length)return json({error:'Use up to 40 distinct participant names (up to 80 characters each), or leave the list empty for people to join themselves.'},400);
 const id=Array.from(crypto.getRandomValues(new Uint8Array(16))).map(v=>v.toString(16).padStart(2,'0')).join('').toUpperCase();const hostKey=token();const people=names.map((name:string,i:number)=>({id:'p'+i,name,hash:null}));
 await d.prepare('INSERT INTO workshops (id,host_hash,title,card,people,slide,revealed,created) VALUES (?,?,?,?,?,0,0,?)').bind(id,await hash(hostKey),String(b.title||card.title+' workshop').slice(0,150),JSON.stringify(card),JSON.stringify(people),new Date().toISOString()).run();return json({id,hostKey});
 }
 const id=String(b.id||'').toUpperCase();let s:any=await d.prepare('SELECT * FROM workshops WHERE id=?').bind(id).first();if(!s)return json({error:'Session not found.'},404);
 const people=JSON.parse(s.people),card=JSON.parse(s.card),key=req.headers.get('Authorization')?.replace(/^Bearer /,'')||'',h=key?await hash(key):'',host=h===s.host_hash,p=people.find((p:any)=>p.hash===h&&p.hash);
 if(b.action==='join'){
 if(s.revealed)return json({error:'This session has ended.'},409);
 let chosen;
 if(b.person){
 chosen=people.find((p:any)=>p.id===b.person);
 if(!chosen||chosen.hash)return json({error:'This seat has already been claimed. Use the original device or ask the facilitator to release it.'},409);
 }else{
 const name=typeof b.name==='string'?b.name.trim():'';
 if(!name||name.length>80)return json({error:'Enter your name (up to 80 characters).'},400);
 chosen=people.find((p:any)=>p.name.toLowerCase()===name.toLowerCase());
 if(chosen?.hash)return json({error:'That name is already in the room. Use your original device, ask the facilitator to release your seat, or add a last name to distinguish yourself.'},409);
 if(!chosen){
 if(people.length>=40)return json({error:'This room is full (40 participants).'},409);
 chosen={id:crypto.randomUUID(),name,hash:null};people.push(chosen);
 }
 }
 const participantKey=token();chosen.hash=await hash(participantKey);
 const update=await d.prepare('UPDATE workshops SET people=? WHERE id=? AND people=? AND revealed=0').bind(JSON.stringify(people),id,s.people).run();if(!update.meta.changes)return json({error:'The room changed. Please try joining again.'},409);
 return json({key:participantKey,person:chosen.id});
 }
 if(b.action==='control'){
 if(!host)return json({error:'Facilitator link required.'},403);
 if(b.reviewSection!==undefined){
 const sectionIndex=b.reviewSection;
 if(!Number.isInteger(sectionIndex)||sectionIndex<0||sectionIndex>=card.sections.length)return json({error:'Choose a valid section to review.'},400);
 const slides=flatten(card),current=slides[s.slide];
 if(current.sectionIndex!==sectionIndex||current.itemIndex!==current.section.items.length-1)return json({error:'Finish this section before opening its review.'},409);
 await d.prepare('UPDATE workshops SET review_section=?,reviewed_through=MAX(reviewed_through,?) WHERE id=?').bind(sectionIndex,sectionIndex,id).run();
 return json({ok:true});
 }
 if(b.revealed!==undefined)await d.prepare('UPDATE workshops SET revealed=? WHERE id=?').bind(b.revealed?1:0,id).run();
 if(b.slide!==undefined){
 if(!Number.isInteger(b.slide)||b.slide<0||b.slide>=flatten(card).length)return json({error:'Choose a valid behavior.'},400);
 await d.prepare('UPDATE workshops SET slide=?,review_section=-1 WHERE id=?').bind(b.slide,id).run();
 }
 return json({ok:true});
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
