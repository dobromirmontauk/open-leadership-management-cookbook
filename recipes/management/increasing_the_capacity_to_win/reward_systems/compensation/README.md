# Comp Planning 
Compensation planning is one of the most important -- and most boring -- things you do as an engineering manager. If you are very lucky, you have a whole, competent department handling this for you. If you are unlucky, you have an incompetent department getting it all wrong (and causing you to lose engineers). Most of us startup folks will be in the middle: nobody does comp planning for us, so we get to be that incompetent department. Yay. The goal of these recipes is to extract you from incompetence as quickly as possible. Because the postmortem meetings don't run themselves.

Why is comp planning so important? Think of the engineering department from the perspective of the CEO. It's probably the biggest line item in her budget - scary. Worse, there are no metrics that can tell her if the department is doing well. No sales $ numbers to hit. No marketing click-through rates or leads generated. No Operations efficiency trends. In fact, when things go badly, you probably go ask for money, and when things are going well, you ask for more money. Do you think she really wants to hear that all those super-expensive engineers are going to cost her EVEN MORE NEXT YEAR?? 

So how do you convince your CEO that raises do make sense? Because if you don't, and you lose a couple of your superstars, she'll blame you for mismanaging them and fire your ass. One easy tip: never propose a raise for yourself, save all that cash for your team. And then, off-cycle, make a big fuss that you are underpaid and have an offer from OpenAI. Sure, it'll burn a huge budget hole in her temp-CFO's spreadsheet, but you can probably end up the hero too by "finding" some $50K you can cut from your AWS spend. All in a day's work.

## Preparation
Before you start comp planning you should prepare a few key ingredients:

1. [Compensation philosophy TODO](TODO): How your company chooses to reward its people has a huge effect on the approach to the plan. There might be a small gap between your philosphy and your CEO's, so it's worth investigating this. You probably want to pay top 90% of the market in cash & equity while she was thinking some occasional launch swag and a monthly motivating All Hands speech might be enough. I'm sure you can resolve this in a 15 minute unprepared 1:1.
2. Human Resource [allies TODO](TODO): You are biased so no matter what numbers you come up with your CEO will cut them in half. Having a non-partisan ally painstakingly spend 100 hours building an unimpeachable market report should convince her to only cut it by 1/3. It's also nice to have someone to blame when the numbers are still WAY too high and your CEO is really mad that engineers are paid too much.
3. [Salary comparisons TODO](TODO): ideally, you've already gotten access to some salary data so you are not flying blind. Try to avoid the "this is how much Google paid me so that's what the market must be" argument. Everybody knows Google is cheap, OpenAI salaries are closer to our real value as engineers!

## Recipes

## Comp Calculators
There are several good reasons to spend the time to build a comp calculator, and one bad reason to.

Bad reason: because you had one at your previous job so obviously you need one here too. You'll waste a ton of time getting buy-in on the numbers & approach and 3 months later nobody will be using it. I mean, that's what my friend said.

Good reasons: 
1. If you are planning on making a lot of offers and want to align with your CEO on comp ranges so you can approve them without having to go back for permission every time.
2. If your team is going to be making lots of offers and you don't want to have to block them on comp ranges every time.
3. If you are putting together a complex hiring plan and need estimates on how much it's going to cost.
4. If you need to introduce some more fairness into how your team is being comp'd because you have some 'management debt' here. I.e. you did random stuff just to close candidates in the first N years and now you are regretting it.

### Dobromir's Cash & Equity Calculator
Start by putting together a draft spreadsheet of market comp bands that your HR ally can fill out. Something like [this](https://docs.google.com/spreadsheets/d/1BuM5ar1LTmhLUVN96lVS1vZM3nGbEUKBQhUDyvtuU58/edit#gid=1332198471):
![image](https://github.com/dobromirmontauk/llm-recipes/assets/50121200/19049448-7bd7-4c98-9de3-25230a142b26)
This is mostly to help them work within the template you defined so you don't have to re-do all their work later and pretend they saved you time.

Next, give them the spreadsheet, and ask them to use 1-2 more sources from the salary comps recipes. This can take anywhere from a week to a month; it's that rare occassion when they can go golfing with their HR friends and call it 'work', so give them some space. 

Build a Comp & Equity Calculator like [this one](https://docs.google.com/spreadsheets/d/1BuM5ar1LTmhLUVN96lVS1vZM3nGbEUKBQhUDyvtuU58/edit#gid=1226519420) that ~I copied from Twitter and my friends at Abnormal~ came up with myself. (see [this Miro version](https://miro.com/app/board/uXjVND-VLJg=/) if you need explanationas about what the various parts of the calculator are doing). 
![image](https://github.com/dobromirmontauk/llm-recipes/assets/50121200/87a1bcde-37be-4f26-9328-0ec254482fcc)

Set up an hour [controlled meeting](controlled_meeting) with your CEO, HR ally, CFO, and anyone else that can veto this document. This is a rare occasion where sharing the document ahead of time will likely cause more problems than it solves. Control the narrative of how the numbers were researched (I'm innocent, it's the HR guy! Or: it's not us, it's the market...). 

The CEO/CFO will likely look overwhelmed and say they need some time to review the numbers in more detail. Share the spreadsheet with them (and have a backup copy just in case they fiddle with your numbers...).

A week or two later (if you are lucky) they'll get back to you and say their CEO friends think these numbers are crazy. They've been hiring COBOL Senior Engineers for $120K so you should as well. Or they might say it's time to open an office in Antarctica because penguins are cheap. Remind them that Starlink isn't available in Antarctica yet and, anyhow, nobody understands how timezones work at the poles. You should probably agree to hire the COBOL engineer and then immediately show him a back-of-the-envolope calculation that the product roadmap needs to be paused for 1-2 years to rewrite everything into COBOL. When your CEO grimaces, solemnly promise that you'll make all initial offers at the bottom of the range. 

After the first couple of candidates negotiate their way up to the middle or high-end, you'll have your ranges finalized.

Repeat once a year to keep things tasting fresh. 

**Common Pitfalls**
1. Your CEO very likely won't care about your ranges -- until it's the worst possible time to care about them. Usually this is when you are about to close a candidate, or put together the 2024 budget off these numbers. 🤷‍♂️ You may need to find a decision pressure like that in order to get the ranges approved.
2. Your entire company should ideally use a common approach, but they won't. You most often end up with very different equity numbers between departments. Keep an eye out for this -- a good way is to ask for advice from your sales/product/operations counterpart on "how are you doing equity grants?" If you notice something VERY off, bring it up with the CFO/CEO/HR team gently.
3. Ranges & Calculators are just a tool. The REAL decision makers are the "cash in the bank" and "equity in the option pool". Make sure you have enough there before you waste time on calculating how many $M that 10-person Bay Area A-team will cost you. If you aren't sure, go hire the penguins.
