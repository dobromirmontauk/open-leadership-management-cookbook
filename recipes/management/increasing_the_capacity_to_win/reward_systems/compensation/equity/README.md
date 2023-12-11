# Overview
Ah, equity. That delicious little number on your offer that looks like a $1M for some reason. But what is it, really? How does it work? And, most importantly, as a new Head of Engineering, how the hell do I figure out how much to give it, when to give it, and how to feel confident I'm giving the right amount?

Equity is a very complex topic, way too deep to handle here. A great place to start if you are new to thinking about equity is (The Open Guide to Equity Compensation
)[https://github.com/jlevy/og-equity-compensation?tab=readme-ov-file#typical-employee-equity-levels]. 

The recipes below will assume that you understand a lot of the technical terms around equity. We'll attempt to give you some approaches to quicky build a great equity program for your engineers, and pointers to example artifacts.

# Recipes

## Equity Valuation Recipes
We've seen two broad types of recipes for answering the "how much equity should I give?" question:

1. Market-based valuation: what are other similar companies giving? Find a set of comparables and baseline off of that.
2. Value-based valuation: what is the approximate value of the equity (today or on some future date)? Come up with an estimate and baseline off of that.

### Market-based valuation recipes
TODO

### Value-based valuation recipes
#### Dobromir's Recipe
I always felt a little uncomfortable with the 'market-based valuation' recipes, even though I understand they are probably the correct way to grant equity for early startups. Still, it would be nice to know that startups are giving the right proportion of their equity to employees so that, risk-adjusted, we aren't asking the entire population of startup employees to accept *worse outcomes* than if they went to Big Tech. So this is the recipe I came up with to understand what % is 'reasonable' and what % is 'unreasonable'. 

Ingredients:
1. (Employee market value)[TODO]: some fresh data around how much equity this employee could get at a Big Tech company (or whatever their best alternative might be).
2. (Current startup valuation)[TODO]: while this should be easy to get from the company (just ask for their last preferred valuation), valuations have their own recipes -- so make sure you use the one that tastes right for you!
3. (Expected growth rate)[TODO]: this is mostly guesswork (black magic). Put together some numbers by year using the recipes specified here.
4. (Risk premium)[TODO]: there is some data at the population level of startups. But each startup is different. Salt to taste.

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


## New Offer Recipes
TODO 
## Refresher Grant Recipes
TODO
