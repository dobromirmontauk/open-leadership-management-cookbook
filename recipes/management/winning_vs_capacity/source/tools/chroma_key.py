import sys
import numpy as np
from PIL import Image
src,out,box=sys.argv[1],sys.argv[2],[int(v) for v in sys.argv[3].split(',')]
a=np.asarray(Image.open(src).convert('RGB').crop(box)).astype(float)
r,g,b=a[...,0],a[...,1],a[...,2]
spill=np.clip(g-np.maximum(r,b),0,255)          # how green a pixel is
alpha=np.clip(1-spill/180.0,0,1)                 # pure green -> 0
g2=np.minimum(g,np.maximum(r,b))                 # despill
rgb=np.stack([r,g2,b],-1)
img=np.dstack([rgb,alpha*255]).astype(np.uint8)
Image.fromarray(img,'RGBA').save(out)
