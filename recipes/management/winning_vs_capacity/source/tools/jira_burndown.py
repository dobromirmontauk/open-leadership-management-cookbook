import sys,datetime as dt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
OUT=sys.argv[1]
scope_events={30:13000,40:11000,90:15000,100:12500,178:11500}
cap_events={0:30,55:20,68:35,75:50,115:5,121:50,130:120,150:155}
start=dt.date(2026,1,5); END=180
days=list(range(0,END+1)); rem=[]
t=9000;c=30;done=0
for d in days:
    t=scope_events.get(d,t); c=cap_events.get(d,c)
    rem.append(max(t-done,0)); done+=c
dates=[start+dt.timedelta(d) for d in days]
plt.rcParams.update({'font.family':['Arial','Helvetica','DejaVu Sans'],'font.size':15,'text.color':'#42526E','axes.labelcolor':'#42526E','xtick.color':'#6B778C','ytick.color':'#6B778C'})
fig,ax=plt.subplots(figsize=(16.64,7.0),dpi=100)
fig.subplots_adjust(left=0.07,right=0.99,top=0.97,bottom=0.27)
for d in days:  # non-working days
    if dates[d].weekday()>=5: ax.axvspan(dates[d],dates[d]+dt.timedelta(1),color='#F4F5F7',lw=0)
ax.plot([dates[0],dates[-1]],[9000,0],color='#A5ADBA',lw=1.5,label='Guideline')
ax.step(dates,rem,where='post',color='#DE350B',lw=2,label='Remaining Values')
ax.set_ylabel('Story Points'); ax.set_ylim(0,16000); ax.set_xlim(dates[0],dates[-1])
ax.yaxis.grid(True,color='#DFE1E6',lw=1); ax.set_axisbelow(True)
for s in ('top','right','left'): ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#C1C7D0')
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO,interval=2)); ax.xaxis.set_major_formatter(md.DateFormatter('%d/%b/%y'))
plt.setp(ax.get_xticklabels(),rotation=45,ha='right',fontsize=12)
ax.legend(loc='upper center',bbox_to_anchor=(0.5,-0.3),ncol=2,frameon=False,fontsize=14)
fig.savefig(OUT,facecolor='white')
