# 30 & 90 Day Objectives

This is an example of what we expect from you in the first 30 and 90 days. The objectives set out below are owned by you: if you feel they are not aggressive enough, or not even the right objectives, just let us know! I expect you to very quickly have an excellent judgment of what is important and the ownership to Rigorously Get Shit Done.

You are joining Doxel as our Product Frontend Engineering Manager. 

We’ve grown this team over the last year to have X engineers. Historically, Doxel has invested more in our internal tooling and Ground Truth Data Platform. We’ve delivered most of our insights to customers using our Customer Success team. 20XX has been about hiring out our Product, Design, and Product Engineering teams so we can shift from a CSM/ProdOps-led experience to a CSM/ProdOps-supported experience. Over 20XX we will want to shift entirely into a self-serve product: this will require us creating a beautiful, simple, yet powerful FE experience. That is your mission.

As the Product FE EM, you will need to take this relatively new team and all the different workstreams and turn them into a high-performing group. Some of the key problems you should try to solve:



1. Prioritization across many initiatives: the FE team is spread thin with many workstreams having 1 engineer or less. Some of our tech/products are understood by just a single person. You’ll need to work closely with Product to really understand the roadmap and thread it into the team that we have.
2. Heterogeneous infrastructure: our Product Eng codebases have evolved over time and may need a serious revisit. We have RoR, Python API, DB shared with the Ground Truth Data Platform team… This is likely causing productivity issues and will continue to get worse. However, balancing this work with all the product priorities doesn’t yield an obvious solution. Figure out what tech debt to pay off, when.
3. Poor FE quality: historically we haven’t invested in QA, testing, or monitoring. That means our FE has been slow with frequent customer-facing issues. We want to speed up development while also improving the quality of the experience. How do we do that?
4. Lack of a strong design language and information architecture: our FE has the feeling of ideas thrown against the wall rather than an end-to-end design. We’ve just hired our first Product Designers ( and ) which should help, and our PM team led by  are starting to think through the end-to-end flow. You should be a partner to them in this journey. 

For Doxel to win, our Product Engineering team needs to iterate very quickly on ideas coming from Product. You should be constantly looking for ways to #IncreasingCapacityToWin. Your partners-in-crime on this will be:



1. Joe: über-TL for the Product Eng team. Arun knows more about Doxel than anyone else here and built a lot of it himself. He’s the DRI for our Product Eng technical stack and engineering best practices. He’s new to the FE world so you two should partner closely so he can have a solid end-to-end perspective. 
2. Jack: EM for the Product BE team. Together, the two of you are responsible for all the engineers working in Product Eng. You should be peas-in-a-pod on resourcing projects, team processes, planning, sharing best practices, hiring, and mentoring/coaching engineers.
3. Jane: PM for the Product Core team. She is responsible for core features of the platform, from visualization to authentication to our data model. She’s the PM you will likely work the most closely with.

And your team: REDACTED. We will do 1:1 handoffs with each one so you get to meet them more personally. 

Because of the cross-functional nature of the role you will have multiple mentors:



1. A: he will be your primary mentor. Schedule daily sync-ups with him until you don’t need them anymore.
2. B: he’s been doing a lot of the work of the EM and is eager to hand it off to you. He knows the FE team end-to-end and will slowly transition responsibilities as you are ready for them.
3. C: he’s the longest-tenured FE engineer at Doxel and has built much of the stack as it is today. Work closely with him to understand the historical decisions and some of the options going forward.


# Day 1



1. Welcome to Doxel! 
    1. 8:30am: Schedule V-Team Team Meeting. Shadow this to see how this V-Team operates. Your report, REDACTED, is part of this team. 
    2. 9:00am: Product Core standup. Shadow this to see how this team operates. 
    3. 9:30am: Meet & Greet the Product FE team
    4. 10am: Eng Staff meeting. This is my weekly meeting to get a pulse on what is happening across Engineering.
    5. 11am: Review this onboarding doc with Dobromir. Discuss the first week. 
    6. 1pm PST: Meet & greet with REDACTED
    7. 2pm PST: Meet & greet with REDACTED
2. Go through the Doxel Onboarding Guide. Make sure you’re done with Logistics and have scheduled all the sessions in the first week.  will help you get scheduled. 
    8. Meetings Scheduled
3. Review our current Engineering Plan and start coming up with questions (especially terms/things you don’t understand). This is an old plan from the beginning of the year but reveals some thoughts on how we grow Doxel.
4. Watch the Introduction to Doxel Eng: Team, Culture, Process. 
5. Read everything in our Software Engineering Wiki.
    9. Please make improvements to it :) Organize things, clarify things, update/delete out-of-date information!
    10. Go through the recordings and list down the missing things.
