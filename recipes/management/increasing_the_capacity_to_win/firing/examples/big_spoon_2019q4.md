# Summary

REDACTED has impressed me these last six months with his wisdom married to his practicality. More than any other engineer at [COMPANY] he is able to propose simple, elegant computer vision solutions that are likely to do 90% of what we need. He also sees team and company issues before most other employees and has helped me make decisions on what to build and how to build it.

While REDACTED’s mind is a sharp weapon it is often blunted by his introverted personality. He shines in 1:1 conversations while retreating into a shell in group discussions and in disagreements. While he’s an excellent mentor, he prefers to work alone and hasn’t done enough projects closely with other senior engineers (REDACTED, REDACTED, REDACTED, REDACTED…) to have a multiplicative effect. He also hasn’t taken full end-to-end ownership of his area of responsibility, Annotation, which has led to some glass balls being dropped (e.g. database integration & updates). 

This makes it hard to rely on him as a Tech Lead who can represent and distribute work across a group of engineers. REDACTED has mentioned that he has trouble working in a high-interrupt environment so perhaps the role is not the right fit and we should explore more of an IC position moving forward. We’ll discuss this in the upcoming month.

Overall, he Meets Expectations for a Senior Engineer now and could quickly Exceed Expectations if he modified some of his behaviors and habits. I’m excited to work with REDACTED on these improvements in 2020!


# Strengths


## Practical CV Knowledge

REDACTED has proposed, and implemented (himself or with his team) our current LabelBox Annotation approach, a high-potential Alignment verification tool (Top Down XRay View), and a simple model system which looks like it will hit >50% recall at 95%+ precision. He marries a solid understanding of CV tools with a product-based mindset that encourages quick solutions that are “good enough”. 

Peer feedback:



* Worked very closely in many situations. He has lots of good ideas - I like them, they are different than what I was thinking. He sees things in a different way than I do. Brings practical, implementable solutions, that really work on current problems.
* Delivered quite a few things, e.g. the annotation tool. He’s doing really well on the CV side of things.
* Real combination I’ve seen - most CV folks are not interested in the product side, help deliver the whole product not just the CV. It’s really good that he’s trying out more, learning new things. The only thing is more interest, more exploration of the details would be good, how to productionize things would be good. 
* He has initiative. He proactively proposes solutions, don’t need to ask him - e.g. introducing OpenVDB or annotation by images rather than point clouds. 
* He has no problem with trying new things. He’s very good at that. No ego - “I don’t know it, I’ll go figure it out.”
* Good software engineer, learned a lot about C++ - CMake, Docker, etc. Good at traditional CV, OpenVDB, libraries, etc. Used some of his functions fo reading OBJ files, sampling surfaces of the models, etc. Leveraged his code. 
* Good technical knowledge of CS. REDACTED might be slightly stronger than …. Historically REDACTED was more about OpenVDB, subtracting data, etc.
* He knows quite a bit about 3D CV which was a new domain for me. Without him I wouldn’t really understand what we are doing. He can propose the most useful ideas - e.g. LabelBox, he contributed the most to the overall pipeline. 


## Mentorship

Several people have been relying on REDACTED as a mentor and they rave about him. He’s probably our strongest mentor at the company; however, he needs to have someone close to him (physically + org-wise) to really invest him, probably due to his introverted personality.

Peer feedback says it best:



* He’s a very good mentor. He has this good quality - he’s straightforward, very knowledgeable - and will tell you when he doesn’t know something. He’ll admit when he doesn’t know instead of giving me a skewed answer - I’ve experienced that elsewhere. He’s not afraid to learn from other engineers.
* Really like his personality - enjoyable to work with. Especially important when you are stressed out. The entire corner is so nice; we are stuck next to each other and when we have to work - everyone is pleasant. 
* He’s very good at mentoring. What I like about him is that he breaks things down. Tries to do it simpler and then builds upon it. I find it most of the time useful. But sometimes it’s a bit too much - would be better to do it right because changing it later is harder. 
* I like his ideas. He helps me a lot when I get stuck. When he knows something he tells you, when he doesn’t - he says he doesn’t. He has no ego, he doesn’t manipulate. He’s straightforward, I like that about him. Takes the time to explain things.
* He’s a great mentor. He’s always happy to teach new skills he just discovered. I learned many things like Docker, CI/CD, pipeline design. He gives me a lot of advice which has helped me a lot. He’s a pioneer of many projects. When I joined the company we had just started to use Docker and CI and he did most of the rules, best practices there. 
* REDACTED is wise, he should share his wisdom. He should change his routine - maybe different desks? He needs to get uncomfortable with change. 


