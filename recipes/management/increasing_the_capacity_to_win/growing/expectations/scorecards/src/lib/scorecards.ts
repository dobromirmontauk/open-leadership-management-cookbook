import sources from '../data/sources.json';
export type Item={id:string;text:string};
export type Section={id:string;title:string;items:Item[]};
export type Card={id:string;title:string;description:string;source?:string;sha?:string;scale:string[];sections:Section[]};
export const defaultScale=['Unlikely in 6+ months','Not yet, maybe in <6 months','Does this well','Very strong','Role model for everyone'];
export function clean(s:string){return s.replace(/\[([^\]]+)\]\([^)]*\)/g,'$1').replace(/<[^>]+>/g,'').replace(/[*_]/g,'').replace(/\\([!_#])/g,'$1').trim()}
export function parseMarkdown(text:string,title='Imported scorecard'):Card{
 let sections:Section[]=[], current:Section|undefined,childIndent=-1;
 for(const line of text.split('\n')){
 const m=line.match(/^(\s*)(?:\d+\.|[-*])\s+(.+)$/); if(!m)continue;
 const indent=m[1].length,body=clean(m[2]); if(!body||body==='TODO')continue;
 if(indent===0){current={id:'s'+sections.length,title:body,items:[]};sections.push(current);childIndent=-1;}
 else if(current){if(childIndent===-1)childIndent=indent;if(indent===childIndent)current.items.push({id:current.id+'i'+current.items.length,text:body});else if(indent>childIndent&&current.items.length)current.items[current.items.length-1].text+=' '+body;}
 }
 sections=sections.filter(s=>s.items.length>0);
 return {id:'custom',title,description:'Your scorecard, the same workshop experience.',scale:defaultScale,sections};
}
const labels:Record<string,[string,string]>={
 'twitter_ad_serving_em.md':['EM · Ad Serving','Grow teams and deliver large, reliable systems.'],
 'twitter_billing_payments_em.md':['EM · Billing & Payments','Build reliable payment platforms and strong teams.'],
 'doxel_fe_em.md':['Sr. Engineering Manager, Product','Execution, product leadership, talent, and technology.'],
 'warrior_tl_scorecard.md':['Warrior Technical Lead','Ship ambitious projects through execution and influence.'],
 'gardener_tl_scorecard.md':['Gardener Technical Lead','Grow healthy systems, teams, and engineering practices.'],
 'uber_tl_scorecard.md':['Über Technical Lead','Lead architecture and engineering across teams.'],
 'qa_lead.md':['QA Lead','Raise product quality while helping engineering move faster.'],
 'director.md':['Engineering Director','Scale execution, clarity, alignment, and organizational health.'],
 'vp_of_eng.md':['VP of Engineering','Wade Chambers’ executive expectations, through the CEO’s eyes.']};
export const templates:Card[]=sources.map(s=>{
 const [title,description]=labels[s.file];const body=s.file==='vp_of_eng.md'?s.content.split('How the CEO judges you:')[1]:s.content;const c=parseMarkdown(body,title);
 return {...c,id:s.file.replace('.md',''),description,source:s.display_url,sha:s.sha};
});
export function validateCard(c:any):Card{
 if(!c||typeof c.title!=='string'||!c.title.trim()||c.title.length>150||!Array.isArray(c.sections)||!c.sections.length||c.sections.length>12)throw Error('Add a title and 1–12 sections.');
 let count=0; const sections=c.sections.map((s:any,j:number)=>{
 if(typeof s.title!=='string'||!s.title.trim()||s.title.length>500||!Array.isArray(s.items)||!s.items.length||s.items.length>20)throw Error('Each section needs a title and 1–20 behaviors.');
 return {id:'s'+j,title:s.title,items:s.items.map((i:any,k:number)=>{count++;const text=typeof i==='string'?i:i?.text;if(typeof text!=='string'||!text.trim()||text.length>5000)throw Error('Every behavior needs text (up to 5,000 characters).');return {id:'s'+j+'i'+k,text};})};});
 if(count>120)throw Error('Use up to 120 behaviors.');
 if(c.scale!==undefined&&(!Array.isArray(c.scale)||c.scale.length!==5||!c.scale.every((v:any)=>typeof v==='string'&&v.length>0&&v.length<300)))throw Error('If provided, scale must contain exactly five nonempty text labels (under 300 characters each).');
 const scale=Array.isArray(c.scale)&&c.scale.length===5&&c.scale.every((v:any)=>typeof v==='string'&&v.length>0&&v.length<300)?c.scale:defaultScale;
 return {id:c.id||'custom',title:c.title.trim(),description:typeof c.description==='string'?c.description.slice(0,500):'',sections,scale,source:typeof c.source==='string'&&c.source.startsWith('https://github.com/')?c.source:undefined};
}
export const flatten=(card:Card)=>card.sections.flatMap((section,sectionIndex)=>section.items.map((item,itemIndex)=>({section,sectionIndex,item,itemIndex})));
export type Rating={rater:string;target:string;item:string;value:number|null;note?:string};
export function report(card:Card,ratings:Rating[],person:string){
 return card.sections.map(section=>{
 const items=section.items.map(item=>{const self=ratings.find(r=>r.rater===person&&r.target===person&&r.item===item.id)?.value??null;const peer=ratings.filter(r=>r.rater!==person&&r.target===person&&r.item===item.id&&typeof r.value==='number');const avg=peer.length?peer.reduce((a,b)=>a+(b.value as number),0)/peer.length:null;return {...item,self,peer:avg,n:peer.length,range:peer.length?[Math.min(...peer.map(r=>r.value!)),Math.max(...peer.map(r=>r.value!))]:null,gap:self!==null&&avg!==null?self-avg:null};});
 const mean=(a:number[])=>a.length?a.reduce((x,y)=>x+y,0)/a.length:null;
 const paired=items.filter(i=>i.gap!==null);
 return {...section,items,self:mean(items.filter(i=>i.self!==null).map(i=>i.self!)),peer:mean(items.filter(i=>i.peer!==null).map(i=>i.peer!)),gap:mean(paired.map(i=>i.gap!)),selfCount:items.filter(i=>i.self!==null).length,peerCount:items.filter(i=>i.peer!==null).length};
 });
}
export function inspectMarkdown(text:string,title:string){
 if(!text.trim())throw Error('Paste or upload a scorecard first.');
 const lines=text.split('\n'),warnings:string[]=[],sections:Section[]=[];
 let current:Section|undefined,childIndent:number|null=null,headingMode=false,omitted=0,nested=false;
 for(const line of lines){
  const heading=line.match(/^##\s+(.+)$/);
  if(heading){headingMode=true;current={id:'s'+sections.length,title:clean(heading[1]),items:[]};sections.push(current);childIndent=null;continue;}
  const m=line.match(/^(\s*)(?:\d+[.)]|[-*])\s+(.+)$/);if(!m){if(line.trim()&&!line.startsWith('#'))omitted++;continue;}
  const indent=m[1].replace(/\t/g,'    ').length,body=clean(m[2]);
  if(!body)continue;
  if(!headingMode&&indent===0){current={id:'s'+sections.length,title:body,items:[]};sections.push(current);childIndent=null;continue;}
  if(!current){omitted++;continue;}
  if(childIndent===null)childIndent=indent;
  if(indent===childIndent){current.items.push({id:current.id+'i'+current.items.length,text:body});}
  else if(indent>childIndent&&current.items.length){current.items[current.items.length-1].text+=' '+body;nested=true;}
  else throw Error('Inconsistent indentation. Use top-level numbered sections and indent each behavior equally, or use ## section headings with bullet lists.');
 }
 if(!sections.length)throw Error('No sections found. Use numbered sections with indented behaviors, or ## section headings with bullet lists.');
 const empty=sections.filter(s=>!s.items.length);if(empty.length)throw Error('These sections have no behaviors: '+empty.map(s=>s.title).join(', ')+'. Indent behavior bullets beneath each section.');
 if(omitted)warnings.push(omitted+' lines of introductory or unstructured text were not included. Check that every intended behavior appears below.');
 if(nested)warnings.push('Deeper nested bullets were combined with their parent behavior. Review the resulting slides.');
 return {card:{id:'custom',title,description:'Your scorecard, the same workshop experience.',scale:defaultScale,sections},warnings};
}
