import re,sys
src,out,logo=sys.argv[1],sys.argv[2],sys.argv[3]   # logo: path, or '' to drop it
m={'c49163456796de760f32f9c039efbb18':'fun-burst.png','e85a5180f192551d548983324b524c1d':'fun-bubble.png','6d7b637a91025bd6ae2fd93d33864ef2':logo}
s=re.sub(r'<aside>.*?</aside>','',open(src).read(),flags=re.S)
if not logo: s=re.sub(r'<img src="/_blob/6d7b637a91025bd6ae2fd93d33864ef2"[^>]*>\n?','',s)
s=re.sub(r'/_blob/([0-9a-f]{32})',lambda x:m[x.group(1)],s)
s=s.replace('data-transition="fade" style="','data-transition="fade" style="position:relative;width:1920px;height:1080px;overflow:hidden;',1)
open(out,'w').write('<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0}p{margin:0}</style></head><body>'+s+'</body></html>')