# Areas for Improvement


## End-to-End Ownership

While REDACTED is a solid owner of pieces that he has built himself he struggled in taking ownership over the entire Annotation subteam. We had to push him a lot to look into DXQS, data importing, and how the database worked; he seemed to mostly stay in his comfort areas instead of proactively trying to understand the whole pipeline. He also has rarely contributed to Pull Requests reviews in cross-cutting pieces (e.g. schema reviews), which prevent him from catching issues earlier that will affect Annotation.

There were several surprises, e.g. KD data not being updated in the database, and the schema not being friendly to ML, that REDACTED should have caught himself. By paying better attention he would reduce the work on his plate/his team’s plate and increase his impact at the same time.

Peer Feedback:



* His nature: he doesn’t leave his scope sometimes. He sets a perimeter for himself and he doesn’t go out of it. E.g. annotation CSV update on DB - we had that discussion for the last 2 months but it took him that long to start working on it.
* REDACTED is comfortable with the things he knows. When its within his domain expertise. When the variables start increasing… he gets nervous. He starts shutting down. He crawls back to his shell, his domain. You need to give him one thing at a time. Example: with the CSV - I noticed with the date conversation, I’ve had calls with him REDACTED, Justin, REDACTED - we’ve had walk throughs - we agree on things, but then he falls back to the process he’s used to. The one he’s established. I don’t see him trying to start PGAdmin, see how it works… We end up having the same conversation. He keeps using “dxqs” - which is great, but not the tool he should be using.
* Mixed feelings. In many cases he’s been great in ownership. Example that bothers me: Airflow wasn’t set up right on pager duty originally; a couple of times he came to me complaining about query_targets. “Not my responsibility” - I hated that phrase. When he was building top-down image, but if any problem assignment should be to us (me + [EMPLOYEE]). I said “I go outside my responsibility”, we all need to do that. 
* Most of the code was written in PoC way; patched many times; not really ready for larger scale. REDACTED, along with his ideas, should start thinking about production, how it will run, how it will scale, resource consumption.
* CV knowledge, if combined with product knowledge, would be really good for him and for the company.
* He’s figuring out the things he knows but he isn’t really learning more things about Python, etc. He explores the things to solve his purpose but he could have done a little bit more. That would help him guide and mentor his folks more. Areas outside his expertise 3-4, not very high.
* Is there a risk that annotation team won’t keep up with what other teams are doing? Yes… that’s the risk. He needs to understand that [COMPANY] will be changing quickly, the solution right now is not set in stone, and he as the leader needs to show his team that change is great and the importance of it. They will only listen to his actions, not his words, so they will do what they see him doing. He needs to light the torch.
* When there is a vacuum I have the tendency to go fix things. But I don’t see him have that quality. He lets things drop. He just says that “he doesn’t know”. He complained that he didn’t need to know DB, I explained it was just a tool like k8s.


## Leadership

REDACTED needs to make numerous small improvements in his leadership skill-set to truly have the impact of a senior engineer. They broadly fall into three categories:



* Intellectual honesty: REDACTED needs to express his disagreements more clearly, especially in group meetings. On several occasions he was right (e.g. being too early to annotate with a remote team) but didn’t push his opinion enough to be listened to. This makes him uncomfortable and the organization misses out on his insights.
* Delegating & leveraging others: REDACTED doesn’t think in terms of setting larger goals and splitting up work between people (peers, or team members) to hit the goal as fast as possible. He tends to throw projects over the wall to someone else and not pay attention to the details, e.g. with Ebot’s DataFlow work or Sofya’s ML project. This means he isn’t as effective at course-correcting the work as it happens, which makes him more weary of depending on others and decreases his ability to have impact via leadership.

Peer Feedback:



