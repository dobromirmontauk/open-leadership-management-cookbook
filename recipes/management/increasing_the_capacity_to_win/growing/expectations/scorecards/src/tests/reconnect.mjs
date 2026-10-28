import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';

// Exercise the actual client handlers without a browser or server.
const source=readFileSync('app/page.tsx','utf8');
const storage=new Map();
const state={};
let response={id:'ABC',host:true,card:{},slide:2};
const context={URL,URLSearchParams,room:{id:'ABC'},joinCode:'abc',hostLink:'',
 localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v)},
 history:{pushState(){},replaceState(){}},api:async()=>response};
for(const name of ['Room','Selected','Slide','View','Error','Busy','Demo','Key','HostLink','Tab','Notice'])context['set'+name]=v=>{state[name]=v};
vm.createContext(context);
for(const name of ['loadRoom','join','reconnectHost']){
 const start=source.indexOf(' async function '+name+'(');
 const end=source.indexOf('\n ',start+1);
 const code=source.slice(start,end).replaceAll(':string','').replaceAll(':any','');
 vm.runInContext(code,context);
}
await context.loadRoom('ABC','private-key');
assert.equal(storage.get('ggm-host-ABC'),'private-key');
storage.set('ggm-key-ABC','participant-key');
await context.join();
assert.equal(state.Key,'private-key','rejoining prefers saved facilitator access');
response={id:'ABC',host:false,card:{},slide:0};
await context.loadRoom('ABC','participant-key');
assert.equal(storage.get('ggm-host-ABC'),'private-key','participant access cannot replace facilitator access');
context.hostLink='https://scorecards.montauk.family/?room=OTHER#host=bad';
await context.reconnectHost();
assert.match(state.Error,/different session/);
context.hostLink='bad-key';
await context.reconnectHost();
assert.match(state.Error,/not valid/);
assert.equal(storage.get('ggm-host-ABC'),'private-key');
response={id:'ABC',host:true,card:{},slide:2};
context.hostLink='https://scorecards.montauk.family/?room=abc#host=restored-key';
await context.reconnectHost();
assert.equal(storage.get('ggm-host-ABC'),'restored-key');
assert.equal(state.Key,'restored-key');
assert.equal(state.Tab,'people');
assert.equal(state.HostLink,'');
assert.equal(state.Busy,false);
console.log('PASS: facilitator persistence, credential priority, participant isolation, reconnect validation and restoration');
