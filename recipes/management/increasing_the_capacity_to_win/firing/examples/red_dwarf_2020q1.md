# Summary

Red Dwarf is** sometimes missing expectations** at Doxel. He is a hard engineer to write a Manager Review for because of the large variability in his performance at the company. Red Dwarf is a technically sharp engineer who possesses deep knowledge of CV. He has a research bent of mind which has emerged as a strength - as well a weakness. When he is allowed to focus on just a few meaty research/R&D related items (which often he feels the need to decide by himself), he does well - he has literally Saved Our Butts numerous times. But when asked to do R&D on other items or help the broader engineering team on some production code related items, his enthusiasm wanes and his contributions are slow and below-par. This has hurt broader Engineering team goals multiple times and affected the spirit of camaraderie. Red Dwarf needs to think deeper on how he can fit better within a startup which needs to solve many technical problems versus just R&D with his own assessment on 'fit' helping decide next steps.

He’s been given feedback by his peers and by me many times on numerous issues. Most of the material in this Manager Review should not be a surprise, although this may be the first time he’ll be reviewing such a concentrated collection. This leads me to worry, as his manager, that Red Dwarf has a huge blindspot when it comes to self-improvement. **He dismisses feedback with a smile, or a witticism, or a logical counter argument** **instead of listening soberly and changing his behaviors seriously. **I’ve personally witnessed this when giving him feedback on throwing balls in the office and others have told me they stopped giving him feedback altogether since he wasn’t listening.

I’m sure there are environments in which a friendly, independent, deep thinker like Red Dwarf can be incredibly successful. Unfortunately for us and him, a startup environment does not mesh well with his preferred work approach. If Red Dwarf was eager to learn the skills necessary to be **a star team player** at a startup I would bet on him and invest in the transition - he could do it in 6 months. Based on his existing approach to feedback, I’m not sure he’s interested in learning those skills at this point in his career. 

Red Dwarf’s needs to make a big decision in his career: can he value teamwork and team goals over his own personal interests. If he’s able to put his Doxel family ahead of the hard problems he wants to pursue he could have a lot more impact over the next six months - and maybe actually solve even more hard problems! If he prioritizes the hard problems instead, his fellow engineers will likely isolate him and his contributions to Doxel will falter.

# Strengths


## Domain Expertise

Red Dwarf is our strongest traditional computer vision researcher/engineer at the company. His knowledge has helped us build a robust alignment system and a promising error detection system (which was paused due to lack of engineering time). He should share his expertise more broadly to train the next generation of CV engineers at Doxel.

Peer Feedback:



* He is good with the open-ended research problems! He will find you a solution. He won’t try to cut corners. Red Dwarf has really good fundamentals. His experience is vastly better than XXX. Top 20% of the industry, maybe top 15%.
* Domain experience is quite high. Good abilities to learn newer things. Neural nets - he has self-taught himself quite a bit in this domain. When he joined Doxel he barely knew about it about DL, now on quality of conversations it’s much better. 
* Technically he is smart & strong in his own domain. His feedback, if I have a thought, resonates with me. It helps me strengthen my ideas or to nullify them. As an example, even when talking about the registration engine, I was thinking of a different flow and he talked through the flow he was proposing and he was able to convince me with some of the details he had in mind. E.g. flattening the floors first and then XY-based global registration.
* In terms of technology, Red Dwarf is more aware than XXX. He’s spending time on conferences, talking to people, etc. He’s aware of strengths/weaknesses of different methods.
    * One thing disappoints me: I don’t see any of that reflected in any of the work. He’s not proposing projects based on stuff he learned. Excitement is missing. We are having meetup about the conference 3 months later! In my previous job we would talk about conference right away and implemented shortly after.

Alternate opinion:



* “He’s very good but he thinks he’s perfect.” What limits people is not what they know they don’t don’t know - it’s what they think they know, but don’t, and that limits them.


## Good Naturedness

Red Dwarf is one of the nicest, most caring people at the company. He sets a great “we are a family” tone at Doxel (most of the time - see some comments later). 



* He understands people’s limitations, wants to pick them up. When we were working together on a project he finished his work and stayed late (1am!) slept on the couch to see if I would need help on the work I was doing. When you talk to him, the conversations he asks about other people makes the opposite person realize he cares about them. He sets a good vibe for Doxel.
* Really fun person. Having him in a meeting elevates the energy in a room. That helps boring meetings or discussions - that’s very nice of him. A lot of people don’t do that.
* In tough situations he helps us out. He’s a nice person as a whole.


# Areas for Improvement


## Ownership

Red Dwarf doesn’t display the type of ownership we need at a startup. He focuses very narrowly on what _he thinks_ he should own (usually either what he wrote, or the hardest problem) and not what we actually need him to own. There are many examples of this:



