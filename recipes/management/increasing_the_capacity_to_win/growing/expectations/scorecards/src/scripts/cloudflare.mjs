#!/usr/bin/env node
// Standalone Cloudflare deployment. Credentials stay in Wrangler login or environment variables.
import {readFileSync,writeFileSync,mkdirSync,existsSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import {resolve} from 'node:path';
const action=process.argv[2]||'help';
const run=(args)=>{const r=spawnSync(process.execPath,args,{stdio:'inherit',env:process.env});if(r.error)throw r.error;if(r.status!==0)process.exit(r.status||1)};
const wrangler=resolve('node_modules/wrangler/bin/wrangler.js');
if(!existsSync(wrangler)&&action!=='help')throw Error('Install dependencies first: pnpm install --frozen-lockfile');
const name=process.env.CLOUDFLARE_WORKER_NAME||'good-great-manager';
const dbName=process.env.CLOUDFLARE_DATABASE_NAME||'good-great-manager';
if(!/^[a-z][a-z0-9-]{1,62}$/.test(name)||!/^[a-z][a-z0-9-]{1,62}$/.test(dbName))throw Error('Use 2–63 lowercase letters, numbers, and hyphens for Worker and database names.');
if(action==='login'){run([wrangler,'login']);process.exit(0)}
if(action==='create-db'){run([wrangler,'d1','create',dbName]);console.log('Set CLOUDFLARE_DATABASE_ID to the UUID above, then run pnpm cloudflare:deploy.');process.exit(0)}
if(!['prepare','deploy','dry-run','migrate'].includes(action)){console.log('Commands: login, create-db, prepare, dry-run, migrate, deploy. See DEPLOYMENT.md.');process.exit(action==='help'?0:1)}
const dbId=process.env.CLOUDFLARE_DATABASE_ID;
if(!dbId||!/^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$/i.test(dbId)||dbId==='00000000-0000-4000-8000-000000000000')throw Error('Set CLOUDFLARE_DATABASE_ID to your real D1 database UUID. No resources have been changed.');
if(action!=='migrate')run(['scripts/run-framework.mjs','build']);
const generated=JSON.parse(readFileSync('dist/server/wrangler.json','utf8'));
const config={name,main:'../dist/server/index.js',no_bundle:true,compatibility_date:generated.compatibility_date,compatibility_flags:generated.compatibility_flags,assets:{directory:'../dist/client'},d1_databases:[{binding:'DB',database_name:dbName,database_id:dbId,migrations_dir:'../drizzle'}],rules:[{type:'ESModule',globs:['**/*.js','**/*.mjs']}],workers_dev:true,observability:{enabled:true}};
const domain=process.env.CLOUDFLARE_CUSTOM_DOMAIN;
if(domain){if(!/^(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}$/.test(domain))throw Error('Set CLOUDFLARE_CUSTOM_DOMAIN to a hostname without a protocol or path.');config.routes=[{pattern:domain,custom_domain:true}];}
if(process.env.CLOUDFLARE_ACCOUNT_ID)config.account_id=process.env.CLOUDFLARE_ACCOUNT_ID;
mkdirSync('.cloudflare',{recursive:true});writeFileSync('.cloudflare/wrangler.json',JSON.stringify(config,null,2)+'\n');
console.log('Prepared standalone Cloudflare config. No credentials written.');
if(action==='prepare')process.exit(0);
if(action==='dry-run'){run([wrangler,'deploy','--config','.cloudflare/wrangler.json','--dry-run','--outdir','.cloudflare/dry-run']);process.exit(0)}
run([wrangler,'d1','migrations','apply','DB','--remote','--config','.cloudflare/wrangler.json']);
if(action==='deploy')run([wrangler,'deploy','--config','.cloudflare/wrangler.json']);
