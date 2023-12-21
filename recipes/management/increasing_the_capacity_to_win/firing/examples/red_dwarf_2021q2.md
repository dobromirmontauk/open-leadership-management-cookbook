(background: this is a performance review from Q2 2021)
# Overview

Red Dwarf is **missing expectations **as a Staff-level Software Engineer at Doxel. 

In my [last review](NEED LINK) a year ago I called out many areas for improvement that Red Dwarf should focus on over the next few quarters. I also pointed out that Red Dwarf generally was not amenable to feedback. I followed up that review with many discussions in 1:1s, some of which pointed back at the review and reminded him of key issues he needed to address, like Ownership. 

A year later, he has not improved in most of those areas. The quality of his work has actually degraded. His [Quality data analysis](REDACTED) was full of logical gaps and I had to send him back to redo it twice - and it still doesn’t have trustworthy data. His design docs like [HALT]() are not consumable by others and it’s very rare to get documentation in written form from him. Even his self-review contained no data to back up some of his claims, which caused him to take credit for work with no impact (which I called out in the last review as well). Our Staff bar is [very well defined]() and Red Dwarf is not operating at that level across many areas.

As a Staff SWE who has had a year to improve with regular feedback he should have a very good idea about our expectations and his gaps towards meeting them. I’m giving Red Dwarf 30 days to make significant improvements to his performance if he wants to remain at Doxel as a Staff Software Engineer. I’ll be checking in with Red Dwarf again in early June to see if he’s met our required bar or not.



# Strengths


## Domain Expertise

This was a strength in the last review and continues to be the main bright spot.

Feedback

* Magnetometer work - he took that and ran with it, was good work.
* HALT is a very effective alignment method.
* He is very good at a specific set of things. Signal processing and geometry. 


# Areas for Improvement


## Not Data-Driven

As written above Red Dwarf does not proactively try to gather and analyze the data to see if his intuition is correct. He prefers to skip that step and just roll things out. I believe this is a symptom of what I called out in the last review - Ownership. If he really cared about having true impact he’d push himself to find the data to prove it; since he’s happy just solving the brain teaser the data won’t teach him anything he’s desperate to know, so he skips it.

For the Quality project I was also directly involved with his data analysis and was very worried to see that he wasn’t able to reason about the size of the dataset needed for statistically-significant conclusions to be reached. He felt comfortable publishing numbers between two approaches when they weren’t even tested on the same set of data. This was an incredibly cavalier attitude that would have had his work rejected by any journal and definitely doesn’t set the right precedent for Doxel’s engineering team.

Feedback

* Doesn’t provide evidence for the improvements he is making. Has bitten the team in the butt with rollbacks. 
* [PEER] is pushing for a more scientific approach - I’m surprised that Red Dwarf is not super on-board on that. Maybe he doesn’t have a lot of experience with that type of approach? 
* He’s effectively developed a couple of good things. He’s been successful on his intuition. I would like to see a more data-driven approach. We don’t know when we will make things worse - that’s a particularly a problem to making something running in production. 


## Production-grade work

In my last review I wrote: “Over the next quarter Red Dwarf needs to display better ownership by getting his projects from “works on his computer” to “works in production reliably for a month”. While he has invested some effort into understanding DXDB and Airflow (after a lot of prodding) he’s caused an unnecessary load on the team by pushing code that doesn’t work. In a recent 1:1 I even asked him how often he used the new local Airflow environment; he pointed out that rarely because “I just wait to be oncall, then I push my changes, and it’s OK if it pages because I can handle it right away.” This showed an incredibly naive and dangerous mindset about production reliability. 

Feedback

* Problems with automatability. It’s good work. He does maintain it (“in his own way”) and is available to improve it.
* But philosophically, having someone who doesn’t want to be more rigorous, from a mentorship perspective he is not setting the right example.
* He has good ideas. He fails in the systems piece, he’s had to do systems stuff. 
* He puts very little effort into improving the system. Very little effort into integration.
* He does not meet the bar for what Doxel needs. Finding improvements, demonstrating them, and deploying them. He is a good “member of technical staff” → once Doxel has the right abstractions for him to do well, he might be close to Staff… but we have not given him that opportunity to shine.


## Collaboration & Leadership

In my last review I wrote: “For Red Dwarf to exceed expectations in the next quarter he needs to take team membership seriously and put the goals of the team above his own personal interests.” He continues to be mostly a “black box” that doesn’t communicate well and makes it very difficult to integrate him into other teams. 

Feedback



* Communication is the main problem Red Dwarf has. He is not being clear on what he is trying to do, how he is trying to do it, and why he believes he will hit the timeline. I tried poking him many times on this and he was not really communicative about it upfront. He was not keeping people on the same page when things changed. Especially in a cross-team contributor it’s really important for you to be communicative. 
* He was getting blocked on other people and it came as a surprise. Unclear when he is blocked vs when he is just asking a question. 


# Performance Score



* Expectation of Role (role expectations for Engineering are [here]()): 1
* Contribution to Team: 1
* Doxel Virtues: 3.1
    * Ownership: 2
        * _Don’t see 5, I see it as much lower. We’ve had with issues with his definition of “done”. His version is “code complete, works in prod” but without evidence of ROI. He’s not eager to improve when corrected. We’ve had public, poignant tiffs in standup about PRs being too big; he doesn’t own it. No desire to improve on this._
    * Humble: 4. 
        * _Doesn’t tout his own horn. _
    * Empathy: 3
        * _surprisingly empathetic in the colloquial sense; I tend to rely on him to change my thinking about that stuff. He’s good at understanding other people’s suffering. Your definition: see a little about it but not proactive. Maybe high-3s? _
    * Decisiveness: 2
        * _He wants to have impact, he values the recognition, but he doesn’t understand how to have impact. In many cases the things don’t get done end-to-end. E.g. Activity Cloud; orphaned project but hugely valuable. He didn’t drive it home._
    * Intellectual Honesty: 4.5
        * _pretty good at this. He’s quite comfortable challenging authority. Sometimes way out of sync. Might be overdoing it. I don’t think he values getting hard feedback, he doesn’t listen and incorporate other people’s ideas as much. _
* Overall Doxel Impact: 2