* He never learned how Airflow or Python wrappers worked which forced other engineers to spend time to make ARX function in production.
* He never understood the entire pipeline and when Operations time was being sunk and customers were getting deliverables. That leads him to write things like “realignment greatly improved accuracy” which is generally not true; we used it a few times but because it runs last it generally didn’t provide any value (yet).
* While Alignment would frequently fail due to Registration issues, instead of stepping up and finding solutions (or helping build tools to determine if Alignment or Registration were at-fault), Red Dwarf would push-back and ask others to figure things out.
* He pushed back against training our Operations team on using markers; he only wanted to talk to Eric about it. He logically tries to argue his way out instead of answering the question: “how can I help ensure that the project is successful and my work provides value to Doxel?” 

Over the next quarter Red Dwarf needs to display better ownership by getting his projects from “works on his computer” to “works in production reliably for a month”. While this may not tie well into his personal interests we are still too small a company for him to focus purely on research and let others complete his projects. 

Peer Feedback:



* He did not demonstrate ownership - going beyond his area to fix the whole problem. Even when markers did start getting stable, he didn’t push the conversation into “how do we fix registration”.
* I don’t think he takes ownership seriously. I had a discussion with him; we had so many problems in Airflow, for him OWNERSHIP means to get things done on the tactical level. Red Dwarf doesn’t think beyond the narrow vision; he thinks only about fixing the bug. Ownership is supposed to be broad. Timeliness: when you commit to something, if you don’t make it, he’s fine with it. He doesn’t keep people accountable. He doesn’t think missing a deadline is a big deal
* He likes his ways and he sandboxes himself. He doesn’t want to own things end-to-end. Other people put it in Airflow, with Asal he was sending her the things he didn’t like - that is not ownership. I heard that from her - that fits into the same pattern. Sure, you can delegate, but… that’s not what was happening.
* When he owns something he’s a 5. Once he takes ownership. It depends if he wants to do it. If you include the things he doesn’t want to do - 3.5, 4? **If he doesn’t want to, I’ve seen where he battles his way to get out of that ownership, to explain why he shouldn’t do it. If he really doesn’t want to do it, it won’t happen.**
* **He doesn’t own things end-to-end. He’s doing stuff on his computer, he wants us to do things his way** - “this is what I have installed on my computer, so we should have it in the Docker image.” He has that version on his machine and maybe it doesn’t work with another. 
* Overall, his ideas about wall markers - arx is technically strong. Hard to implement in the real world.
* His ideas are technically heavy, process heavy. In practice things might be very difficult to do. Working on EDEM: he was working for aesthetic part of it over functional part of it. The discussion with the Ops team was not leading anywhere, hitting roadblocks with making practical progress.
* First I was distant, I didn’t understand his communication skills. They are on the low end. I think it’s a language barrier. Prime example is communicating how to lay out floor markers, wall markers. He wanted to explain to someone in-house and have them explain to the field. To use in-house as interpreters. **When requested, for documentation, pictures, better understanding of what he was requiring - he pushed back. That caused more frustration for folks trying to translate for him.** Why did I not see that in the documentation? I don’t know. **Maybe he doesn’t want that responsibility?**
* When you challenge Red Dwarf that alignment is bad he asks you questions that get to the answer. If he thinks its alignment he’ll get the most information what could be the problem and solves it. But it’s only when he thinks alignment is the issue. **If he thinks registration is the issue he doesn’t dive into it. He goes thinks about something else.** He’s like a doctor: you can pretend you have symptoms, they’ll give you antibiotics. **You have to know what to say Red Dwarf to have him hop on it, then he’ll dig into it.**


## Collaboration & Leadership

For someone as friendly as Red Dwarf it is somewhat surprising to see that he works poorly with team mates. I think the root cause comes from his desire to work on hard problems; a great senior engineer and team leader gives the most interesting, hardest problems to others and does the “grungy” work other folks don’t really want to do. This is leading by example and causes a team to gel and have everyone share the burden. 

Instead, Red Dwarf tries to shed the uninteresting work so he can focus on the hard stuff. This has led others to shy away from working with him since they have an intuition they will be taken advantage of instead of trained and empowered. This has more negative downstream consequences: siloing, where Red Dwarf isn’t paying attention to work happening around him and other engineers don’t review his code and solutions. 

The situation is especially glaring with Bogdan, our other senior computer vision engineer. Bogdan and Red Dwarf have two very different approaches and, if they worked well together, they’d be incredibly strong at compromising between short-term 80% solutions and long-term 99% solutions. However, I’ve rarely seen them collaborate, ask each other for help, bounce ideas off each other…

For Red Dwarf to exceed expectations in the next quarter he needs to take team membership seriously and put the goals of the team above his own personal interests.

Peer Feedback:



