# What is My Startup Worth?

This is a surprisingly hard question.

The easiest definition of "what is something worth" is "what would someone, right now, be willing to pay for it?" They
might have their own, complex decision process about how they would come up with that number... but if there are enough
such individuals, we can be blissfully ignorant of how they came up with the number and simply call it the "market
price." This is how public companies function: anyone can buy & sell their stock, so even though everyone is making
these decisions in a different way, a final price is agreed upon every time a buyer/seller transact. Unfortunately,
private companies by definition don't have a market for their stock, so we can't look up the 'public market price.'

Instead, we can use one of many different recipes for coming up with this number. Note that these recipes may yield VERY
different results: use at your own risk :)

## Discounted Cash Flow (DCF) Recipes

[DCF](https://www.investopedia.com/terms/d/dcf.asp) is a simple concept. What an asset is worth today is simply the
value of all the "cash flow" (money in your pocket, roughly) that you will get from it, within a certain timeframe,
where future $ are "discounted" because they are worth less than a $ today (inflation). This recipe would be foul-proof
if there weren't so many unknowns:

1. How much cash will I generate in the next few years? 🤷‍♂️
2. How much will my taxes, expenses, etc eat from that cash? 🤷‍♀️
3. How much will inflation reduce the value of the cash? 🤷

You can a feeling for the recipe [here](https://www.wallstreetprep.com/knowledge/terminal-value/). It's pretty complex
though, so we don't often see it used in valuing startups as Heads of Engineering.

## Forward-Revenue Multiple Recipes

For high-growth companies looking at **next year's** revenues and multiplying by some "market factor" is the most common
approach (that I've heard of). So this deserves a few recipes of its own.

### Tom Tunguz's Recipe

See [here](https://tomtunguz.com/correlates-to-forward-multiple/). Note this is from 2020 which was very frothy; this
recipe may not work so well anymore.

### Dobromir's Recipes

Throwing together a spreadsheet for ARR multiples is pretty easy. We just need a few ingredients:

1. [Current forward multiples](https://tomtunguz.com/how-markets-value-saas-in-mid-2023/): as of this writing, the best
   25% of public companies have ~10x multiples, the worst have ~4x multiples.
2. [Company growth rate](TODO):

Now that you have this you can throw
something [like this](https://docs.google.com/spreadsheets/d/1udlOD-M2_EGtZq6xmXNbEPN_me4l1tAznZKzr18mCHY/edit#gid=0)
together. Here we compare
the [2021 multipler on current ARR](https://www.linkedin.com/pulse/100x-arr-multiple-tomasz-tunguz/) versus the more
common forward-revenue multipler.

![image](https://github.com/dobromirmontauk/llm-recipes/assets/50121200/b0b820aa-ff88-4967-a99e-7c5a5dc99c67)

Since the data we have on FRM is for public companies, we drop the FRM every year until it reaches public-company
thresholds.

More useful reading:

https://tomtunguz.com/figma-acquisition/
https://tomtunguz.com/rates-and-multiples-2022/
