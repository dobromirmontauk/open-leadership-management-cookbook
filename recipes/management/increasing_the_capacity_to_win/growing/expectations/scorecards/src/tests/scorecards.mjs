import ts from 'typescript';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const src=fs.readFileSync('lib/scorecards.ts','utf8').replace("import sources from '../data/sources.json';",'const sources='+fs.readFileSync('data/sources.json','utf8')+';');
const compiled=ts.transpileModule(src,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {templates,report,parseMarkdown,validateCard,inspectMarkdown}=await import('data:text/javascript;base64,'+Buffer.from(compiled).toString('base64'));
assert.equal(templates.length,10);
assert.deepEqual(templates.map(c=>c.sections.length),[4,6,6,6,5,6,6,4,4,6]);
assert.deepEqual(templates.map(c=>c.sections.reduce((n,s)=>n+s.items.length,0)),[20,30,30,30,23,27,23,23,23,30]);
assert.ok(templates.every(c=>c.sections.every(s=>s.items.every(i=>i.text!=='TODO'))));
const c=validateCard(parseMarkdown('1. Execution\n    1. Ships.\n    2. Plans.','Test'));
const ratings=[{rater:'a',target:'a',item:'s0i0',value:4},{rater:'a',target:'a',item:'s0i1',value:2},{rater:'b',target:'a',item:'s0i0',value:2},{rater:'c',target:'a',item:'s0i0',value:4},{rater:'b',target:'a',item:'s0i1',value:1},{rater:'c',target:'a',item:'s0i1',value:null}];
let [r]=report(c,ratings,'a');assert.equal(r.self,3);assert.equal(r.peer,2);assert.equal(r.gap,1);assert.equal(r.items[1].n,1);
[r]=report(c,ratings.filter(x=>x.item==='s0i0'||x.rater==='a'),'a');assert.equal(r.peer,3);assert.equal(r.gap,1);assert.equal(r.peerCount,1);
[r]=report(c,[],'a');assert.equal(r.self,null);assert.equal(r.peer,null);assert.equal(r.gap,null);
assert.throws(()=>validateCard({title:'Bad',sections:[]}));
console.log('Scorecard ingestion, all 10 template structures, equal behavior weighting, matched gaps, skips, empty data, and validation passed.');
console.log(templates.map(c=>[c.title,c.sections.map(s=>s.items.length)]));

assert.throws(()=>inspectMarkdown('1. Execution','Test'),/no behaviors/);
assert.throws(()=>inspectMarkdown('Just some words','Test'),/No sections/);
const parsed=inspectMarkdown('Intro ignored.\n## Execution\n- Plans.\n- Ships.','Test');assert.equal(parsed.card.sections[0].items.length,2);assert.equal(parsed.warnings.length,1);
console.log('Markdown headings, nested numbering, omissions warning, and empty-section rejection passed.');

const generic=templates.find(c=>c.id==='generic_manager');
assert.deepEqual(generic.sections.map(s=>s.items.length),[5,5,5,5,5,5]);
assert.match(generic.sections[5].title,/Delegate/);
assert.match(generic.sections[5].items[0].text,/Delegates missions/);

// Section review statistics exclude self-scores and skips from peer distributions.
const [review]=report(c,ratings,'a');
assert.deepEqual(review.items[0].distribution,[0,1,0,1,0]);
assert.equal(review.items[0].lowest,2);
assert.equal(review.items[0].highest,4);
assert.deepEqual(review.distribution,[1,1,0,1,0]);
assert.equal(review.peerAverage,2.75);
assert.equal(review.peerHighest,4);
assert.equal(review.peerLowest,1.5);
assert.equal(review.peerRaters,2);
assert.equal(review.self,3);
assert.equal(review.peerCount,2);
assert.equal(report(c,[],'a')[0].peerAverage,null);
const partial=report(c,ratings.filter(x=>x.item==='s0i0'),'a')[0];
assert.equal(partial.peerAverage,3);
assert.equal(partial.peerHighest,4);
assert.equal(partial.peerLowest,2);
assert.equal(partial.peerCount,1);
console.log('Section distributions, per-peer section averages, coverage, and missing feedback passed.');
