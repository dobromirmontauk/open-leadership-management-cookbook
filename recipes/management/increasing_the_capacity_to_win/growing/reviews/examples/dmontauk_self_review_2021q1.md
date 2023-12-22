# Responsibilities & Projects

Over the course of 20XX I transitioned from a Tech Lead/Manager role to a more traditional Director-level role (managing managers). I’m packaging up my individual contributor work into one “project” for expediency despite personally delivering several major projects. 

Previous self-review: [Dobromir's Self Evaluation Q4 20XX](https://docs.google.com/document/d/1yuMyMNO9XPCRThTOnuILwAbiYjyM8fJjrCCPc8YlAVU/edit#heading=h.3icszsnnjdvy) 


## “[COMPANY] Technical Architect”

**Responsibility/description**

Responsible for making major architectural/infrastructure decisions across the [COMPANY] platform and kicking off projects to guide the technical direction for the rest of [COMPANY]’s engineering team. I took over this role after we decided we didn’t have the budget to expand the Engineering team. It became crucial after the COVID-related RIF since we were very tight on engineering resources.

**Your contribution**

In 20XX I was incredibly prolific in terms of the code contributed and my code reviews of other engineer’s code, especially in the Annotation, Data Platform, and Customer Insights teams. 



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


Biggest contributions include:



* Personally ensuring that our Data Pipeline was green from Jan-March and teaching DC and AN teams proper on-call hygiene and [procedures](https://github.com/[COMPANY]-AI/doxel/pull/739/files). This was the foundation that allowed us to reliably hit customer SLAs (see below in Head of Engineering section).
* Rebuilt the entire Annotation pipeline ([twice](https://github.com/[COMPANY]-AI/dxqs/pull/63)) to support Shell, transition from CSVs to our Annotation Plugin (Project Mysore), and reduce the customer-visible bugs significantly via testing.
* Rebuilt our database to support (mostly) an idempotent data pipeline with history and support for multiple annotation sources. This was the foundation that allowed us to experiment with Machine Learning, Connectivity Graph, and Dependency Graph approaches for annotation automation.
* Worked with [EMPLOYEE], [EMPLOYEE], and [EMPLOYEE] to develop our [API server approach](https://github.com/[COMPANY]-AI/doxel/pull/706/files) and transition a major piece of our infrastructure from Airflow to live API calls. This had a huge impact on our annotation costs (see below in Head of Engineering section). 
* Along with Matt and [EMPLOYEE] invented the [Construction Encyclopedia](https://github.com/[COMPANY]-AI/doxel/pull/1664). This was a foundational piece that allowed us to start scaling ML, Schedule, and EAC across customers by standardizing all BIM models into a single language. This was a key piece of technology in our [Series B pitch](https://docs.google.com/document/d/1XdXELV3UvZ1KH1cDdTywOv2D5LKvPZnCRo83DTrtBvY/edit) to [investors](https://drive.google.com/file/d/10BmmCAEJnsKLo20l4vlPoHGi0jPgs9ip/view?usp=sharing). 
* Developed [COMPANY]’s [first Metrics system](https://github.com/[COMPANY]-AI/doxel/pull/991) to [really measure](https://github.com/[COMPANY]-AI/doxel/pull/1079) Annotation OKR metrics. Continually refined the metrics to guarantee they were [correct](https://github.com/[COMPANY]-AI/doxel/pull/1137) and [well-understood](https://github.com/[COMPANY]-AI/doxel/pull/1545/files). These were key in catching the fact that our ML performance was not actually working in production.
* Along with [EMPLOYEE] rebuilt our entire EAC product on top of [DXDBv2](https://github.com/[COMPANY]-AI/doxel/pull/1667/files) and vastly improved [PayApp](https://github.com/[COMPANY]-AI/doxel/pull/1757), [Field Report](https://github.com/[COMPANY]-AI/doxel/pull/1755/files), and WBS importing. Spent countless hours with Matt [debugging differences](https://drive.google.com/drive/u/0/folders/1sjZF1q8V6U9kXWKeAbV4Hbp_JRJtL5X8) between new system/old system to guarantee accurate reporting.
* Significant contributions (along with [EMPLOYEE]) to original Schedule quantification, design, and implementation.
* Tons of [code reviews](https://github.com/dobromirmontauk?tab=overview&from=20XX-12-01&to=20XX-12-31), experiments like [DataFlow](https://github.com/[COMPANY]-AI/doxel/pull/1605) and Aquarium, migrating to [Monorepo](https://github.com/[COMPANY]-AI/doxel/pull/1340/files), unit tests, etc. Generally pushed hard on improving [COMPANY]’s overall engineering quality and output.

**Impact**

Critical. Many of the technical foundations I implemented are relied on for all our products and scale efforts.

**Areas for Improvement**



* Some of the work that I did probably ended up orphaned (e.g. metrics) because there wasn’t a clear owner when I had to move out of the engineering role.
* Ran a bit too fast in certain places (e.g. DataFlow experiment) where the investment wasn’t yet necessary.
* Should have spent more time training people on the work I was doing instead of handing over 80% finished code.
* I probably should have transitioned out of the engineering role into the Head of Engineering role a few months earlier; we were late in kicking off hiring and more strategic pieces because I was spending so much time coding.


## Head of Engineering: Execution

**Responsibility/description**

The #1 responsibility of every manager is to win with the team that they have. As Head of Engineering I staffed projects, made bets, provided guidance, etc to help _my teams win_. My output is the sum of the output of my teams; thus most of the credit below goes to other individuals/teams. I am aggregating it here to show how Engineering execution in 20XX was critical to [COMPANY]’s success. 

**Your contribution**



* Make [COMPANY] reports boring again: at the beginning of 20XX we were [struggling](https://docs.google.com/document/d/1LDPARv8VqoQTwXZqKcBGEgQ3DOY7RHgAi_-UcfazIkg/edit#bookmark=id.gfzmbqnhv0su) to deliver our weekly progress reports and monthly EAC reports within SLA. We didn’t even have ways of measuring our SLAs and thus really improving them. We made quite a few bets and improvements and now our weekly SLA reports are quite boring. This has been critical to allowing the business to continue to scale smoothly.
    1. Migrated from Faro/Rover combination to M6/VLX. See below for details.
    2. Automated the vast majority of _manual_ work (i.e. does not require human judgement) from Data Capture (DxUploader, Airflow) to Annotation (Navisworks Plugin + API) to Schedule/EAC (Airflow). In most cases, humans are not copying files, importing point clouds, etc - we have tools/systems for everything. This has made _measuring_ and _improving_ possible.
    3. Made significant progress in automating registration + alignment pieces. Registration is fully automated via Navvis pipeline and alignment has [&lt;40% human involvement](https://doxel.slack.com/archives/C014FNFDU3G/p1617136739003300). 
    4. Developed an SLA culture/oncall culture, including [rolling out PagerDuty](https://drive.google.com/file/d/14BinAODC9pfI6jso6Svxg_KvxS5USQg0/view?usp=sharing) to engineering teams and reporting on SLAs at [every All Hands](https://docs.google.com/presentation/d/1knK_rZMzdG1SFMbr4flMLQO2_2dOjIzRSOtV9xwi290/edit#slide=id.ga615f09411_1_72). In the first 3 months of 20XX our response rate has been solid:

<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")

    5. All this work let us tighten SLAs to 72 hours and still hit them, and we are very close to being able to tighten SLAs again and provide weekend coverage.
* Static scanner → mobile scanner transition: in 20XX [CTO] and [CEO] gave Engineering a mandate to transition off the Faro to a mobile scanner. We had no idea if this was possible based on the current technology so it was a huge risk for the company - and the #1 priority from the Founders. We transitioned successfully :)
    6. We undertook a very [hypothesis-driven](https://docs.google.com/document/d/1IInKsSQuU0MAJa7GL3xekafVqaFZvsxG0YjvS5hI_L0/edit#heading=h.epfryjs1bp1) and [data-driven approach](https://docs.google.com/document/d/1VR9F7nrMC0X7g6Hzer63yyaHjrjpGEN1QT0WQUIa6iw/edit#heading=h.gredc6pei2e2) to evaluate mobile scanners. This was the first-time at [COMPANY] that we picked hardware _not_ on a gut-feel. 
    7. Our [BLK2GO evaluation](https://docs.google.com/document/d/1JPKMozBX50OWixRQZu4X5SIx_ACFA16EIstiVnMS_rY/edit#heading=h.ju6ba58btjf6) found significant issues but was clearly the best bet at the time; we made the good decision not to roll out Kaarta. When rolled out to NHUB we found even more problems and pushed hard to do an [M6/VLX evaluation](https://docs.google.com/document/d/11l9BWpv0HsN_DtzbufLBD7ZkzaIcUMxBALPE-XQsD3E/edit#heading=h.qw7yi3o4dwr1) in time for the Facebook launch. 
    8. I personally made the decision to _not_ use the BLK2GO (or the Faro!) at Facebook - this is probably the single best decision I’ve made in the last year. The M6/VLX is a large reason why [COMPANY] is winning right now.
* Lower new customer onboarding time to 5 business days: at the beginning of 20XX it could take us _weeks_ to turn around the first scan for a new project. We officially set SLAs to hit 10 business days. Everything from getting the BIM model onboarded to getting scans registered and aligned was incredibly manual.
    9. We invested very heavily in Onboarding plugins inside the Navisworks interface. Now most of setting up a BIM model is done inside our environment and can be pushed to production in hours.
    10. Our investment in M6/VLX automation above made “first-scan” registration easy to hit in &lt;12 hours.
    11. Our investment in HALT (aligning straight to the model) made initial alignments without markers possible. This was an idea that I came up with in brainstorms with Anton.
    12. We lowered our onboarding time to 5 days and we are getting close to lowering it again to 3 days. 
    13. **We launched at Facebook, Microsoft, Genentech, Prologis, and other pilots successfully with no major (Engineering) fires! **
* Decrease COGS cost: at the end of 20XX 100ksqft took us about [REDACTED] hours to scan and about [REDACTED] hours to annotate (without quality!). We significantly reduced our costs to operate:
    14. Built a very comprehensive [COMPANY] Annotation Tool which takes care of managing most of the annotation overhead (copying point clouds, sending data to the next stage, etc). This has improved annotation speed [to about [REDACTED] hours/100ksqft](https://app.mode.com/doxel/reports/e629474382df) (almost 2x improvement). 
    15. With [Project Mysore](https://docs.google.com/document/d/1Rb19XTVghyfRbGfF4YzpdHEGm-VqD553wrF04fwPwQQ/edit#heading=h.269z62rdchn1) (Annotation Tool via API) we were able to expand annotation to India without as much formal training required. This reduced our costs per hour about 4x. I helped connect engineers (Annotation, D.I team), brainstorm the project, and ensure [milestone-based execution](https://docs.google.com/document/d/1Rb19XTVghyfRbGfF4YzpdHEGm-VqD553wrF04fwPwQQ/edit#heading=h.rc8tqjqyfw1e). We’re probably below $0.10/sqft in annotation cost for weekly progress scanning.
    16. With VLX rollout we’re able to scan about [XXksqft/hour ](https://doxel.slack.com/archives/C014FNFDU3G/p1617136739003300)or XXhrs/100ksqft with low-skilled labor. This is a 6-8x drop in human cost. The hardware is also somewhat cheaper then our previous generation so we’re probably saving 20-30% there. 
    17. With DxUploader + VLX we can now start supporting GC-based or 3rd-party based scanning. We successfully experimented with this at Facebook. That can take all the costs off our books. 
    18. Our R&D on vSLAM and 2D data capture is looking [very promising](https://docs.google.com/document/d/1Z0Vz9DWdPJdWYDjtiiUXMC62EmcODICHwVj3Xfgpj-E/edit). It’s likely in 6-9 months we’ll be able to roll out a ~50x improvement in DC hardware cost and it may lower our compute/storage costs as well (TBD).
* Launched new products: we built a Schedule Alpha product for FB and launched it to other pilots, then built [Schedule Beta](https://docs.google.com/document/d/1tPPLGzD2ljZFmunUPg5xjXmtE4jpeSSUlxBsFE9vSrU/edit#heading=h.802bpae2sys4) and started on [Schedule Gamma](https://docs.google.com/document/d/1yHBecqoPUmlRIQyhZsaInQp0jNRtTLImqJMC111n_yU/edit) until requirements changed. We re-built our Quality product to actually work through our tools/infrastructure and launched it at FB and other pilots. 
* Increase accuracy of [COMPANY]’s product: while we don’t actively sell “accuracy” as a feature our customers expect perfect accuracy and get frustrated when we don’t deliver that. At the beginning of 20XX we had a rudimentary understanding of construction sites and weren’t able to really track them at the right detail. We built the foundations in 20XX:
    19. Started measuring Annotation quality via a [Verification Mode](https://docs.google.com/document/d/1pn7LkqM8UEwSzIbp8rlqClbGlRmIe6fRwZjRhnrjU3c/edit). This helped us realize that Techture (annotating Shell) was a poor investment due to quality issues. It also helped us start tracking our Automation quality and realized it wasn’t good enough for launch. I drove the initial requirements for the Verification approach.
    20. We built [Stages of Construction](https://docs.google.com/document/d/1oQBtZtQ7QlZ9PmeHFIqOZ0ZAFHz-dXssWH7DpTffHOU/edit#heading=h.2ztjh7fg0qu) based off of [Matt’s PRD](https://docs.google.com/document/d/1KI03PsvRb9uP4URpjBeEYAW3N1wYKB7iQqH1fPlBtMI/edit). This allowed us to actually build a Schedule product and more granular EAC product since we’re able to track way more details of a construction project. Along with the Encyclopedia and Rules of Credit this is one of [COMPANY]’s big technological advantages over our competitors. 
    21. We integrated [2D data into our pipeline](https://docs.google.com/document/d/1KdN9XQ9i6VeuYy5G97d0FBpoajaeEZU2hhnbb8n8Bzk/edit#) to allow us to track more line items (e.g. electrical boxes, painting, etc). 
    22. Along with Matt I drove the Schedule Review process for FB launch to ensure our numbers were reasonable. This is now a [standard process](https://docs.google.com/spreadsheets/d/15aoiRCSOWQBP5hmTCXVzGMhzMUvfA2QdLOn23KMpizA/edit#gid=1624379865) and being turned into part of the product. 
* Ensure great engineering: a lot of investments here from testing, to our infrastructure launch on Azure, to our improved security story… 

**Impact**

Critical. At the beginning of the year [COMPANY]’s growth was limited by engineering. That is no longer the case.

**Areas for Improvement**



* We still have “gaps in ownership” that cause us to miss execution simply because no one is the clear owner & we haven’t built the systems to notify us that we are dropping the ball. Examples include the handoff of data from Data Capture Technicians → Data Capture Team (we had SLAs misses due to this) and ProdOps/Engineering handoffs on Schedule delivery (we missed delivery at FB for several weeks due to simple confusion).
* Annotation automation went very poorly. Lack of ML experience prevented me from making good decisions on resource allocations here and I was way too optimistic on what we could accomplish with the resources we had. In self-defense, I did warn in 20XX that I didn’t have this expertise and we would “learn as we go” -- I should have been clearer that we can’t commit to anything and maybe even pushed back on any ML work. But ML was sexy and I wanted to do it - probably ended up wasting $200K-$300K of company resources. I still run the risk that I’m not setting expectations correctly and that R&S expect significant automation improvements whereas I expect barely any progress.
* I haven’t been able to staff the Customer Insights team adequately in the last 6 months which has led to much slower automation/product execution than the business needs. Temporary patches (loaning engineers from other teams) hasn’t helped much. See below for the challenges in hiring that caused this miss. I also need to improve at making the case to [CTO] & [CEO] about lack of staffing causing negative business impact. 
* In 20XX Engineering teams have often been bottlenecked by lack of Product support. E.g. our Schedule forecasting is mostly useless and Facebook just ignores it; we didn’t have a good definition and built something simple (and wrong). I should have raised this issue more clearly, for example by offering to cut the engineering budget in order to fund Product headcount. 
* I don’t think I spend enough time educating [CTO] & [CEO] on all the work that Engineering is delivering and how we are solving critical business problems. That has led to the perception that “engineering is not on the critical path” when in fact EAC, Schedule, and Quality are all powered by engineering-built systems - although they do rely on human judgement in key places. 


## Head of Engineering: Team Building

**Responsibility/description**

The #2 responsibility of every manager is to increase their team’s capacity to win. This can be done by hiring, training, coaching, improving process, smoothing out relationships, etc. My responsibility in 20XX was to build a “team of leaders” that could help me scale the Engineering team to ~20 engineers.

**Your contribution**

(2 paragraphs, **include documentation/links)**



* Smoothed out the RIF effects: due to COVID the company decided to do a Reduction in Force. We cut our entire Frontend team (mostly staffed through Andela) and a couple of the more recent hires. While painful for all teammates it was the right company decision and I spent time with every individual on the team to reassure them and hear concerns. We continued to execute and didn’t lose any engineers. 
* Navigated the “remote-first” requirements of COVID. I set up a new All Hands structure to communicate across the company better, encouraged a much more written-first culture (which led to the great docs linked above), and took advantage of location agnostic hiring by finding talent in Boston, Michigan, Los Angeles - and helping engineers move to Colorado and South Korea. I did an across-the-org check-in and discovered that engineers preferred the remote-first culture so we committed to it.
* I made big bets on a few individuals to help scale the org:
    23. [EMPLOYEE]: I asked [EMPLOYEE] to take over the Customer Insights “team” (just him) at the beginner of the year after the RIF. I also had him start managing the Data Infrastructure team. This meant he had ~2 full-time jobs and was responsible for growing the India presence as well. He stepped up and executed on all the key priorities the company needed, including the Facebook launch (Schedule) and MSFT launch (Azure migration). 
    24. [EMPLOYEE]: After the Annotation team failed to gel and deliver on key projects (e.g. NHUB launch) I asked [EMPLOYEE] to transition from the Data Capture team and take it over. He debugged significant issues (beyond the scope of this doc) and got the team to execute much better. They launched Quality to Facebook on time, made significant improvements to annotation cost, and have more predictability with a [0.88 score on Q1 20XX OKRs](https://docs.google.com/spreadsheets/d/16imaHqU68tUX32W5RU-Op3_8YN6EbNlQx9hcX7oMTO8/edit#gid=2072677260)! I spend a lot of time with [EMPLOYEE] on everything from people management to making data-driven decisions to hiring.
    25. [EMPLOYEE]: he took over the Data Capture team when [EMPLOYEE] transitioned out and has led the effort to scale up smoothly. Per results above, the D.C. team is no longer the bottleneck in scaling up the company and that is largely due to [EMPLOYEE]’s leadership of the team. 
* Personally drove some key hires from initial conversations all the way through close and onboarding: 
    26. John and Alex have personally transformed [COMPANY]’s confidence in 2D data capture. 
    27. Agnes who is finally owning our most important product, Schedule.
    28. Sergey who is rebuilding our FE team.
    29. Will who finally gives [COMPANY] a knowledgeable ML individual.
    30. Erik who is repairing our hiring pipeline to execute on our ambitious hiring goals. 
* Drove hiring excellence: I have an end-to-end view of what an amazing hiring engine can look like and I’ve been implementing it step-by-step at [COMPANY].  
    31. Clean Lever pipeline from JDs to roles to funnel steps. We are getting close to publishing relevant data that will make our hiring another data-driven activity instead of intuition-based activity.
    32. [Training for hiring managers and interviewers](https://docs.google.com/presentation/d/1ZSyn4Ut41mT_zhi8Jacu8ElGDaHKnuEdyC6blh3Ghoo/edit?usp=drive_web&ouid=115234162360957637188). Spent many hours training hiring managers ([EMPLOYEE], [EMPLOYEE]), shadowing them, and providing feedback. Provided multiple training sessions for Engineers.
    33. Scorecards for key roles: [Quality PM](https://docs.google.com/document/d/1-Ty-cYEcWlQX6g4P-Up5TZLZmSmiMHnAgiaxpbUM2tE/edit), [FE PM](https://docs.google.com/document/d/1KOtooGEHfNESDwPzkolpblMEvx2Io0bBGqdHQWoCUm0/edit?usp=drive_web&ouid=115234162360957637188), FE TL
    34. [Cultural definition](https://github.com/[COMPANY]-AI/company_handbook/blob/main/career_ladder/global_ladder.md) and key TopGrading interview to ensure culture fit
    35. In-depth [Onboarding docs](https://drive.google.com/drive/u/0/folders/1uGpefxT83WigrngsT-_7rZRj_w1J9fjm) for every new hire and a “[COMPANY] 101” class that goes in-depth on all our teams and technology. I personally check-in with every Engineer in their first month and make sure their positive + negative feedback is sent to the whole organization.
    36. Effect: almost every candidate says we have a “unique interview” and are very attracted to [COMPANY].
* Performance management: raising the bar through clear expectations. I set expectations for [engineers](https://github.com/[COMPANY]-AI/company_handbook/blob/main/career_ladder/eng_ladder.md) and [engineering leaders](https://github.com/dobromirmontauk/engineering-scorecards) clearly. In 20XX I was a lot more diligent in holding people accountable to these expectations through 1:1 conversations, goal setting, etc. Details are out-of-scope for this document.  

**Impact**

Critical. We have a good team now with some established leaders and most of the cultural pieces needed to scale 2-4x. 

**Areas for Improvement**



* India hiring is going worse than I expected. I haven’t yet landed a single senior candidate and have lost quite a few. Based on some analysis it looks like a combination of not-quite-competitive salaries (and too much reliance on equity), lack of name-brand, lack of India entity, and a culture that does not emphasize externalities (e.g. titles). We’ve tweaked a bunch of things to see if it improves it but we’ll need to experiment for another 6-9 months before I can claim we are great here.
* Overloading [EMPLOYEE]: he’s had so much thrown at him that he’s often working 80+ hour weeks. Looking back, I could probably have detected this earlier and taken some things off his plate to help him focus on what was most important for the business. 
* Still not building “Product Teams” successfully. We’ve tried to build some “vertical teams” and put engineers on the mission (e.g. Sergy, [EMPLOYEE] on Schedule) but generally find that engineers don’t gravitate to the product mission naturally. I need to spend more time on evangelizing this approach and setting expectations with my org on what it means to be part of a Product Team.
* In 20XX I realized I had mis-hired several individuals; they were either more junior than I had thought or not quite the right fit for the role I put them in. I think I’ve improved in the 2nd half of the year, mainly by building a much bigger candidate pipeline and thus being less desperate.
* Spreading culture to other orgs. E.g. my hiring approach has not spread to Ops, Product, or Sales, largely because I haven’t had time to get buy-in and spread the culture. E.g. our [COMPANY] Virtues are probably not used by other departments which makes them more “Engineering Virtues” and not [COMPANY] Virtues. 
* I don’t manage-up proactively enough and help educate [CTO] & [CEO] on the intricacies of building engineering teams. This has historically led to differences in opinion on what our teams _should_ be accomplishing and what they _are_ accomplishing. I need to find better ways to communicate what I’m doing (and how long it will take) so the business can make educated decisions e.g. on staffing levels and ramp-up time.


## Project 4→N



* People Ops/Culture stuff
    * Comp ranges + model
    * 360 reviews
    * Hiring process
        * [Quality Product Manager: Interview Rubric & Scorecard](https://docs.google.com/document/d/1-Ty-cYEcWlQX6g4P-Up5TZLZmSmiMHnAgiaxpbUM2tE/edit) 
    * Hired recruiter + building the internal function
    * Owning All Hands + refactor → generally positive reviews
    * Leadership/Management courses
    * Holiday gifts + events
    * [COMPANY] Virtues
    * [COMPANY] Offsite planning
    * Bottleneck analysis for 20XX planning


# 


# Strengths



1. **Impact-driven, metrics-driven, data-driven.** I’m constantly trying to bring my team back to **impact to the customer **(internal or external) and find ways to measure the impact. As we move human workflows into tools (e.g. Annotation Tool) I push hard to get measurable numbers so we can track improvements. This approach has led to some good decisions, including switching from BLK2GO to M6/VLX, ending our contract with Techture, and discovering the ML pipeline test results were not matched in production. When reviewing projects, OKRs, and launches I go straight to the data and ask hard questions.  
2. **Written communication. **This matters even more in COVID times as we build an asynchronous, remote-first engineering culture. My writing is fast, clear, and thorough (this doc being an example). I encourage writing vs meetings in many aspects of my organization from sprints to standups to OKRs. 
3. **Betting on people.** I’ve gotten pretty good at spotting great talent externally and growing highly skilled people internally. I think I have pretty good skills in both coaching/mentoring/delegating and directing/training/evaluating. While sometimes I don’t have enough time to do the latter overall I’m better than most in managing individuals the way _they need_ to excel. 


# Areas for Improvement



1. **Trust → emotional outbursts**. I’m a high-context preference individual that trusts slowly and is suspicious of others’ talents. I was raised this way and have struggled to reach a “trust first” mentality, especially of superiors. This has led me to jump to inaccurate conclusions when I didn’t understand the motives or have all the data. Several episodes probably weakened my relationship with [CTO] & [CEO] and I need to show them I can handle ambiguous, high-stress situations. 
2. **Truly listening**. I have strong opinions, and I try to hold them weakly but either I do not actually succeed or I fail to show this to others since I’ve received feedback that I don’t truly listen. As the organization grows and we hire more specialized skills my opinion will likely be the least valuable in the room. I need to improve at showing others that their expertise is valued and that I’m OK being proven wrong.
3. **Educating up + sideways**. I frequently feel out-of-sync with [CTO] & [CEO] on “expectations vs reality” of the Engineering team. I haven’t yet found the right balance of implementing their feedback/questions to improve the team vs re-setting expectations on what is “normal” and “possible” in a given situation. 




# Company Virtues

_(For each of these virtues score yourself 1-5 and provide examples for that score. For a description of what each virtue means and how to score read the details [here](https://drive.google.com/file/d/13ePwnK7xCkYiespzzM5MxoaTLj_1cZuT/view?usp=sharing) (or Github [here](https://github.com/[COMPANY]-AI/company_handbook/blob/main/career_ladder/global_ladder.md)))_



* Ownership: 5. Similar to my review in 20XX; in 20XX I took even more ownership by helping the company outside of my domain (e.g. People Ops).
* Decisiveness: 4.5. I think I’ve improved since last year, in particular around performance management and key decisions. Not a 5 yet since I don’t think I’ve done a good job of educating my team how to help me make decisions _across the org_.
* Humble: 3.5. I’ve improved slightly in the last year by moving out of a Tech Lead role into a more Manager role, which makes it easier to share credit. 
* Empathy: 4. No change from last review.
* Intellectual Honesty: 4.5. Probably slipped a bit in the last year as sometimes I was probably too tough on people and hurt feelings unnecessarily.
