**The Award**



* ~~Every [EMPLOYEE] can nominate **one person per month** for the #RGSD award.~~
* ~~Nominations go on the #RGSD Slack channel. You can also use the :rgsd: Emoji to send an example of great #RGSD to this Slack channel.~~
* **~~Every individual nominated gets a $100 bonus if they are eligible:~~**
    * ~~The work has to be a good example of #RGSD. ~~
    * ~~Maximum of one award received per month.~~

**Eng Motto: Rigorously Get Shit Done (RGSD)**

The keywords here that define us vs other engineering groups are _rigor_ **and** _done_. Why do I have those two?

Done: defining _done_ isn’t easy, and that’s the point. Done is about impact over activity. It isn’t _done_ until it has solved the problem: the technical problem, the customer’s problem, or the business problem. It isn’t about shipping code or closing tickets. It’s about moving the actual metrics that matter. We don’t want to get mesmerized by the illusion of speed at the cost of moving the needle. 

Rigor: this is required because of the unique environment [COMPANY] finds itself in. Let’s contrast ourselves to other companies and cultures. What inherent differences require us to act differently in order to succeed?



* Small client base - likely forever. We could be a $1B company with just 1000 construction sites and &lt;10,000 monthly users. Each project and user interaction is a precious, precious moment.
* High-value, low-frequency touch points. Our customers use us just a few times during a monthly cycle, often for just a few hours. 
* Physical world complexity. We run hardware on real-world sites; data collection, hardware experimentation, etc is much slower due to this dependency.
* Remote team. We are already distributed across half a dozen timezones. Communication is difficult: VC is lower-bandwidth than in-person. Finding overlapping times is becoming increasingly difficult. 
* Hard problems: ML / CV have never been done. This type of product has never been done.
* Suspicious customer base. Construction Tech has its share of broken promises and failed technologies. Our customers are suspicious that we can do what we say we can.
* A [Small Data business](https://medium.com/dangerous-engineering/a-reference-guide-for-fintech-small-data-engineering-bd65b9796d90). The correctness and accuracy of the data is critical. 

       


All of this means that, for us, **experimentation in production is expensive. **In the spectrum between NASA-style Mars missions and Facebook-style “break & rollback”, we are definitely somewhere like SpaceX; we can iterate on the weeks-to-months scale, not the minutes-to-days scale. 

This is why _rigor_ is necessary. 

Without rigor we will _feel_ like we are moving fast (“look at all the stuff I’m doing!”) but we will fail to _move_ fast (“look at all the goals I’m missing!”) when the reality of our **slow production iteration loop** hits us. 

We need to enforce rigor in these places across all of EDPR:



1. Goals: what is important to accomplish?
2. Research: what are the options to achieve them?
3. Design: which option is the most likely to succeed?
4. Planning: how do we tackle it?
5. Communication: how do we avoid confusion on who, what, when, how? 
6. Execution: how do we track, unblock, learn, and revisit the decisions if necessary?

How do we know we are being rigorous? When we have very few surprises. Unacceptable surprises are when customers are disappointed in what they see - or they don’t use it. That is our “rocket blowing up” scenario. Surprises upstream might include product functionality not working as expected, engineering systems having bugs, additional necessary work exposed during execution, etc.

**Our culture will be rigorous when, without any external pressures, teams convert a surprise to an upstream change that reduces the probability of those surprises in the future.**


## How do we balance the two?

Get Shit Done is the goal. Rigor is supposed to help us achieve it because of the environment we operate in. If you read it carefully you can see we did _not _say “Rigorously, Get Shit Done.” The most important part is to define _done_ and then rigorously execute against it in the best possible way. 

In some cases, more emphasis should be on the rigor: “yes, you got this TDD done, but is it really rigorous? Or are we going to run into tons of problems implementing it that will actually slow us down in the real _done_ - the customer impact?”.

In other cases, more emphasis should be on the done: “why are we spending 3 weeks putting together a TDD for engineering work that might last just a month and has low risk?”

The point of RGSD is to make people _think_ if they know what _done_ means, and if they are applying the right level of _rigor_ to actually achieve it. Leaders at [COMPANY] need to wield this phrase carefully to drive that thinking.  


## What do we change in how we behave - immediately?

**We need to learn from every customer interaction**. Like SpaceX, every Schedule review, every EAC review is our “rocket launch.” _We need to collect and analyze the data from every single one._ We need to improve our system, even if slightly, for the next one - in 1 week, 1 month. Today we are failing to do this! This is an example where we need _more rigor_ because it will help us _move faster_. 

**We need a serious Product Research arm**. Large emphasis on design, prototyping, and product-led research. Learning via sales calls, or by showing designs to current customers, or (worst case) launching to customers is **unnecessarily slow and not rigorous**. We can burn months learning things that could probably be learnt in weeks. We should build up our Design and Product teams to **maximize the probability** that we actually build the right thing.

**We need a better writing culture**. Thinking that is not written down is not rigorous. We need something like Amazon’s 6-pager culture for Product investments. We need TDDs to have better thought-out engineering designs. We need clearer PRDs to avoid [building a feature and then realizing it can’t launch](https://docs.google.com/document/d/1WC3Y0Rp4zyw1-RDWIM9FSS49dBBEdoq1vTNb8kv5LI8/edit). We need better JIRA tickets & comment threads so we can re-analyze where rigor was missing and improve.

**We need metrics**. We are a data company that tracks construction at an incredibly granular level but does not, by default, review or share numbers internally. Teams don’t do metric-first approaches to “what is success?” This is visible in our OKRs (“launch this”), our designs (“store this, no idea how much it is”), etc. 

**We need to make calibrated assessments. ...**

We need to make the implicit, explicit. ...

WHAT ELSE IS NOT RIGOROUS TODAY AND SHOULD BE?


## How do we implement this?



* #RGSD hashtag
* Sharing stories
    * Saurabh Series B on the airplane
    * What other stories are part of the cannon?
* Symbols
    * Names - conference rooms? Projects? RGSD - can’t be too cheesy, needs to be genuine
* One pager on rigor
    * Truths
    * First principles
    * Finding assumptions 
    * Essence
    * Concise, precise, well-thought-out
    * “Can’t remove any pieces”
    * We are doing HARD ENGINEERING. R&D.
    * 
* One pager on Getting Shit Done
* Onboarding
    * RGSD session
    * RGSD 4-week retro
        * Sign up for fixing one thing in the next 3 months. “GSD”
        * The doc is Rigorously
* 