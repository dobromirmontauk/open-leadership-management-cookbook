# 2024 QA Lead Interview Handbook

# Role Expectations

* [Job description](https://jobs.lever.co/mashgin/426fbe85-f581-4180-8387-5d63d53d7610)  
* Job scorecard: [QA Lead Scorecard](https://docs.google.com/document/d/1XYbzE4-dL-6uIv-qYboUmB-cLIlXUF4GxXVAQ_daJXo/edit)

# Interviewer Guidance

1. **Attract**: the candidate is interviewing us as much as we are interviewing them. Make them feel comfortable and want to work with you\! Show your excitement for the job \+ the company \+ the product. *If you cannot do this – tell me. You should NOT be on the interview panel until you can\!\!*  
2. **Avoid Voodoo Hiring**: we have specific criteria we are looking for that we believe will make someone successful here. Don’t hire them because “I like them.” Make sure you are familiar with the criteria, and that you know how to look for evidence they can/cannot do the job. *You will be required to score them on the scorecard\!\!*  
3. **Have Conviction**: two thumbs up, OR two thumbs down\! If you are NOT SURE when you get out of the interview, you failed. Don’t be afraid to interrupt and keep digging until you have evidence that they can do the job.  
4. **Interrupt & move the conversation forward**. The goal of the interview is to learn things; if you are not learning anything (e.g. they already showed they are awesome, you don’t need more info, or they are being vague and you aren’t learning anything) → redirect them with a different question. You shouldn’t send more than 30 seconds on a topic where you are NOT learning anything.   
5. 

How? Every interview should follow this pattern:

1. Warmup: 5-10 minutes. Introduce yourself. What have you accomplished in your career? Why are you at Mashgin? Ask them similar questions.   
2. Main interview. Usually split to 2 equal parts so we can get 2 different angles on the candidate.  
3. Closure: answer their questions. Give them space for this – even if they aren’t sure, prompt them\! The questions a candidate asks is an AMAZING insight into how they are thinking about us, what doubts they have, etc.   
   1. **NO QUESTIONS is a red flag**. You can even tell them that: “we really value curious, engaged individuals at Mashgin. Are you sure you don’t have any questions about our company, product, or team?” 

# Interview Process

1. Pre-Onsite  
   1. Recruiter Screen: TODO  
   2. QA Process Depth: the candidate will discuss a previous QA process they rolled out or improved.   
   3. HM Screen: TODO  
2. Onsite Interview  
   1. Hands-on testing: the candidate will execute a (small) Testiny test plan.   
   2. Product Depth: the candidate will discuss a previous product they QA’d.  
   3. BREAK (15 min): discuss the candidate and possibly cut them.   
   4. TopGrading Interview: the candidate will discuss various roles and relationships on their resume.

## **PS: QA Process Depth \[60 min \]**

Objectives:

* Get a deeper understanding of how this candidate has rolled out QA processes in the past.  
* Understand how the candidate would approach our QA process.

Scorecard covered:

1. (none)  
2. (i-v)  
3. (i-v)  
4. (i-v)  
5. (none)

Prerequisites:

* Be familiar with their resume. Pick 1-2 experiences that you want to go deep on.

Timeline:

* 10 min: meet & greet.   
* 20 min: discuss their previous QA Process rollouts.  Questions below.  
* 20 min: do a “reverse interview” and have them ask us about our QA process. Questions below.  
* 10 min: answer candidate questions/overflow time.

Part 1: Prompts & Answer Quality:

* I saw that you joined X team, I’m curious about what their QA process looked like and what you did to improve it. Can you tell us that story? \[you may need to jump to a different team if you picked one that they didn’t really change anything in\]  
  * HINT: make sure when you ask this question you double check what THEY DID to improve things. If they use a lot of the “we did this” or passive “this happened”, DIG IN and ask “what did you, specifically, do in this situation…”  
  * Bad: no good stories, or very vague answers. They can’t describe the QA process, or “it was fine” and they didn’t do anything concrete to improve it.   
  * OK: they talk about the tools they rolled out, the test cases they wrote, the JIRA process they set up, etc…  
  * Good: they talk about how the process was not really the hard part – getting people to buy into it was harder. They have good stories about how they did that, e.g. leading by example, training, etc. Should NOT have (too much) Stick or Authority in their roll-out. No “My VP told everyone they need to start doing QA.” \++ points if they were MEASURING the impact of their changes.  
  * BEST: you should LEARN something from them and walk away from this interview with some ideas on what we should be doing differently.   
* (followup question, if they don’t touch this topic): how did engineering react to the QA process changes? Were there any engineers who resisted the new approach?  
  * HINT:   
  * Bad:   
  * OK:   
  * Good: 

Part 2: Prompts & Answer Quality:

* Let me describe our current end-to-end process. You’ve seen some of it earlier today. We also… \<describe the process in a few sentences\> I would like to swap places and have you ask me questions about it so you can reach a conclusion about what we are doing well, and what we are not doing well. Let’s spend 10-15 minutes on questions, and then 5 minutes of you summarizing what you learned about us and what you might consider changing if you were to join.  
  * Bad: they are NOT able to do discovery and ask any relevant questions.  
  * OK: they are able to fill up 10 minutes of questions, but their recommendations at the end feel a little copy-paste and not really designed for Mashgin.  
  * Good: they run out of time asking very specific, insightful questions (including about how QA is valued at the leadership level), and then they have easily 5 minutes of recommendations, and even some ideas on how to prioritize them.   
  * BEST: you should LEARN something from them and walk away from this interview with some ideas on what we should be doing differently. 

Email preparing candidate for Onsite:

| TODOMust include: Link to scorecard – yes, we should share this with the candidate, so they know exactly how they will be judged in this role. Link to Testiny so they can log-in and make sure it works for them. We can have a “[qa-interviewer@mashgin.com](mailto:qa-interviewer@mashgin.com)” Testiny account to share for all users. Link to PRD that we will have them evaluate. They should plan on spending 30 min reading it before the interview. Description of each interview. Link to LinkedIn profiles of the interviewers they will be meeting.  |
| :---- |

## **OS: Hands-On Testing \[90 min \- \]**

Objectives:

* Give the candidate a feeling for the day-to-day job and working with the Mashgin team.  
* Make the product a concrete thing for the candidate. Get them excited about improving it.  
* Evaluate their ability to think critically about OUR testing problems. 

Scorecard covered:

1. (i), (iii), (v)  
2. (i), (ii), (iii)  
3. \[none\]  
4. (i), (ii)  
5. (ii)

Prerequisites:

* We should have a broken build\!  
* Need fake “release notes” for them to test  
* We should have a Testiny run ready-to-go. Should be TOO MUCH to do in 40 minutes. They should prioritize.   
* They need a login to Testiny.  
* They need to bring their own laptops and be ready to log into Testiny. 

Timeline: 

* 15 min \[interview room\]: meet & greet, introduction to the Mashgin machine \+ Testiny.   
* 30 min \[back QA room\]: hands-on testing (candidate can be left alone)  
* 30 min \[interview room\]: discussion on problems with the Mashgin machine \+ testing process. See questions below.  
* 15 min \[interview room\]: answer candidate questions/overflow time.

Prompts & Answer Quality:

* How would you improve the Mashgin kiosk/this feature?  
  * Bad: the candidate has no answers or generic answers like “make it faster.” When you dig in *why* they would want to improve that, they can’t back up their statements.  
  * OK: their answers might be uninspiring/standard, but they can reason through them. They are able to tie things back to the customer experience.   
  * Good: they have very insightful answers that most folks using the machine for an hour may not have reached. They are able to think of various stakeholders (end-users, CSRs, etc) and think of improvements for each. \++ points if they think of HW improvements as well as SW improvements.  
* How would you improve our testing process?   
  * Bad: they are copy-pasting from a different company without thinking, e.g. “I would switch to JIRA and TestRails.” Or: their answers are generic and not influenced by them doing QA for 30 minutes.  
  * OK: they have specific feedback on *tactical* changes they could make, e.g. improving certain test cases, or using a tool we haven’t considered. They are able to back up their feedback with stories, evidence, etc.   
  * Good: candidate comes with *written notes* about what they would improve (i.e. they are thinking about it without us even asking about it\!\!). They are able to give tactical AND strategic improvements, ideally teaching us something WE HAVEN’T EVEN THOUGHT ABOUT.

## **OS: Product Depth \[60 min \- \]**

Objective: 

* Give the candidate a feeling of how we run product at Mashgin, and how they are expected to engage with our PMs.  
* Gather evidence that they go really deep on products they’ve worked on in the past.  
* See if they are passionate about the Mashgin product and will feel motivated to improve it. 

Scorecard covered: 

1. (i-v)  
2. (none)  
3. (i-v)  
4. (none)  
5. (i)

Prerequisites:

* Be familiar with their resume. Pick 1 product that you want to go deep on.  
* Have a PRD that can be shared with the candidate BEFORE the interview. 

Timeline:

* 10 min: meet & greet.   
* 20 min: discuss a previous product the candidate is very familiar with. See questions below.  
* 20 min: discuss a Mashgin PRD and get the candidate’s thoughts. See questions below.   
* 10 min: answer candidate questions/overflow time.

Part \#1 Prompts & Answer Quality:

* Tell me about Product X. What did you love about it? What did you hate about it?  
  * Bad: uninspiring answer with basic examples.   
  * OK: the candidate has some good details and clearly an eye for quality – but no emotions attached to it. The product is “just work” to them.   
  * Good: the candidate has a *story* about why they went to work on the product. It mattered to them. They won’t shut up when you ask this question and you have to gently direct them to the next one…  
* Why was this product important to customers?  
  * HINT:  Keep digging with “why” questions until you feel you wouldn’t be able to get a better answer from the CEO of that company\!  
  * Bad: they are NOT able to tie the product back to customer value.  
  * OK: they have a rough sense of value of the product but not as good as you would have as a PM.  
  * Good: their value is as good as yours would be.   
* How did you make Product X better during the time you worked on it?  
  * Bad: the candidate performed QA and made sure bugs didn’t go into production.  
  * OK: the candidate found edge cases that were not thought of by anyone else and caught real production bugs. \++ if the candidate was involved in product requirements definition or weekly engineering discussions.  
  * Good: the candidate changed the culture on their team so that all engineers/PMs cared more about quality. Should have a very compelling story here. Make sure you get examples.  
* (followup, dig-in if they aren’t answering) Give me an example of how you disagreed with a product design, and what you did in that situation.  
  * Bad: the candidate has no examples, or if they have examples, they did not do anything about it (that could be worse\!).   
  * OK: the candidate has at least one example. They tried to influence product/others to change the design, unsuccessfully. Their example might be uninspiring/simplistic.  
  * Good: the candidate has an insightful example and a great story about how they lobbied Product to change the design. Success is a \++ but not necessary. If they failed to convince Product, they should have a good story (and learning\!) about that as well. 

Part \#2 Prompts & Answer Quality

* What are your thoughts on this PRD, after having played with the kiosk itself?   
  * Bad: the candidate struggles to engage at the PRD level. They are waiting for more direction/specific actions requested and can’t deal with a vague question. They might immediately jump to testing without asking any questions.  
  * OK: the candidate has a lot of questions about *why* the product should behave this way. Then they come up with good ideas on how to test the PRD, but no thoughts about the product itself.  
  * Good:They should do the “OK” and also have lots of thoughts about other approaches that might solve the user problem better.  
* (followup, dig-in if they aren’t going in this direction) How would you test this feature?  
  * Bad: candidate would be vague or say “I would run our regression tests.” They might propose some new tests but not be concrete.  
  * OK: candidate would propose very concrete tests, using a framework like [BDD](https://testomat.io/blog/writing-bdd-test-cases-in-agile-software-development-examples-best-practices-test-case-templates/). They are writing them down on the whiteboard or in a doc.   
  * Good: candidate is thinking about risks. They are comfortable not testing everything and specifically talk about prioritizing the various test cases they think of. 

## **OS: Topgrading \[90 min \- \]**

Standard TG.

Scorecard covered: 

1. (iv), (v)  
2. (iv), (v)  
3. (iv), (v)  
4. (i-v)  
5. (i-v)