6. Pick one code base and read through it. Recommendations:
    11. REDACTED: our Web FE. Probably a good place to start :) 
    12. REDACTED: our legacy RoR app, which still hosts a ton of functionality.
    13. REDACTED: where the majority of Product Backend work happens now. 
7. Dev Setup environment instructions REDACTED. 
8. Schedule 1:1s with  (Product Core PM),  (Schedule PM), (Budget PM),  (Product Designer) Tuesday/Wednesday. Get a brain dump of what they need from the FE team in the next 90 days.


# Week 1: Get Familiar with Doxel



1. Handoffs with all of your reports
    1. Schedule a 1:1 with each of your reports for an initial meet & greet. Start building a sense of what skills & interests your team has.
    2. Schedule a 2:1 30 min with me, you, and each report near the end of the week/2nd week to discuss the handoff. We’ll review their last performance review + next set of growth areas.
2. Go through all the Onboarding Sessions set up by REDACTED. 
    3. Watch historical videos as much as possible.
    4. Deep dive into annotation tooling, Operations processes as much as possible since your team supports this.
3. 2pm daily: Debrief with Dobromir on the day + what is coming next. 
    5. Come with questions, anything goes!


# Week 2: Deep Dive



1. Finish any Onboarding sessions not covered in the 1st week.
2. Pick 2-3 of these topics to dive in deep, based on what you learned in Week 1. Use your judgement (run it by me if you’d like). The rest you can cover in 90 days:
    1. Ruby-on-Rails history with REDACTED. What is the long-term plan with this system? I’ll want you to have opinions + a roadmap on what to do here in the first 90 days.
    2. Forge vs NavisWorks tool development: deep dive with REDACTED and REDACTED. What are the pros/cons of each technical stack? I’ll want you to have technical/business opinions on the transition in the first 90 days.
    3. Three.js Model/Panorama Viewer: deep dive with REDACTED about what they built here. Learn enough so you can t-shirt size for Q4 planning (or rely on your team) as we decide what to invest in.
        1. Figure out if we have Computer Graphics gaps on the team. Should we hire, like REDACTED is thinking? Or should we train people internally?
    4. Ground Truth Data Platform API vs Product Eng API: deep dive with REDACTED. We have tight coupling at the database layer today; how do we decompose our systems so that each team can iterate independently?
    5. Design system for Doxel with our Designer: work with REDACTED on the current state of our Design System (hint: not much) and how to roll out a real one.
    6. Talk to REDACTED about our external website. Who owns it, how he wants to migrate it, etc. Should our team contribute here somehow?
    7. Competitor analysis: work with REDACTED and other PMs on what our competitor web experience looks like. Understand it deeply so that we know where we should match them and where we can beat them. Come up with a roadmap to out-execute them.
3. Set up weekly 1:1s with all your team members and key partners.
4. Set up a “how do we run Product Engineering?” discussion with REDACTED.
5. 2pm daily: Debrief with Dobromir on the day + what is coming next.
    8. Start coming with deeper questions and/or opinions.
6. Set up 1:1s (if you haven’t yet) with:
    9. REDACTED 


# Week 3-4: Start Driving



1. Pick 1-2 of the topics above to start driving. Run them by REDACTED first.
2. OKR planning for Q4: We will be kicking off OKR planning in the first 2 weeks you are here. You should attend all the sessions and work closely with  to do the planning; likely you won’t be ready to own it yet. However, you will be committing your team to delivery. Figure out how to do that :)
3. Take over the Product Core Sprint process from  
    1. Re-organize JIRA to be easier to use
    2. Start working with  on user stories, Eng tickets, etc.
    3. Help REDACTED free up as much time as possible for development going forward.
4. Figure out oncall process across Product Engineering (FE + BE) with .
    4. Our Oncall process for Product Engineering isn’t clear today. A lot of work is understood by one engineer only, which makes it hard for us to “own” things across the FE/BE teams. Work with  to cross-train engineers and figure out the right solution here. 
5. Weekly 1:1 with Dobromir
    5. You drive the agenda. You should have 30-45 minutes of content/questions. 
6. Schedule 1:1s (might be the first 2 months) with:
    6. REDACTED


# 30 days



1. Write up a 4-week summary of Doxel engineering (technical and non-technical). Email it to REDACTED and for comments.
    1. #Rigor: What are we doing well? What should we improve?
    2. #GSD: sign up for one thing to improve in the next 90 days


# 90 days



1. Have opinions on all the things called out above :)
2. Create a customer-centric culture
    1. Help motivate FE engineers by giving more access to how their products are used by customers.
3. Have a FE product/technology roadmap (~2-4 quarters)
    2. Work with REDACTED to have a unified Product Eng architecture, based on knowing what REDACTED and his team wants to build. Make sure this is well-supported by and the GTDP team.


# Appendix

You might find it useful to read the previous 30-day onboarding docs stored here: REDACTED