* What motivates him is a hard problem.** Hard researchy problems, where he can be the sole developer, get all the credit. Hard to get him to work on a team, hard for him to look at things beyond what he wants to do.**
* Unless he is convinced something will work out - he won’t execute. **It has to be his idea.** If it’s somebody else’s idea - he won’t execute.
* **I don’t think he’s able to decide for himself that he needs help. **This ties back to him not working well with teams.
* Given a senior person on the team - we’d expect him to figure out how to split the work, parallelize the work. The way he assigns: it cannot be parallelized. Everything is dependent on him. He’s not very good at splitting it.
* His estimates are not something he’s gotten right. He over-promises or underpromises, even on things that are pure engineering and not experimentation. On initial projects I thought he was under-promising. But then I noticed he overpromises as well. He’s just not good at predicting. Fear factors - where the project will fail or slow down - he actually can think about it. He knows where the assumptions are, where they might not work. But he doesn’t bake this into his judgement of time or schedule. 
* He has a very strong personality. Gets into conflict easily - he has a humorous side of it but I’ve seen him take things very personally. E.g. things spoken to the team he might think are being spoken at him. E.g. Matching/Cropping was not working properly for Airflow, Red Dwarf  +Bogdan were supposed to figure out APIs. But putting them together they weren’t working; I mentioned in Slack channel and Red Dwarf took it very personally.
* I don’t think [Bogdan and Red Dwarf] gel well - they have complementary virtues.** If they worked together they would be really, really strong. **They don’t work very closely at all. They each open up individually, but not together. They have a tendency to refute each other almost immediately without understanding the proposal from the other person. They are the most senior people we have and that’s a huge concern.
* Playfulness can be distracting.** He was messing with me in a meeting - he was messing with XXX by throwing the ball at him.** XXX was good at not letting that stuff bother him but you can see it bothered him, it added up. Stuff like that can bother people, take away from their productivity.
* He thinks he’s humble but he’s not humble. He never asks for 2nd opinion. Not in-your-face arrogance, “I’m better than you”, but his view of the world is how smart he is. **He doesn’t feel the need to ask a 2nd opinion.** When he starts to do something he doesn’t ask. He never asked about how to do matching - and he will never ask. Unless someone tells him. **Because he doesn’t realize that he might not know best.** That he might need some help. Einstein was wrong - 30 year argument with Bohr about quantum physics - and Einstein was wrong. Nobody is always right.
* **He can look insensitive: when he was playing tennis and Brody was working late at night, and Red Dwarf was insisting for him to play tennis, that looked weird. Not just me - other people realized that.** He was throwing balls at XXX. This is childless. He was teaching new hires to throw balls at XXX - this is childish. Not good behavior - even for a child! You would tell a child not to do that. Bueno resisted but other people threw balls at XXX because Red Dwarf insisted. That’s not nice. I don’t know why he doesn’t realize this. He’s not mean. 


## Decisiveness

A decisive engineer is one who is hungry for impact and can quickly unblock themselves in their quest to move the company forward. They know when to balance taking short-cuts or absorbing technical debt and when to invest in the long term. Red Dwarf has a long way to go here, again largely due to his interest in solving hard problems first and foremost.

Occasionally, Red Dwarf will shine when he is given “guidance to stay in balance, to focus on the real problems, problems that can be solved in a short time frame.” Otherwise he doesn’t think about the big picture and make the best decisions. E.g. in the current registration project I was surprised to hear that he’s focusing on deep learning features for global registration and needed another 2-4 weeks to see if the approach works. We are in the process of rolling out Ouster sensors (which he is aware of) and expect much better SLAM even with Cartographer (which he should be aware of), which means the most “bang-for-the-buck” would be to get a fine-grained registration engine up & running first so we can automate 50-80% of registrations. Global registration should come after that; I’m assuming Red Dwarf focused on it first since it seemed like a more interesting problem. 

Another example is discussion about how much data we need to capture per hour. He’s brought up multiple times “why don’t we just run more Rovers?” and I’ve had to sternly explain both the why and that that type of question is not productive. It both sets a bad example for the team and sends a strong signal that he doesn’t understand the constraints of the business or use them to prioritize his own work.

I highly urge that Red Dwarf regularly thinks about the big picture and has conversations with me and his peers about the biggest problems so his work is focused and he can make the right tradeoffs day-to-day. 

Peer Feedback:



* He needs to change his focus from technology → product. 
* He is an engineer’s engineer. He just wants to work on the hard projects. **He’s thinking about the curtains when the roof is leaking.** He is not thinking about the hardest problem overall for Doxel. He also becomes pedantic about the approach he wants to solve. E.g. the quality tool - instead of understanding how much value it provides the company he really pushed beyond the reasonable energy to convince him otherwise.
* For him to do his work - it’s slow, it takes time. The results are at-par with what you would expect from someone in the space, with a strong solution.
* I think he’s happy to solve difficult problems even if it doesn’t have to be difficult. He loves problems more than solutions. **He likes puzzles.** 
* **He was opposed to krx - not enthusiastic Red Dwarf - my guess is because it was too simple. We should have tried krx a long time ago.** It’s not like Kevin was an expert in the field. Red Dwarf could have thought of it, why not try that first? Red Dwarf doesn’t want to try simple things that can give results, then come up with something better. He wants to do whatever can be **best**. If it takes 6 months or a year - he’s fine.
* **He needs guidance to stay in balance, to focus on the real problems, problems that can be solved in a short time frame.** Help him focus on solutions that might be mundane - results in a timely manner - more than beautiful solutions later. We are a startup, **I don’t think he realizes that.** 
* He has a bias for technology. He wants to solve problems, not build a product. This is something he lacks.