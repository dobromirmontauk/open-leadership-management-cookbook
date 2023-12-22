# Responsibilities & Projects

As Head of Engineering I don’t work directly on projects so I’m calling out three major responsibilities I’ve had over this review period.

(I will also be putting together a scorecard for my role as Head of Engineering - in the meantime here is an [example scorecard](https://drive.google.com/open?id=1fA9nObYf29d-FLE9jwIFm2JTOK8G4m4Z) from a different company)


## Team Building

**Responsibility**: to build a world-class Engineering and Operations team that is able to scale up [COMPANY] to hundreds of customers over the next few years with the right combination of technology, process, and training. 

**Contributions**: I’ve significantly increased the capacity of the Engineering and Operations teams through a combination of hiring, coaching, and process improvements:



* 10 engineering hires (on a base of 12), of which 5 are Senior level, which is enabling us to get out of firefighting mode and into investment mode.
* X operations hires, including a Sr. EM of Operations, which enabled us to execute on current customers and have room for new customers.
* Process improvements to make engineering work more focused and impactful: [new team structure](https://docs.google.com/document/d/15ZBTtmuUsXxlGdwFHE1yCU1Y7-URqR5kp8ahxL98SVE/edit?usp=drive_web&ouid=115234162360957637188), a better [sprint process](https://docs.google.com/document/d/1I25UM3LdF7isTDUDcuKNBZXHCvaEwDUwmro0B7a4Ywk/edit) (and encouraging [sprint](https://docs.google.com/document/d/18JFewb0M3mHg_1QOFvowE96rahq5JURmjdw9s1TTcRI/edit#heading=h.674zas4pgb3v) [reports](https://docs.google.com/document/d/1WfhK2dpuyRhUdF3p3MXi6FrkdZOUeS6d22DNAK5iGKY/edit#heading=h.lncmpemsfp3u)), and [more](https://docs.google.com/document/d/1_L3KdSN30ZhWauY7CkL5xuJhdjECz3Ce7iKhXwZD5Zc/edit) [long-term](https://docs.google.com/document/d/1viNjkQzRuNLl6x99oN6s92uXEZmwH893VIqbvUcdaAM/edit#heading=h.xizhcc6tre0r) [planning](https://docs.google.com/document/d/1iTano1lMhBG9hLfhRpjcYOH1GV_u7PWwW6qX_HMPf9E/edit#heading=h.kb75xeskow8n).
* Regular 1:1s with all direct reports to hear concerns and funnel information through the organization. I think I’ve done a decent job listening to individuals and helping them influence the organization.
* Significant investment in coaching new leaders on the team: [EMPLOYEE], [EMPLOYEE], [EMPLOYEE], [EMPLOYEE], [EMPLOYEE]. Significant investment in onboarding new engineers, including our [Onboarding](https://drive.google.com/drive/u/0/folders/1uGpefxT83WigrngsT-_7rZRj_w1J9fjm) docs and onboarding [classes](https://docs.google.com/document/d/1PPX8XP4jNpYc14z2oWBaQPuyk36pk4qzvN8w7ZarhDY/edit?usp=drive_web&ouid=115234162360957637188).

**Contribution Impact to Project/Responsibility**: critical.

**Improvements**: 



1. Hiring: our close rate is ~28% and we did very poorly on hiring new grads (1 hire out of 20+ interviews). We over-emphasized new grad hiring too early - we lost quite a few candidates because they were concerned about getting mentorship. We should have closed senior candidates first. Also, I haven’t calibrated my “up-stream filter” to people who aren’t actually likely to join startups and so we get a lot of solid candidates who have cold feet at the offer stage.
2. As the team has hit 20+ engineers my ability to have 1:1s and pay attention to all the interpersonal issues is strained. I haven’t put a structure in place that lets us run effectively at this scale, mainly because I’m keeping the organization flat as long as possible in an attempt to stay nimble. I definitely am noticing that I don’t have as much of a read on certain individuals/subteams as much as I used to. E.g. I haven’t been able to regularly check-in with folks on the Customer Engineering team to see how the culture is evolving with [EMPLOYEE] as the new manager. 


## Execution

**Responsibility**: as Head of Engineering & Operations I need to ensure that our organization is delivering our product to customers every week while also building the technology to scale up the product with minimum human capital over the next few years.

**Contributions:**



* In-door scanning across [CUSTOMER], [CUSTOMER], and [CUSTOMER] (after reboot) have almost entirely been within customer expected SLA. In many cases this came from personal elbow grease (daily check-ins, process improvements, tech improvements…), in others by effectively delegating to the right individuals who take ownership and customers seriously.
* [CUSTOMER] pilot went OK (and satisfied the customer) due to [planning](https://docs.google.com/spreadsheets/d/1iP9hemjRxRKfX8fyuCB2Iae3MUTyvhftGa51wuqSHUM/edit#gid=2118181387) and [several](https://docs.google.com/document/d/1l2CMD-1qErCOFiQng9Ymz_WFWSX7E-UY0l3osuNL7fM/edit#heading=h.sov46q3cn3xw) [postmortems](https://docs.google.com/document/d/1MhjJcg_tfsqfHbXzxB9uiezJJSydxh54gt6A8s54gkY/edit#heading=h.sov46q3cn3xw) so we’d learn how to bring up a new site. Engineering and Operations should be able to handle multiple pilots per month now.
* Data Pipeline rollout: we went from zero data going through the data pipeline to an 50% complete solution that provides value in the alignment side and occasionally annotation side. Moving to GCP, BigQuery, Airflow, and Postgres has also given us the foundations to make future execution much faster. 
* Our Web frontend has gone from a per-customer bespoke experience to a generic, configurable framework that can launch a new customer in ~hours instead of ~days. I worked closely with the Web team on product strategy, technical evaluations (Mode), and executing the various projects.
* Scaling up Rovers from zero in production when I joined to 10 built and 3 (soon 4) actively in production. The team did most of the execution here; I contributed via setting the goals, removing roadblocks, and hiring Mike to help drive things. At the beginning of the year we thought building Rovers would be our [bottleneck](https://docs.google.com/document/d/1_L3KdSN30ZhWauY7CkL5xuJhdjECz3Ce7iKhXwZD5Zc/edit#heading=h.ogop6iam8j1a) :) Turns out we were wrong!
* Introduced many process improvements to help execution: Product Planning, CEO Staff meeting, weekly Eng Staff meeting, more effective standups, and better Sprint hygiene.

**Contribution Impact to Project/Responsibility**: Critical

**Improvements**: 



* My lack of domain expertise around computer vision and robotics made it difficult for me to predict where we had significant technical risk and invest engineering resources appropriately. As such, we way under-invested in pieces like SLAM and registration earlier in the year (assuming they would work or be easy) and now those are bottlenecks in our ability to scale up. I still need to get better thinking through where the risks are, or having in-house experts that I can rely on to bring up these risks.
* A lot of technical work that we planned 6 months ago hasn’t been completed or is being done with lower-than-appropriate quality. Examples include our database still not being a primary tool in the data pipeline, LabelBox/NavisWorks annotation integration not being 100% automated, and lack of testing across the board (from Web FE, which suffers quality issues regularly, to data pipeline, which frequently breaks due to simple human errors that we don’t test pre-emptively).
* VAN was a shit-show and [CUSTOMER] had significant issues at first, and I waited too long to realize the seriousness and turn those projects around. This almost cost us our VAN pilot success and still risks our ability to convert the pilot. I’ve realized that from past experience I’ve learned to wait for “bad news” but I never set the [COMPANY] culture to bubble up bad news, and didn’t train individuals on how to do so. We are working now on that now, e.g. by rolling out SLAs we track across every scan.


## Technical Leadership

**Responsibility**: provide the right amount of technical leadership - not too hot, not too cold - so that the engineering team can keep improving and executing.

**Contributions**: 



* Spearheaded the effort to move to databases as a key foundational piece (BigQuery/Postgres). While not 100% completed (see execution above) this has already significantly simplified our stack (no more protocol buffers being passed around!), increased reliability, and increased flexibility.
* Spearheaded moving our metrics to a 3rd party (Mode analytics) instead of building everything in-house. Setting the culture of “if you can buy it, or run someone else’s software, do that instead of building it.” No point in reinventing the wheel at a small startup.
* Spearheaded the move to GCP and worked with Mayur to build a solid foundation with IaC and a better permissions/security structure than our AWS setup.
* Spearheaded [collaboration with Main Street Autonomy](https://docs.google.com/document/d/1USRpOQIEyZKRzzcSXv2gvDPQucgS3xlntm9AjMwRN_Y/edit) to leverage their expertise in building out a better SLAM stack rather than us doing it in-house.

**Contribution Impact to Project/Responsibility**: medium

**Improvements**:



* I’ve been able to provide technical leadership in the areas that I’m familiar with (production, distributed systems, data pipelines) but unable to provide much in areas foreign to me (robotics, computer vision, machine learning). This has hurt execution (see above) and also means the team needs more senior people in some areas to help grow junior engineers. My role should be to educate myself where appropriate, and hire great engineers otherwise.


# Strengths



1. **Fast learner**. I believe I’m incredibly fast learner (when I have enough time) so I can pick up new domains and become effective at them. At [COMPANY] I’ve had to learn the construction business, some robotics, and some computer vision… I think I was able to understand everything well enough in &lt;6 months to effectively have engineering and product opinions and lead the Eng & Ops organizations
2. **High standards**. This may sound strange as a strength so I’ll explain: as an engineer and leader it’s tempting to let low quality work slide which leads to standards eventually dropping. Keeping standards high - via constant feedback and pointing out when work is not up to expectations - takes energy and diligence. I prioritize this constantly.
3. **Leadership**. I really enjoy [coaching leaders ](https://github.com/dobromirmontauk/engineering-scorecards)and I think I do a good job of the fine balancing act leadership requires. I can shift between coaching and directing, inspiring and driving with urgency, listening and telling, delegating and owning directly, creating pressure and creating space, prioritizing employees and prioritizing the business. 


# AFI



1. **Frustration**. I’ve gotten frustrated with individuals at [COMPANY] a few times and this has led me to having heated arguments which were not productive. The bigger the disagreement the more important it is for me to keep my cool so people feel comfortable approaching me with contentious issues and come to a resolution together.
2. **Candidate Startup Alignment Filter**. I haven’t been able to determine early in the recruiting process how aligned a candidate is with a small startup. I need to rethink what signals demonstrate that an individual is really good material for a startup. Most of my past experience has been hiring into larger companies and I’m more attuned to people’s concerns and decision-making in those environments. I’m not sure yet how to improve here other than practice.
3. **Performance Management**. I’ve had challenges tracking progress and therefore discovering team and individual performance issues at a company like [COMPANY]. The fact that we span the gamut of in-field operations to hard-core algorithms to general SWE means no single tool works for everyone and it’s harder to keep individuals accountable (since failures can happen multiple places). I’m still iterating on and testing ways to have the right visibility and accountability needed to make the company hum.


# Contribution to Team

My primary team is the leadership Staff meeting ([CEO]’s reports). My job is to represent Engineering and Operations for the company. My contributions to the team should be focused on making it more likely [COMPANY] is making good decisions, hiring the right leadership, and executing to the plan. A few things I’ve done:



* Contributed to the hiring of our VP of Finance, via actionable feedback on candidate set.
* Set up the [COMPANY] Staff meeting to discuss the most important issues facing the company. I organize the meeting, take notes, and make sure we are following up on action items. Small but important :)
* I’ve communicated Engineering plans, budgets, hiring plans, etc to make sure the Staff team is informed about everything happening in the organization.

Improvement: I feel like I haven’t represented the Operations team nearly as well at the executive level; e.g. this led to a misunderstanding on resourcing needs for various projects. I need to gather the right level of visibility from Mike to bubble information up and help make the important decisions with the right information.


# Demonstration of Company Virtues



* **Ownership: 5 **
    * Example: I’ve done everything from jump into reviewing LabelBox labels to writing code to hiring people to negotiating contracts. I try to apply my time and energy in the direction that will help move the company forward the fastest.
    * Example: I do my best to understand all the executive functions at the company (sales, finance, product) so I can direct the engineering & ops teams correctly, with what is best for the company as a whole.
    * Example: I proactively had engineering start sharing metrics in All Hands - even if they don’t look great - so that we hold ourselves accountable to end success.
    * Example: I’ll jump on any fire, at any time (weekends, evenings, etc) to help things along if I can.
* **Decisiveness: 4**
    * Example: made the call early on that we should focus on a single data capture platform and see how well our platform can perform. 
    * Example: helped set up the [COMPANY] Staff meetings so that decisions could be made quicker and course-corrections made with full buy-in of the exec team.
    * Example: Not a level 5 yet since I sometimes take longer than I should on making and executing decisions. E.g. restructuring the team and certain performance issues should have been handled faster.
* **Humble: 3**
    * This is something I’ve struggled with for the majority of my career. While I feel like I’ve gotten to L4 or L5 internally (I certainly believe I can only succeed by being surrounded by better peers) I realize I don’t always appear that way. I’ve consistently gotten feedback that I can be overbearing and appear haughty. This probably comes from a lack of internal patience which I need to work on.
* **Empathy: 4**
    * Example: I understand the difficulty of being remote employees and try hard to make sure they are included equally in the company events (All Hands, planning, etc).
    * Example: I care deeply about every individual's happiness and regularly spend 1:1 time to understand how their work is affecting their life and how we can improve things. With some people I could probably have a better connection to make this easier but overall the intention is there and I think I’m mostly successful.
    * I have not yet developed a sixth-sense for the needs of overs, consistently. I’m occasionally still surprised when people come to me with issues since I haven’t noticed them myself. I need to work on a better “map” of each individual and see when they are behaving differently than the map suggests.
* **Intellectual Honesty: 5	**
    * While I’ve always had a streak of honesty it used to be caustic (putting me in L3). I believe that now I’ve learned to both be challenged and challenge myself in a way that focuses on the problem and not the people, avoiding conflicts. 
    * Example: Robin and I have had numerous discussions 1:1 where I’ve disagreed and we had a good debate :)
    * Example: when the Engineering team is slipping on goals I bring this up proactively with Staff team to explain why and how we can improve.