'use client';
import {Printer,Download} from 'lucide-react';
import type {Card,report} from '../lib/scorecards';
import SectionReview from './section-review';
type Sections=ReturnType<typeof report>;
const fmt=(value:number|null)=>value===null?'—':value.toFixed(1);
export default function FinalReport({card,sections,person,session,demo=false,onExport}:{card:Card;sections:Sections;person:string;session:string;demo?:boolean;onExport:()=>void}){
 return <article className="final-report">
  <header className="final-report-header">
   <div className="eyebrow">PERSONAL SCORECARD REPORT{demo?' · FICTIONAL SAMPLE':''}</div>
   <h1>{person}</h1><h2>{card.title}</h2><p>{session}</p>
   <div className="final-report-actions no-print"><button className="button" onClick={()=>window.print()}><Printer size={16}/> Print / Save PDF</button><button className="button outline" onClick={onExport}><Download size={16}/> Export JSON</button><p>Print the complete report or choose “Save as PDF” in your browser’s print dialog.</p></div>
  </header>
  <section className="panel final-report-overview">
   <h2>All sections at a glance</h2>
   <div className="report-table-wrap"><table className="report-summary-table"><thead><tr><th scope="col">Section</th><th scope="col">Peer Average</th><th scope="col">Your Average</th><th scope="col">Peer Highest</th><th scope="col">Peer Lowest</th><th scope="col">Peers</th></tr></thead><tbody>{sections.map((section,i)=><tr key={section.id}><th scope="row">{i+1}. {section.title}</th><td>{fmt(section.peerAverage)}</td><td>{fmt(section.self)}</td><td>{fmt(section.peerHighest)}</td><td>{fmt(section.peerLowest)}</td><td>{section.peerRaters}</td></tr>)}</tbody></table></div>
   <p className="final-report-method">All scores are out of 5. Each peer’s scores are averaged across the section; Peer Average weights those peer averages equally. Peer Highest and Peer Lowest each come from one peer’s section average. Your Average includes only your self-scores. Skips and missing feedback are excluded, never treated as zero. A dash means no numeric feedback.</p>
   <div className="final-report-scale"><h3>Scoring scale</h3><ol>{card.scale.map((label,i)=><li key={i}>{label}</li>)}</ol></div>
   <p className="final-report-privacy">Personal feedback for {person}. Peer identities and private reflection notes are excluded.</p>
  </section>
  {card.sections.map((section,index)=><div className="final-report-section" key={section.id}><SectionReview card={card} sectionIndex={index} moderator={false} personal={sections} people={[]} active={false}/></div>)}
  <div className="final-report-end">End of report · {card.sections.length} sections · {person}</div>
 </article>;
}
