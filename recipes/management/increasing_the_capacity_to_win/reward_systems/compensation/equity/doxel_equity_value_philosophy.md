<!-----



Conversion time: 0.471 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β35
* Thu Dec 07 2023 16:42:34 GMT-0800 (PST)
* Source doc: A Principled Explanation of Equity Grants
----->


How startups grant equity might feel like dark magic. In reality, great startups have a principled approach that balances _how much the employee should earn_ vs _how much will the company grow_. This post explains some of the thinking that usually goes into equity grants (consciously or unconsciously) and should help prospective startup employees ask the right questions to make sure their grants make sense.

These are the factors that should determine the size of the grant. Note that _none of these factors can be known with 100% confidence when equity is being granted; _it is often just a guess by both sides. Negotiations can be more productive if each of these factors is discussed and agreed upon rather than just arguing about raw equity numbers, which always feel too low to employees and too high to employers!



1. What is the _market value_ of the employee? 
    1. This is the maximum dollar value of equity that the employee could get if they interviewed and received offers from multiple companies. Most large companies AFAIK (Google, Twitter) actually have these written down for each level/each employee and grant equity towards this target comp, so getting ranges isn’t too hard. 
    2. Example yearly equity targets from a large (>$10B market cap) public company in 2019:
        1. L1: $10K-$20K
        2. L2: $25K-$70K
        3. L3: $70K-$120K
        4. L4 (Sr. SWE): $79K-$150K
        5. L5 (Staff SWE): $150K-$300K
2. What is the _current valuation_ of the company?
    3. This is easy to get, just ask the startup for their last post-money valuation. If they don’t want to share it, skip that startup - they are playing games with you.
    4. Valuations are tricky; they may greatly depend on the _heat of the market_ at the time. E.g. at the time of this post a ~40x multiplier is normal in public markets for SaaS companies; historically 20-25x was closer to normal, which means valuations may be 2x overinflated for companies raising right now. This mainly matters if you join at the “top of the market” and you think multipliers might drop in the next 4 years.
3. What is the _expected growth in the next 4 years_? Rough is fine: 2x, 4x, 6x, 8x…
    5. Early stage companies (Seed, Series A) should have much higher growth rates - growing from $1M to $2M is a lot easier than $50M to $100M! The risk factor for smaller companies is also a lot higher however: they haven’t yet developed the “revenue factory”.
    6. Companies should have a good story behind their growth, ideally a top-down model that includes what customers they are going after, what product they need to build, who they need to hire… The more mature the company, the better this plan will be. Seed companies may just have a good Founder story. Series A companies should have some target customers and a good idea of how to get them. Series B companies should have a Salesforce backlog and yearly Sales targets.
    7. You can see data for good/better/best here: [https://www.bvp.com/atlas/state-of-the-cloud-2019/](https://www.bvp.com/atlas/state-of-the-cloud-2019/)  or here: [https://techcrunch.com/2015/02/01/the-saas-travel-adventure/](https://techcrunch.com/2015/02/01/the-saas-travel-adventure/)  \
“Great” valuation performance might be something like, following the T2D3 rule:
        6. Year 1: $0M → $12M (infinite x in 1 year)
        7. Year 2: $12M → $50M (3x in 1 year)
        8. Year 3: $50M → $150M (3x in 1 year)
        9. Year 4: $150M → $300M  (2x in1  year)
        10. Year 5: $300M → $600M (2x in 1 year)
        11. Year 6: $600M → $1.2B (2x in 1 year)
4. What is the _risk of missing growth targets_? 
    8. If there was no risk - then all the math would be easy :) This is the hardest part and requires deeper conversations with the business to see if they understand their risks and have plans to mitigate them.
    9. At the end of the day, risk is risk - you can’t predict the future. Some startups are lower-risk because they are selling a “better mousetrap” and have ready customers; some are lower-risk because the founders have created companies before. Or both those factors could actually be increased risk: lots of competition in the marketplace, over-confident founders…

Now we can figure out the appropriate amount of equity _ignoring risk_. Let’s define these terms:



1. Market value (MV): total $ employee would make on market.
2. On-target earnings (OTE): total non-equity $ employee would make on market.
3. Target Yearly Equity (TE)  = MV - OTE 
4. Growth Rate (GR): 4 year expected growth of the company
5. Valuation (V): current company valuation
6. Valuation Increase (VI): V * GR - V (i.e. how much *more* valuable the company will be in 4 years)

The equity grant (EG) should be: **TE * 4 / VI**

Scenarios for a Senior Engineer with a TE of $100K. 

Seed-stage startup growing with T2D3:



* V = $12M
* GR = 36x
* VI = $420M
* EG  = $100K * 4 / $420M = ~0.1%

Seed-stage startup growing more “normally”: 



* V = $12M
* GR = 16x (doubling every year)
* VI = $180M
* EG = .22%

Seed stage startup growing “slowly”



* V = $12M
* GR = 5x (50% growth YoY)
* VI = $60M
* EG = .66%

Series B company growing with T2D3:



* V = $300M
* GR = 12 (2x, 2x, 1.8x, 1.7x)
* VI = $3.6B
* EG = 0.011% (about 10x less than our Seed company!)

Series B company growing more “normally”:



* V = $300M
* GR = 9 (1.8x, 1.8x, 1.7x, 1.7x)
* VI = $2.7B
* EG = 0.015%

Series B company growing “slowly”:



* V = $300M
* GR = 5 (50% YoY growth)
* VI = $1.5B
* EG = 0.027%

**I thought I’d get rich by joining a Unicorn??**

So… it depends on (a) your value on the market, (b) the stage of the company, and (c) what you consider “rich”. Remember that there is a wide talent pool out there so companies are aiming to get “close” to your market value and not overpay for talent - they wouldn’t be great companies if they couldn’t figure out how to control their largest costs - people!! If you join a very early stage company (pre-seed or just post-seed) and can get a sizable 0.3-0.5% grant, then you’re likely to end up with ~$1M-$3M (post-dilution) when the company hits $1B. Note that could be >6 years after you join so you better have planned to exercise those options if you leave, or be stuck at the company until they are liquid!

If you join a later-stage company (>$100M in valuation) most of the _risk is behind the company_ and _growth is still ahead of the company_ - while **your** **value** on the market is the same! Since the startup is now likely to generate many $100Ms in value over the next few years your slice of the pie - to get to your _market value_ - shrinks rapidly. Hitting “unicorn status” of $1B will no longer make you rich, and it shouldn’t since that is a “pretty normal outcome” for the startup! Instead, you should be thinking “what is much better than normal growth?” and make sure your equity package looks good if the startup hits _those_ numbers - then maybe the $1M-$3M is back in play.

Most of the stories out of Silicon Valley come when startups do _way better_ than $1B - e.g. Snowflake or Airbnb at $100B, very recently. In those cases, people would have done “OK” at $1B-$10B values, and instead they got 10x better. Our $100K/year Sr. Engineer is suddenly making $1M-$2M/year at Snowflake.

**How do you factor in risk**?

The equity numbers above assume **zero risk** in the company hitting those growth targets. I don’t know of any hard & fast rule on how to factor in risk. You could build a “probability distribution” model, or you could negotiate the “growth factor” multiplier (e.g. company says “we are going for 8x growth”, and you can ask for a “6x multiplier since 8x is risky because…”). Risk tends to decrease as the company gets bigger, and you have other benefits on top that might make up for it…

**Sweat Equity Venture Capital**

The one other benefit not discussed above is the _upside you have after you stop working there_. The model assumes that you can sell your shares after 4 years, and that is all your equity is worth. However, if you have the good fortune of being able to exercise and hold your options, then suddenly you can grab all the growth _for the next N years_, even if you leave. This is a rare opportunity since otherwise only VCs can benefit from these early, pre-IPO years of startup growth. So if you are patient, and you believe in the company, instead of settling for 4x or 8x increases you can look at 16x or 32x. The risk, of course, increases. Choose your own adventure. 