* In few occasions he’ll take decisions that are not good for him. E.g. Python wrapper - he should have let REDACTED do his part and he just volunteered. I asked why - he said “REDACTED will do it in a week” but then REDACTED broke stuff up because he wasn’t familiar with it.
* Floor of knowledge - he developed the annotation tool but most people don’t know what happens there. He produces results but if anyone else wants to help - they can’t. REDACTED needs to do it.
* If they [REDACTED and REDACTED] gel well - and I don’t think they gel well - they have complementary virtues. If they worked together they would be really, really strong
* Sometimes he has good ideas but it’s malleable too. Too easy to convince him sometimes. He’s not really sure about the best way.
* He does not speak up in meetings sometimes. He’ll tell you he disagrees 1:1, and then he’ll agree in a debate.
* He doesn’t understand the power of multiplication, deliver more things with the help of other people. Making people aware of all the things that are happening, the brilliant ideas that he has. He may not have time for all of it, maybe he could start the basic ones and then marshalling other resources to help him out. 
* Intellectual Honesty: he wrote this in his review and I agree with him. Most of his answers are in the “maybe” side, not clearly “yes” or “no”. No is hard for him. He hesitates, doesn’t feel comfortable disagree. He needs to be more comfortable voicing his opinions. He needs to say it and defend it.
* More transparency towards me and other engineers about how to use the database. Don’t just talk to the senior engineers. I wasn’t aware of what was going on. He needs to relay the information more. I don’t know if he knows it well enough to be helpful. He would either say “the database is not ready”.
* Planning needs to be better. Having these small sprints really helps - otherwise it would be a huge mess. We don’t need to do too much planning. But even within these small sprints it would be good to reiterate “where did we fail?” last sprint and “what’s the plan?” for next sprint. Have a better structure in the meetings. We also don’t want to have too long of a meeting. 
* Ask “what’s blocking you” at every standup so we can take care of it immediately.
* AFI: his personality is a bit on the closed side. Reserved, introvert. Sometimes its hard to see what he really feels. 
* I like him a lot, one of the reasons I don’t know him is I feel he’s uncomfortable around me. Not quite sure why - I think it’s getting better over time. Felt like he’s more formal than he normally would be.
* Should have socialized the top-down view stuff with Annotation team more. Get more of a buy-in and feedback loop. It didn’t feel like it was being effective. Maybe it was hard with Kevin, so it’s hard to say what REDACTED could do differently. 
* He doesn’t communicate well remotely. If he’s WFH or I’m WFH - he has problems with that. It’s just hard to get a hold of him. I know he’s busy - when he’s here I can grab him for a couple of minutes. When he’s not here it’s harder.
* He’s the guy in the room that you always have to ask for his opinion - and then you wonder why he didn’t say anything before! Maybe as a single dev he was OK doing his own thing, but he makes such a great impact with his ideas and what he accomplishes that if he thinks his circle of impact to the other things he can do - he can have a much greater impact.
* He should have a rule of thumb - if there is even one single other person who can do what he is doing - he shouldn’t do it. He should only do the things that he can do. When he comes up with an idea and wants to implement it - before he types any code he should think “can I explain this to someone else and have them implement it?” That’s the lowest hanging fruit, he should delegate the things he can easily delegate. 


## Execution

This is somewhat tied to the two items above and those should be considered higher-priority because they will positively impact his ability to execute. 

Peer feedback:



* He commits to too many things. He’ll say “yes” and that he’ll do it but he gets busy with other things. So many people need his attention, a lot of people are asking for help. Better planning, what you can do, in what amount of time. We are all guilty of that. Very important skill to have - maybe give yourself extra time. You need to account for it. 
* Big problem with Annotation In-House is we don’t have time to step back and figure out what we can do better. It’s not really on them - they get hyperfocused on solving a particular blocker, but it becomes less of a problem. There might be other immediate problems. So maybe checking-in to see what’s a blocker.
* Might have been better if there was more training on how to use the Top Down view. I tried it, hard to zoom in, hard to pan - not sure if there is a specific way to use it - easier for me to use NW.
* I think he’s a better experimenter than executor. He’s good at doing pioneering things - from what I saw in his code, it’s not very maintainable. But he’s very good at experimenting with new ideas. This cannot be replaced. He’s in between a developer and a researcher - a bit like a research engineer.