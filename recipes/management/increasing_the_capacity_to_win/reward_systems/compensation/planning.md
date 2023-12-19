# Comp Planning 
Compensation planning is one of the most important -- and most boring -- things you do as a Head of Engineering. If you are very lucky, you have a whole, competent department handling this for you. If you are unlucky, you have an incompetent department getting it all wrong (and causing you to lose engineers). Most of us startup folks will be in the middle: nobody does comp planning for us, so we get to be that incompetent department. Yay. The goal of these recipes is to extract you from incompetence as quickly as possible. Because the postmortem meetings don't run themselves.

Why is comp planning so important? Think of the engineering department from the perspective of the CEO. It's probably the biggest line item in her budget - scary. Worse, there are no metrics that can tell her if the department is doing well. No sales $ numbers to hit. No marketing click-through rates or leads generated. No Operations efficiency trends. In fact, when things go badly, you probably go ask for money, and when things are going well, you ask for more money. Do you think she really wants to hear that all those super-expensive engineers are going to cost her EVEN MORE NEXT YEAR?? 

So how do you convince your CEO that raises do make sense? Because if you don't, and you lose a couple of your superstars, she'll blame you for mismanaging them and fire your ass. One easy tip: never propose a raise for yourself, save all that cash for your team. And then, off-cycle, make a big fuss that you are underpaid and have an offer from OpenAI. Sure, it'll burn a huge budget hole in her temp-CFO's spreadsheet, but you can probably end up the hero too by "finding" some $50K you can cut from your AWS spend. All in a day's work.

## Preparation
Many of the recipes around compensation planning depend on the following ingredients. Try to gather them if they are already available. If they are not, it might make sense to start the compensation planning exercise first. When you get stuck on these inputs, point them out to your CEO or HR Partner, so you are aligned on *why they are important*. 

1. [Compensation Benchmarks](benchmarking.md): How much are your 'competitors' going to offer the same engineers you're trying to hire?
1. [Compensation Philosophy](philosophy.md): How your company chooses to reward its people has a huge effect on the approach to the plan.

You should also have a good understanding of [Equity](equity.md) at startups.

## Recipes

### Comp Calculators
There are several good reasons to spend the time to build a comp calculator, and one bad reason to.

Bad reason: because you had one at your previous job so obviously you need one here too. You'll waste a ton of time getting buy-in on the numbers & approach and 3 months later nobody will be using it. I mean, that's what my friend said.

Good reasons: 
1. If you are planning on making a lot of offers and want to align with your CEO on comp ranges so you can approve them without having to go back for permission every time.
2. If your team is going to be making lots of offers and you don't want to have to block them on comp ranges every time.
3. If you are putting together a complex hiring plan and need estimates on how much it's going to cost.
4. If you need to introduce some more fairness into how your team is being comp'd because you have some 'management debt' here. I.e. you did random stuff just to close candidates in the first N years and now you are regretting it.

#### Dobromir's Cash & Equity Calculator Recipe
1. Start with one of the [Compensation Benchmarks](benchmarking.md) recipes. 
1. Build a Comp & Equity Calculator like [this one](https://docs.google.com/spreadsheets/d/1BuM5ar1LTmhLUVN96lVS1vZM3nGbEUKBQhUDyvtuU58/edit#gid=1226519420) that ~I copied from Twitter and my friends at Abnormal~ came up with myself.
    1. ![image](https://github.com/dobromirmontauk/llm-recipes/assets/50121200/87a1bcde-37be-4f26-9328-0ec254482fcc) (see [this Miro version](https://miro.com/app/board/uXjVND-VLJg=/) if you need explanations about what the various parts of the calculator are doing).
1. You'll now need a few inputs from you [Compensation Philosophy](philosophy.md):
    1. The 'low end' of the cash band.
    1. The 'high end' of the cash band.
    1. The equity/cash mix target.
    1. The company valuation used for equity value. 
    1. The equity vesting schedule. 
1. Set up an hour [Controlled Meeting](tools/controlled_meeting.md) with your CEO, HR ally, CFO, and anyone else that can veto this document. 
    1. This is a rare occasion where sharing the document ahead of time will likely cause more problems than it solves. Control the narrative of how the numbers were researched (I'm innocent, it's the HR guy! Or: it's not us, it's the market...). 
1. The CEO/CFO will likely look overwhelmed and say they need some time to review the numbers in more detail. 
    1. Share the spreadsheet with them (and have a backup copy just in case they fiddle with your numbers...).
1. A week or two later (if you are lucky) they'll get back to you and say their CEO friends think these numbers are crazy. 
    1. They've been hiring COBOL Senior Engineers for $120K so you should as well. 
    1. Or they might say it's time to open an office in Antarctica because penguins are cheap. Remind them that Starlink isn't available in Antarctica yet and, anyhow, nobody understands how timezones work at the poles. 
1. You should probably agree to hire the COBOL engineer and then immediately show him a back-of-the-envelope calculation that the product roadmap needs to be paused for 1-2 years to rewrite everything into COBOL. 
1. When your CEO grimaces, solemnly promise that you'll make all initial offers at the bottom of the range. 
1. After the first couple of candidates negotiate their way up to the middle or high-end, you'll have your ranges finalized.
1. Repeat once a year to keep things tasting fresh. 

**Common Pitfalls**

1. Your CEO very likely won't care about your ranges -- until it's the worst possible time to care about them. Usually this is when you are about to close a candidate, or put together the 2024 budget off these numbers. 🤷‍♂️ You may need to find a decision pressure like that in order to get the ranges approved.
2. Your entire company should ideally use a common approach, but they won't. You most often end up with very different equity numbers between departments. Keep an eye out for this -- a good way is to ask for advice from your sales/product/operations counterpart on "how are you doing equity grants?" If you notice something VERY off, bring it up with the CFO/CEO/HR team gently.
3. Ranges & Calculators are just a tool. The REAL decision makers are the "cash in the bank" and "equity in the option pool". Make sure you have enough there before you waste time on calculating how many $M that 10-person Bay Area A-team will cost you. If you aren't sure, go hire the penguins.

#### Pave Tools
You can save yourself a lot of time by spending a lot money and just using [Pave](https://www.pave.com/compensation-planning). It's basically a spreadsheet that costs you $10K a year (I'm guessing that number, I like making spreadsheets myself...)