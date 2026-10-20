import sys,json
from PIL import Image,ImageDraw,ImageFont
# usage: grid.py font out title spec.json   spec: [[caption, image_path], ...] (10 items)
FONT,OUT,TITLE,SPEC=sys.argv[1:5]
items=json.load(open(SPEC))
W,H=1920,1080; img=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(img)
ft=ImageFont.truetype(FONT,118); fc=ImageFont.truetype(FONT,40)
tw=d.textlength(TITLE,font=ft); d.text(((W-tw)/2,60),TITLE,font=ft,fill='black')
cols,tile_w,gap,pad,cap_h=5,310,34,10,58
pic_w=tile_w-2*pad; pic_h=pic_w; tile_h=pad+pic_h+cap_h   # square teaser crops
x0=(W-(cols*tile_w+(cols-1)*gap))//2; ys=[250,250+tile_h+34]
for n,item in enumerate(items):
    cap,path=item[0],item[1]; box=item[2] if len(item)>2 else None  # optional crop box, fractions x0,y0,x1,y1
    r,c=divmod(n,cols); x=x0+c*(tile_w+gap); y=ys[r]
    src=Image.open(path).convert('RGB'); sw,sh=src.size
    if box:   # square crop: x0, y0 as fractions of width/height, side as a fraction of height
        bx0,by0,side=box; cw=ch=min(int(sh*side),sw,sh); left=min(int(sw*bx0),sw-cw); top=min(int(sh*by0),sh-ch)
    else:
        top=int(sh*0.125); ch=cw=sh-top; left=(sw-cw)//2
    pic=src.crop((left,top,left+cw,top+ch)).resize((pic_w,pic_h),Image.LANCZOS)
    img.paste(pic,(x+pad,y+pad))
    d.rounded_rectangle((x,y,x+tile_w,y+tile_h),radius=18,outline='black',width=4)
    cw2=d.textlength(cap,font=fc); d.text((x+(tile_w-cw2)/2,y+pad+pic_h+8),cap,font=fc,fill='black')
img.save(OUT)
