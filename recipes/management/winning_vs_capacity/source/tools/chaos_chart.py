import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib import font_manager as fm
import matplotlib.pyplot as plt
FONT=sys.argv[1]; OUT=sys.argv[2]
fm.fontManager.addfont(FONT); FN=fm.FontProperties(fname=FONT).get_name()

DEADLINE=180
# total scope (MoB): day -> new total
scope_events={30:13000,40:11000,90:15000,100:12500,178:11500}
# capacity (MoB/day): day -> new rate
cap_events={0:30,55:20,68:35,75:50,115:5,121:50,130:120,150:155}
days=list(range(0,201)); total=[];rem=[];cap=[]
t=9000;c=30;done=0;finish=None
for d in days:
    t=scope_events.get(d,t); c=cap_events.get(d,c)
    r=max(t-done,0)
    if r==0 and finish is None: finish=d
    total.append(t); rem.append(r); cap.append(c if r>0 else float('nan'))
    done+=c if r>0 else 0
print('finish day',finish)

plt.xkcd(scale=0.6,length=120,randomness=2)
plt.rcParams.update({'font.family':[FN,'DejaVu Sans'],'font.size':26,'path.effects':[]})
fig,ax=plt.subplots(figsize=(19.2,10.8),dpi=100)
fig.subplots_adjust(left=0.08,right=0.91,top=0.86,bottom=0.1)
BLUE='#1f5fbf';GREEN='#1e8a3c';RED='#d62828'
ax.plot(days,total,color=BLUE,lw=3,drawstyle='steps-post')
ax.plot(days,rem,color='black',lw=5)
ax.set_xlim(0,205);ax.set_ylim(0,16500)
ax.set_xlabel('DAYS',fontsize=32);ax.set_ylabel('MoBs',fontsize=32)
ax.set_yticks([0,4000,8000,12000,16000]);ax.set_yticklabels(['0','4,000','8,000','12,000','16,000'])
ax.set_xticks([0,30,60,90,120,150,180])
ax.spines['top'].set_visible(False)
ax2=ax.twinx()
ax2.plot(days,cap,color=GREEN,lw=3.5,drawstyle='steps-post')
ax2.set_ylim(0,400);ax2.set_yticks([0,50,100,150,200])
ax2.set_ylabel('MoB / DAY',color=GREEN,fontsize=32)
ax2.yaxis.set_label_coords(1.06,0.25)
ax2.tick_params(axis='y',colors=GREEN);ax2.spines['right'].set_color(GREEN);ax2.spines['top'].set_visible(False)
ax.axvline(DEADLINE,color=RED,lw=4)
ax.text(DEADLINE,16700,'DEADLINE',color=RED,ha='center',fontsize=30)
fig.text(0.08,0.92,'REALITY',fontsize=64)
# line labels
ax.text(184,9700,'TOTAL\nSCOPE',color=BLUE,fontsize=26,va='bottom')
ax.text(48,9900,'REMAINING',color='black',fontsize=28)
ax2.text(4,40,'CAPACITY',color=GREEN,fontsize=26)
def note(axx,n,x,y,tx,ty,l1,l2):
    axx.annotate('(%d) %s\n      → %s'%(n,l1,l2),xy=(x,y),xytext=(tx,ty),fontsize=23,va='center',
                 arrowprops=dict(arrowstyle='-',color='#555555',lw=1.5,shrinkA=4,shrinkB=2))
note(ax,1,30,13000,4,15300,'SCOPE BALLOONS +4,000','TRIM: -2,000')
note(ax,4,90,15000,93,15600,'NEW FLAG: CUSTOMER C +4,000','DECIDE: B FIRST, -2,500')
note(ax2,2,55,20,14,160,'TECH LEAD QUITS: 30 → 20/DAY','DELEGATE: 35/DAY')
note(ax2,3,75,50,58,105,'BIG HIRE LANDS: 50/DAY','GROW')
note(ax2,5,118,5,82,160,'P0 OUTAGE: 6 DAYS AT 5/DAY','RALLY')
note(ax2,6,130,120,103,285,'PLATFORM API: 120/DAY','ALLY')
note(ax2,7,150,155,131,245,'CI 40 → 8 MIN: 155/DAY','AUTOMATE')
ax.annotate('(8) LAST DAY: FURIOUS\n      PM NEGOTIATION\n      → SCOPE -1,000',xy=(178,12000),xytext=(144,13650),fontsize=23,va='center',arrowprops=dict(arrowstyle='-',color='#555555',lw=1.5,shrinkA=4,shrinkB=2))
fig.savefig(OUT,facecolor='white')
