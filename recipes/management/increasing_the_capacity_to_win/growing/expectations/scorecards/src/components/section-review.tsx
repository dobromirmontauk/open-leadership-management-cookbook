'use client';
import type {Card,report} from '../lib/scorecards';
type SectionResult=ReturnType<typeof report>[number];
export type ModeratorResult={person:string;name:string;sections:SectionResult[]};
const fmt=(value:number|null)=>value===null?'—':value.toFixed(1);
function Distribution({counts,label}:{counts:number[];label:string}){
 const total=counts.reduce((a,b)=>a+b,0),max=Math.max(1,...counts);
 return <div className="score-distribution" role="img" aria-label={label+': '+counts.map((count,i)=>(i+1)+' = '+count).join(', ')}>
  {counts.map((count,i)=><div className="distribution-bin" key={i}><span>{count}</span><div className="distribution-track"><i style={{height:count/max*100+'%'}}/></div><strong>{i+1}</strong></div>)}
  {!total&&<span className="distribution-empty">No peer scores yet</span>}
 </div>;
}
export function SectionAverages({result}:{result:SectionResult}){
 return <><div className="section-totals">
  <div><span>Peer Average</span><strong>{fmt(result.peerAverage)}</strong></div>
  <div><span>Your Average</span><strong>{fmt(result.self)}</strong></div>
  <div><span>Peer Highest</span><strong>{fmt(result.peerHighest)}</strong></div>
  <div><span>Peer Lowest</span><strong>{fmt(result.peerLowest)}</strong></div>
 </div><p className="coverage">{result.peerRaters} {result.peerRaters===1?'peer':'peers'} · all scores out of 5{result.peerCount<result.items.length?' · peer feedback covers '+result.peerCount+'/'+result.items.length+' behaviors':''}{result.selfCount<result.items.length?' · self-scores cover '+result.selfCount+'/'+result.items.length+' behaviors':''}</p></>;
}
export default function SectionReview({card,sectionIndex,moderator,personal,people,active,onReturn,onContinue}:{card:Card;sectionIndex:number;moderator:boolean;personal:SectionResult[];people:ModeratorResult[];active:boolean;onReturn?:()=>void;onContinue?:()=>void}){
 const section=card.sections[sectionIndex],result=personal.find(s=>s.id===section.id),last=sectionIndex===card.sections.length-1;
 return <section className="section-review">
  <div className="panel review-heading"><div className="eyebrow">SECTION {sectionIndex+1} OF {card.sections.length} · SCORE REVIEW</div><h2>{section.title}</h2><div className="review-recap"><h3>What we discussed</h3><ol>{section.items.map(item=><li key={item.id}>{item.text}</li>)}</ol></div><p>{moderator?'Compare each person’s peer feedback, then discuss before moving on.':'Your self-scores alongside the feedback you received. Peer names and private notes are not shown.'}</p><p className="coverage">Each peer’s scores are averaged across the section. Peer Average is the mean of those averages; Peer Highest and Peer Lowest are the highest and lowest averages from a single peer. Skips and missing scores are excluded.</p></div>
  {moderator?<>
   {!people.length&&<div className="panel"><h3>No participants yet.</h3><p>Share the join link to bring people into the room.</p></div>}
   <div className="moderator-review-grid">{people.map(person=>{
    const scores=person.sections.find(s=>s.id===section.id);if(!scores)return null;
    return <article className="panel person-section-review" key={person.person}><h3>{person.name}</h3><SectionAverages result={scores}/><h4>Peer score distribution</h4><p className="coverage">All numeric peer ratings across this section’s {section.items.length} behaviors; self-scores excluded.</p><Distribution counts={scores.distribution} label={person.name+' peer score distribution'}/><p className="coverage">{scores.distribution.reduce((a,b)=>a+b,0)} peer ratings</p></article>;
   })}</div>
  </>:result?<>
   <div className="panel"><SectionAverages result={result}/></div>
   {result.items.map((item,i)=><article className="panel behavior-review" key={item.id}><div className="eyebrow">BEHAVIOR {i+1} OF {result.items.length}</div><h3>{item.text}</h3><dl className="behavior-review-stats"><div><dt>Your score</dt><dd>{fmt(item.self)}</dd></div><div><dt>Lowest peer</dt><dd>{fmt(item.lowest)}</dd></div><div><dt>Highest peer</dt><dd>{fmt(item.highest)}</dd></div><div><dt>Average peer</dt><dd>{fmt(item.peer)}</dd></div></dl><h4>Feedback you received</h4><Distribution counts={item.distribution} label={'Behavior '+(i+1)+' peer score distribution'}/><p className="coverage">{item.n} numeric peer {item.n===1?'response':'responses'} · self-score shown separately</p>{item.n===1&&<p className="review-caution">Only one peer rated this behavior. Treat the result as limited evidence.</p>}</article>)}
  </>:<div className="panel"><p>No feedback is available for you in this section yet.</p></div>}
  {active&&<div className="panel review-navigation">{moderator?<><button className="button outline" onClick={onReturn}>Back to last behavior</button><button className="button" onClick={onContinue}>{last?'Finish & release reports':'Continue to next section'}</button></>:<p>Discuss your results. Your moderator will move the room to the next section.</p>}</div>}
 </section>;
}
