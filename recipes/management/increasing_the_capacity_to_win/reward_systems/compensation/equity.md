# Overview
Ah, equity. That delicious little number on your offer that looks like a $1M for some reason. But what is it, really? How does it work? And, most importantly, as a new Head of Engineering, how the hell do I figure out how much to give it, when to give it, and how to feel confident I'm giving the right amount?

Equity is a very complex topic, way too deep to handle here. A great place to start if you are new to thinking about equity is [The Open Guide to Equity Compensation
](https://github.com/jlevy/og-equity-compensation?tab=readme-ov-file#typical-employee-equity-levels). 

The recipes below will assume that you understand a lot of the technical terms around equity. We'll attempt to give you some approaches to quicky build a great equity program for your engineers, and pointers to example artifacts.

# Recipes

## Equity Valuation Recipes
We've seen two broad types of recipes for answering the "how much equity should I give?" question:

1. Market-based valuation: what are other similar companies giving? Find a set of comparables and baseline off of that.
2. Value-based valuation: what is the approximate value of the equity (today or on some future date)? Come up with an estimate and baseline off of that.

The former is the right way to grant equity in the beginning. The equity has basically no value and there is NO formula for determining future value (if there was, Venture Capital wouldn't be a thing!). Following the 'market norms' is the only reasonable thing to do here.

Once a company has lots of revenue ($10M+) and is growing predictably (meeting/beating forecats 4-6 quarters in a row), then transitioning to a 'value-based' recipe might make sense.

### Market-based valuation recipes
TODO

### Value-based valuation recipes
#### Dobromir's Recipe
I always felt a little uncomfortable with the 'market-based valuation' recipes, even though I understand they are probably the correct way to grant equity for early startups. Still, it would be nice to know that startups are giving the right proportion of their equity to employees so that, risk-adjusted, we aren't asking the entire population of startup employees to accept *worse outcomes* than if they went to Big Tech. So this is the recipe I came up with to understand what % is 'reasonable' and what % is 'unreasonable'. 

Ingredients:
1. [Employee market value](benchmarking.md): some fresh data around how much equity this employee could get at a Big Tech company (or whatever their best alternative might be).
2. [Current startup valuation](https://github.com/dobromirmontauk/llm-recipes/blob/main/recipes/management/increasing_the_capacity_to_win/reward_systems/compensation/company_valuation_recipes.md): while this should be easy to get from the company (just ask for their last preferred valuation), valuations have their own recipes -- so make sure you use the one that tastes right for you!
3. [Expected growth rate](TODO): this is mostly guesswork (black magic). Put together some numbers by year using the recipes specified here.
4. [Risk premium](TODO): there is some data at the population level of startups. But each startup is different. Salt to taste.

Now that we have these ingredients ready, we can figure out the appropriate amount of equity ignoring risk. Let’s define these terms:
1. Market value (MV): total $ employee would make on market.
2. On-target earnings (OTE): total non-equity $ employee would make on market.
3. Target Yearly Equity (TE)  = MV - OTE 
4. Growth Rate (GR): 4 year expected growth of the company valuation
5. Valuation (V): current company valuation
6. Valuation Increase (VI): V * GR - V (i.e. how much *more* valuable the company will be in 4 years)
7. Risk Factor (RF): the probability (as a %) that the company will achieve this growth rate.

**The equity grant (EG) should be:**

$$(\frac{TE \times 4}{VI}) \times (\frac{1}{RF})$$

In [spreadsheet format](https://docs.google.com/spreadsheets/d/18ohkLSS3MMsgmS6pTQEfx8HFiwrf3FhtFmVsisJnBvs/edit?usp=sharing) we end up with this:
![image](https://github.com/dobromirmontauk/llm-recipes/assets/50121200/8f33735c-26a3-4398-b15b-974134613753)

**How do you factor in risk?** The equity numbers above assume zero risk in the company hitting those growth targets. I don’t know of any hard & fast rule on how to factor in risk. You could build a “probability distribution” model, or you could negotiate the “growth factor” multiplier (e.g. company says “we are going for 8x growth”, and you can ask for a “6x multiplier since 8x is risky because…”). Risk tends to decrease as the company gets bigger, and you have other benefits on top that might make up for it... To keep things simple, we just apply a risk factor to the final equity BPS.

(My original post on the subject is [here](https://the-edge-of-experience.ghost.io/ghost/#/editor/post/6577762f4d71370001a35478))
(TODO: we are not including dilution in the above math and really we should!)


## New Offer Recipes
### Dobromir's Equity Calculator Recipe
See the bundled calculator in my [Planning Calculator](/recipes/management/increasing_the_capacity_to_win/reward_systems/planning.md).

## Refresher Grant Recipes
TODO

# For Employees
**I thought I’d get rich by joining a Unicorn??**
So… it depends on (a) your value on the market, (b) the stage of the company, and (c) what you consider “rich”. Remember that there is a wide talent pool out there so companies are aiming to get “close” to your market value and not overpay for talent - they wouldn’t be great companies if they couldn’t figure out how to control their largest costs - people!! If you join a very early stage company (pre-seed or just post-seed) and can get a sizable 0.3-0.5% grant, then you’re likely to end up with ~$1M-$3M (post-dilution) when the company hits $1B. Note that could be >6 years after you join so you better have planned to exercise those options if you leave, or be stuck at the company until they are liquid!

If you join a mid-stage company (>$100M in valuation) some of the risk is behind the company and a lot of growth is still ahead of the company - while your value on the market is the same! Since the startup is now likely to generate many $100Ms in value over the next few years your slice of the pie - to get to your market value - shrinks rapidly. Hitting “unicorn status” of $1B will no longer make you rich, and it shouldn’t since that is a “pretty normal outcome” for the startup! Instead, you should be thinking “what is much better than normal growth?” and make sure your equity package looks good if the startup hits those numbers - then maybe the $1M-$3M is back in play.

Most of the stories out of Silicon Valley come when startups do WAY better than $1B - e.g. Snowflake or Airbnb at $100B, very recently. In those cases, people would have done alright at $1B-$10B values, and instead they got 10x better. Our $100K/year Sr. Engineer is suddenly making $1M-$2M/year at Snowflake. 

## Sweat Equity Venture Capital
The one other benefit not discussed above is the upside you have after you stop working there. The model assumes that you can sell your shares after 4 years, and that is all your equity is worth. However, if you have the good fortune of being able to exercise and hold your options, then suddenly you can grab all the growth for the next N years, even if you leave. This is a rare opportunity since otherwise only VCs can benefit from these early, pre-IPO years of startup growth. So if you are patient, and you believe in the company, instead of settling for 4x or 8x increases you can look at 16x or 32x. The risk, of course, increases. Choose your own adventure. 

# Background Reading
https://firstround.com/review/The-Right-Way-to-Grant-Equity-to-Your-Employees/
https://blog.wealthfront.com/startup-employee-equity-compensation/
https://blog.wealthfront.com/stock-options-15-crucial-questions/
https://blog.wealthfront.com/trade-salary-for-equity/
https://www.quora.com/What-are-the-typical-amounts-of-equity-offered-to-engineers-by-startups-of-different-sizes-Specifically-data-for-startups-with-10-20-30-40-50-100-200-500-and-1-000-employees
https://www.slideshare.net/wealthfront/wealthfront-equity-plan/30-well_within_acceptable_range_of
https://www.codingvc.com/analyzing-angellist-job-postings-part-2-salary-and-equity-benchmarks

