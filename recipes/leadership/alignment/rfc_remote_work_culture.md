# Motivation



    * Already were largely remote pre-COVID
    * This is an experiment; revisit in 6 months and probably again in 12 months
    * Expect COVID conditions to last 6+ months
    * Our business will likely require remote-friendly culture + processes even more as we grow. Our customers build around the world. If we are scanning Google, MSFT, and FB DCs we will likely be operating in 10+ countries in the next 2 years.
    * Turn this into a competitive advantage: access to talent, faster execution, etc.
    * “There should be no unwritten rules in a distributed organization.” -- Guide to remote work
    * 


## Employee expectations



    * Read this carefully. Comment on it. A lot should be obvious and in fact already in-effect for a while now. We are writing it down so there aren’t any unwritten norms or expectations that cause confusion for existing or future employees. 
    * Much may applicable to in-office work but matters even more in a remote culture so is called out explicitly. 
    * Everyone ([CEO] down) will need to explicitly AGREE to the proposals. We can’t have different people operating differently; having rules that are partially-followed is worse than not having rules at all.
    * Some items will be MANDATORY and are called out as such. Other items will be RECOMMENDED. 
    * While different approaches were considered in sections of this RFC I haven’t always called them out in an effort to keep it brief. I’ve left multiple options in sections where none is obviously better and the choice will be better with consensus.


## Biggest Challenges/Risks

As we transition to a remote-first culture there are numerous challenges/risks that might cause us to falter as a company. Please keep in mind the ones below as you read this document and add your own!

**Lack of Trust**

Trust is a key ingredient for healthy teams/companies. When people trust each other they feel comfortable pointing out possible improvements or straight-up mistakes. When people trust each other they listen more productively to input from others (even if it hurts!) and come to solutions rather than arguments. When trust is missing… even obvious problems go un-solved and the company limps along.

To win [COMPANY] needs to discover our internal mistakes, learn from them, and self-improve faster than the competition does. Having strong trust between individuals/teams so we can do this is especially difficult in a remote-first environment. The “human touch” is missing! We don’t interact as much as “just people” and we risk developing transactional relationships. Those don’t do well under stress and friction.

**No information osmosis**

Random dissemination of information around lunch tables or random walk-bys are a great way for individuals to hear about what’s happening and - possibly - develop a serendipotous connection. This helps individuals have impact outside their day-to-day function and the company move faster. Without osmosis people may feel more “stuck” inside their day-to-day job and good ideas won’t flow quickly.

**Too many meetings**

This challenge often comes from people overcompensating for a lack of natural information osmosis. They go to more meetings (even if &lt;10% of it is useful to them), they have more 1:1s trying to figure out what is going on, and they schedule more in-person reviews since whiteboarding worked well in the office. Unfortunately, video-conference meetings just can’t replace all the benefits of physical co-location and throwing a lot more hours into them most likely will slow us down as a company.

**Too much process/not enough process**

This is always a difficult balance and doubly so when the effects of process are not as visible. In the office it’s easier to see how much time people are sitting in an office or working on “overhead” instead of their core job. Without careful tuning we can end up requiring too much paperwork from our teams - or not enough, both of which slow us down.

**Slow learning**

It’s hard to improve your work when you can’t just tap someone on the shoulder (seeing that they aren’t super-busy) and ask “hey, how can I do this better?” New tools/ideas/etc won’t flow quickly if we don’t have an more explicit way to up-level our teams.

**Slow course correction**

Everyone is constantly making mistakes. Working on low-priority items, not understanding the actual deliverables, not being aligned on design… We run the risk in a remote-first culture of spending a lot more time going down the wrong path since it won’t be as obvious to others what path we are on. 


## Grand Cultural Strokes

As we design a remote-first culture we have a couple of “cultural north stars” we’d like to achieve. We’ll be incredibly proud if we can say “this is our culture” in a decade.

**Communicate Intentionally**

_Intentional communication_ happens when an individual maps out in their head _what other people know, don’t know, and **should know**_ and then communicates the relevant information, to the relevant parties, in the relevant forum. Unintentional communication is what most individuals do most of the time: communicate thoughts in their head without considering their audience, the forum, or perhaps even the message.

Intentional communication is _tough_. It requires constant awareness (and checking) on other people. It used to be the domain of fairly senior individuals (in fact, it’s a key distinguishor between junior and senior employees). It’s incredibly important since both failure modes hurt the organization. Overcommunicating distracts people from execution: not everybody needs to know everything right away. Undercommunicating leads to siloes, missed goals, and in the worst case political cabals. 

In a remote-first culture we have two choices. Either we hire senior individuals (especially managers) that do a lot of “polling” of their employees (i.e. micromanaging) and then can handle the intentional communication. Or, we expect everyone to do it. While the latter is harder I think it will make us a lot more successful.

So, to build trust with your manager and teammates: _you need to proactively communicate_ what they need to know, and especially what they don’t know that they need to know.

**Execute Efficiently**

Time is one of our greatest assets. Don’t waste it. Don’t slow others down and don’t slow yourself down. Use all the rules and recommendations here with the lens “will this help [COMPANY] move faster?”

In a remote-first culture efficient execution is done by clear goals (company, team, and individual), clear delegation of responsibility + tasks, “just enough” communication, and a bias to action. A good rule of thumb is &lt;20% of time should be spent on communicating (&lt;8 hours/week, although this depends on role) with >80% of the “needed” information transmitted. Why not 100%? In my experience, most people spend _the ROI curve (value/time) on more information drops quickly after 80%_. E.g. in a meeting about a database design the team could get into details on fields, constraints, etc - but that could take an hour, whereas just putting together a schema would take less time and provide _more information_. 

Instead, individuals should feel very comfortable ending communication with some ambiguity and switch into execution mode. The ambiguity will usually resolve itself into deeper questions or just disappear. A good rule-of-thumb for engineers is **code speaks louder than words **(bias towards a PR, even if a rough draft, and not a meeting); for others **written is more scalable than spoken** (avoid the meeting until you have a written proposal, design, etc).

(note this maps somewhat to “decisiveness/hunger” in our [Virtues](REDACTED))

**Default to YES/ON-TRACK**

Organizations move quickly when individuals assume they have permission to execute (“default answer is YES”) and that other teams are on-track by default. This eliminates entire classes of communication (‘permission/status checks’) that have very low ROI. Note that a culture can only adopt this if they have done the work to execute efficiently above. 

In a YES/ON-TRACK culture, any time something might be a NO or work is OFF-TRACK, **every employee is required to pull the rip cord!** If you know we are not on-track (or you don’t know what the track is!) and you haven’t called it out, you are not living up to your responsibility as a [COMPANY]ian. This may feel very uncomfortable - calling out the Head of Eng that they are making a bad decision isn’t easy - but working in a company where your boss is constantly prodding “hey, what’s going on with X…” is even less fun.

(notes this maps somewhat to the “intellectual honesty” in our [Virtues](REDACTED))


# Communication Architecture

In this section we document processes, expectations, and tools for [COMPANY]’s internal communication as a remote-first company.


## Working Hours/Days

Communication starts with knowing what to expect from your coworkers in terms of availability.


### Required “availability” hours: 8:30am-12:00pm PST Monday-Friday

PST is our primary timezone. By that we mean that our current leadership team is based in PST and we expect this to continue. In order to minimize friction for “synchronous communication” we are designating 8:30am-12:00pm PST as the block for this. This has the most overlap with timezones we currently work in for synchronous communication:



* London (GMT): 16:00-20:00
* Europe (CET): 17:00-21:00
* India (??): 21:00-00:30
* China: ??

Note that this does NOT WORK for the following time zones (“middle of the night”). However, we do not have any employees there and so are not worried about this yet:



* ??

ALL EMPLOYEES are expected to be available during this synchronous block and, to the extent possible, meetings/synchronous cross-company commmunication will be scheduled in this block. E.g. All Hands, standups, sprint planning, Founder Reviews, OKR meetings, etc. 

For employees without pre-scheduled meetings in the “sychronous block” we would still like reasonably quick response (~15 minutes) to requests for synchronous communication. 

**If you must schedule a meeting outside the synchronous block**: please be extra careful to take notes and share them widely with remote employees who did not participate! This is widely discouraged; 8:30am-12:00pm M-F is 17.5 hours/week of blocked time which should be _more than enough_ for all the meetings we need during the week. 


### Working Hours: set by employee

Outside of required availability, employees are expected to set their own hours in cooperation with their manager and team. While individual constraints will be taking into account please remember that the needs of the team/[COMPANY] do need to come first. 

Expectations of employees:



* A normal work week (for full-time, salaried employees) is 40-50 hours. 
* If you are regularly working &lt;40 hours, **please have a conversation with your manager. **We have a LOT to do at [COMPANY] and can probably get your help on other projects! It’s much better to ask your manager how you can help the team today than to find out months later that your manager is unhappy with your impact/output compared to others on the team.
* If you are regularly working >50 hours, **please have a conversation with your manager. **While there are often ‘crunch periods’ where even 60+ hour weeks may happen we _know this is not sustainable_ and don’t want you to suffer burnout. Remember, in a remote-first culture it is very difficult to see when people are working. Your manager may not even be aware you are pulling late nights and that work needs to be re-balanced or perhaps the team is too small to handle the workload.
* If your work hours are interfering with your personal life, like picking up kids from school or doctors appoints, please talk to your manager. While we can’t guarantee infinite flexibility a conversation will almost always resolve the issue.
* Working hours should be **explicitly set in Google Calendar** using the “working hours feature.” This will automatically decline meetings outside your working hours. 
* Holidays are tracked on Google Calendar here.


### PROPOSAL: Focus Time

A lot of the work at [COMPANY] is quite complex and requires many hours of no interruptions to make real progress. This is true for annotation, engineering, product, etc. In order to balance our _rapid_ _communication _needs with this _high throughput execution _need I propose we implement Focus Time.

Focus Time is an explicit block on Google Calendar so people don’t schedule meetings, expect you to respond to Slack, or complain that you aren’t doing code reviews. You set these blocks when you need them, ideally as far ahead as possible.

The average individual contributor should be able to get about 20+ hours of Focus Time/week. If you are finding it hard to find that, talk to your manager or team lead. We expect roughly the following non-project overhead per week:



* All Hands: 1 hour
* Standups: 2.5 hours
* Team meeting (sprint, etc): 1 hour (2 hours every 2 weeks)
* Checkins (Founder Review, Weekly Project Checkin, etc): 1 hour
* 1:1: 1 hour
* Misc syncs: 2.5 hours
* Total: 9 hours

For example, for PST employees a good Focus Time would be 1pm-5pm PST. **We highly recommend that a team coordinates their Focus Time**; it would be quite awkward if two people on the Annotation Team want to chat with the rest of the team 3pm daily and work in the evenings while the others are trying to code then. 

**WARNING: **Focus Time should not come _on top of your other work_, i.e. if you are in meetings 8:30am-noon, then unblocking yourself/other engineers 1-5pm, and then coding 9-midnight - you might be doing something wrong. Talk to your manager and figure out how you can have a sustainable schedule that balances your work vs other needs.

**If this proposal is accepted**: we’ll work with every IC to make sure Focus Time is on Google Calendar and we’ll start enforcing the “no interruptions” rule (on Slack + Google Calendar).

Exceptions to Focus Time



* **On call**: if you are on call you MUST be on Slack and phone and ready to respond in &lt;15 minutes.
* **Interviews**: interview blocks may need to be scheduled over your Focus Time. Since they need Focus Time too, they kind of qualify anyhow :)
* **Emergencies**: if we need to pull you into an emergency we’ll call your phone. Make sure it is still on for calls.
* **Code Yellow/Code Red**: If any projects are in a Code Yellow/Code Red then we may pull individuals or the whole company into urgent action and cancel Focus Times temporarily.


### PROPOSAL: “Respond Time”

Since we are encouraging employees not to be “always on” Slack/meetings/etc we should be more explicit about when communication will happen outside our _Required Availability_ hours. This is especially important for “important but not urgent” communication like design docs, code reviews, product proposals, etc.

Respond Time is most important within teams that are frequently synchronously blocked on each other (e.g. code reviews). The proposal is that these teams discuss when they will be in Respond mode and block off the time on Google Calendar. Then everyone can have ad-hoc Slack or VC chats, quick code review turn-around-time, etc. Non-team members will have clear visibility when the team is available for a quick conversation about something without disrupting Focus Time.

**If this proposal is accepted**: we’ll try this out on one team and see if it works well.


### PTO

PTO needs to be approved by your manager **before you schedule it** and tracked on your personal calendar and the PTO calendar here.


## Tools

This section is short since the tools we use are pretty obvious to everyone:



* Email/Calendar/Docs/etc: GSuite
* Chat: Slack
* VC: Zoom
    * PROPOSAL: I think we should switch to Google Meet. I believe the quality and feature-set is on-par now and this gives us free unlimited licenses for everyone. We are still being hit with the “40 min limit” occasionally. Furthermore, it has better integration with other GSuite tools.
* Whiteboarding:
    * PROPOSAL: try to use JamBoard 
* Devices:
    * Standard-issue laptops for everyone.
    * PROPOSAL: annotators should get beefy desktop machines to deal with Navvis clouds + larger models. This is especially true if they want to VC and show off models remotely; machines chug along slowly.
    * PROPOSAL: tablet devices for engineers. 2nd device useful for VC (without killing primary device) and better whiteboarding experience with pen. 
* JIRA: project tracking & product milestones
* 


## Medium Bias

[COMPANY] prefers the written medium! At Basecamp they say “speaking only helps those in the room, writing helps everyone” and we agree. Any information shared via VC or phone cannot be shared further (this often holds true for Slack too because of the difficulty of consuming chat messages later in time). In the spirit of _intentional communication_ make sure you _document_ important information shared verbally in the _right_ _medium _afterwards and share it with the right _audience_. Examples:



* Standups: ticket progress/status updates should be in the JIRAs. 
* Product decisions: documented in PRDs or in Product Planning doc after.
* Strategic decisions: email to relevant teams or company.

_Employees are expected to be proficient in written English. Performance reviews will cover written communication gaps_. Writing quickly and clearly has always been important and now is essential. For team lead/manager positions we expect an incredibly high signal-to-noise in their writing: we are all busy and benefit from tight communication.


### When & how to use the tools

Here is a rough guide on how to use our various media:



* Slack: “best-effort” communication that might not get seen/might get lost (search sucks). 
    * DO: Great for almost-real-time discussions with a slightly broader audience.
    * DO: create specific channels for the right audience. Make channels private to help with freer discussion (especially team channels). 
    * DO: log off Slack when in Focus Time or outside of work hours! If people **really** need to reach you they will call you.
    * DO: use Slack’s Google Calendar integration so people can see when you are in a meeting.
    * DON’T: Use Slack for 1:1 or 3:3 communication about work details! This loses one of the most powerful parts of Slack: transparency and scalability. Instead, start a thread in the right channel (so people can follow/ignore as they feel). Remember, _you are not interrupting people on Slack (see below)._
    * DON’T FORGET: if you have key information that shows up on Slack like decisions or documentation (“this is how you…”), move it to a better medium, like Google Docs, email, or GitHub. **Assume people may not read your message on Slack_._**
* Email: “guaranteed delivery” communication that everyone should (eventually) pay attention to.
    * DO: check your email! You should be skimming it at least once a day, reading it thoroughly at least once every few days.
    * DO: send announcements, docs, code reviews, anything not “near realtime” to email instead of Slack.
    * DON’T: ignore your email. This will cause more messages to go to Slack which will lower our overall productivity with unnecessary interruptions.
* Google Docs: “long-form discussion” communication for complex work
    * DO: move anything longer than a couple of paragraphs from email to Google Docs. It’s hard to reply to long emails in a thoughtful way.
    * DO: use Docs extensively for notes, proposals, design brainstorms (like this doc!), etc.
    * DO: store your docs in a logical structure! We have Shared Drives for Engineering, Product, etc. Keep your docs where other people can find them without asking on Slack :)
    * DO: Use AIs in docs: these are a _great_ way to track work/expectations across a team. Use them, and please comment on/resolve your Action Items in docs when you do get tagged.
    * DON’T: assume writing it means you are done. Docs requires more following-up with people than Slack/email. Tag people if you need their input. Use docs as a way to shorten meetings, but perhaps still have the meeting to ensure that the decision is made.
    * DON’T: assume people will read your doc right away. Give them time after you point them at it.
* JIRA: “paper trail of work” that should be used for project tracking
    * DO: file JIRAs for anything that is >1 hour of work. Seriously, it takes &lt;60s. 
    * DO: put regular updates in your JIRA. Stand up does NOT replace JIRA updates; it should be a time to focus on what is not going well and discussion. 
    * DO: tag people in JIRAs so that they get emails about it. 
    * DO: subscribe to the JIRAs of your team so you get all the updates. Scan them as part of your email flow.
    * DON’T: create JIRAs with no description and a vague title. Remember: _intentional communication_. What do people need to know? JIRA is a great place to slightly over-document. You will end up saving your own time overall.
* Meetings (VC): “high-bandwidth synchronous communication” great for when topics are not exceptionally complex and a lot of material needs to be covered.
    * DO: schedule pre-determined meetings (see below on expectations)
    * DO: schedule ad-hoc 1:1, or 1:many VC calls to unblock progress. Document anything decided/learned whenever possible (so it doesn’t just become the people on the call who know what happened).
    * DO: record meetings and share the recordings, especially in educational sessions.
    * DON’T: expect people to watch your meetings or use that as a crutch to avoid writing down the outcomes!
    * DON’T: run meetings unprepared. See below on expectations.

Exceptions to the written medium expectations:



* Manager/employee 1:1s: these are designed to be a lot more ad-hoc and shouldn’t be considered standard “meetings”. Good 1:1s should increase manager/employee trust, build strong bonds/relationships, and uncover hidden information (that perhaps shouldn’t be hidden…)
* Brainstorming/retro sessions: these are supposed to be a lot more free-wheeling. People should share sensitive thoughts or unformed ideas and may be reluctant to do so if everything is being recorded or written down. Be clear about what is being documented - perhaps only the outcomes, AIs, etc.
* Anything else?


## Time-to-Response Expectations

Everyone is doing _something important right now!_ Please avoid interrupting people unnecessarily; but do balance this with not blocking yourself/others for too long. Use your judgement. A good rule of thumb: if it will take you >30 minutes to figure something out interrupting a peer may be OK. 



* **Phone call/SMS/WhatsApp message/direct VC call: immediate**. Please pick up/respond within ~minutes. Should only be used for real emergencies. OK to use (usually) if a synchronous meeting/communication has been scheduled and you are trying to reach one of the participants who is late (and thus wasting everyone else’s time).
* **Meetings**: if your calendar does not show as busy (either not working hours, no other meeting, and not a “Focus Time”) _then you are available for a meeting_.
* **Slack: ~hours**
    * During availability hours try to respond &lt;1 hour (if you are not in a meeting it should be &lt;15 minutes). 
    * Outside of availability hours you should respond “same day”. A good rule-of-thumb is to reserve 30 minutes at the beginning & end of the day to respond to Slack messages and email. Whenever possible (if it doesn’t interrupt your flow) go check your Slack messages.
    * If you need quicker communication (i.e. real-time), start by asking. “Hey, do you have time for a Slack chat? Need some help with…” 
* **Email (includes JIRA, Code Reviews, other tools that send email): 1-2 days**
    * Email usually includes work that doesn’t “fit into the cracks” (whereas Slack should be “in the cracks”). Examples include bigger conversations, announcements, JIRA updates, code reviews, etc. Make sure you are scanning your email daily and have time set-aside every few days to empty your inbox. 
* **JIRA: 1-2 days**
    * JIRA is similar to email in terms of response time and replaces email mostly for project tracking that requires a paper trail. E.g. most engineering projects fall into this category.
    * If you need faster response-time on a JIRA ticket it is appropriate to post the ticket to Slack and @tag the individual you need a response from. Make sure the response gets into the JIRA ticket so it is not lost forever.
* **Google Docs: ~days**
    * Google docs can take many days for people to find the time to read and digest (like this one!). Please be mindful of other people’s time and share docs with enough lead-time so people actually read them/comment on them.
    * If you do have an urgent discussion you want to do on a doc, it’s OK to sometimes post those to Slack/other medium and call out the unusual SLA.


## Meeting Etiquette

A lot has been written around running effective meetings; instead of re-inventing the wheel please read the links below. Here we only document the specifically-important-to-[COMPANY] components:

Links:

TODO

[COMPANY] expectations:



* Schedule meetings on Google Calendar!
    * Keep your Google Calendar up-to-date (e.g. doctor visits or Focus Time). It’s rude to waste other people’s time rescheduling meetings because you aren’t keeping your calendar clean.
    * Respond yes/no to meetings. If you did not respond, _you are assumed a YES and you are wasting people’s time if you do not show up_. 
* Have a clear agenda at the meeeting. Add it to Google Calendar or to a regular Notes doc (linked from Google Calendar).
* Take notes for people who can’t join.
* DO NOT JOIN MEETINGS IF YOU DON’T NEED TO BE THERE. Check the agenda. Read the notes after (this will encourage people to take good notes!)
    * How do you know if you “need to be there”? If you don’t say anything during the whole meeting, you probably don’t need to be there.
    * If we notice people joining meetings and not speaking frequently we will first verbally let them know and then start removing them from those meetings. Please don’t waste our time with this and just do it yourself.
    * If you see people in a meeting that they probably don’t need to be in - _it is polite and the right thing of company resources to ask them to leave_. 
    * Exception: there are purely-informational meetings (e.g. All Hands, OKR updates) where everyone can (and should!) attend even though input from all attendees is not expected.
* Keep your video on, or if you can’t, express that clearly. A lot of information is lost already by being remote; don’t make it harder on your fellow employees by ?? of your body language cues.
* Mute if you are not speaking.
* Don’t be late. 5 minutes is considered late. 
* End them on time (or earlier if possible!)
* **Postpone the meeting if people are not prepared**. If you sent a doc and they didn’t read it - move the meeting. If people are supposed to present some metrics and they don’t have them at their fingertips - move the meeting. If this happens with the same individual twice, give them feedback. More than twice, find someone else who will not waste everyone’s time. 


# Decision Architecture

Standing meetings for decisions



1. Standups: “what are we doing today?”  
2. Sprint planning ← product invovlement. “What we do in the next 1-2 weeks”
3. OKR ← product involvement. “What we do in the next 6-12 weeks”
4. Strategic Offsites ← whole company, once every 6 months (after COVID)?


# Compensation Architecture

Local comp vs global comp

[https://www.fastcompany.com/90540288/location-based-salaries-will-kill-your-startups-culture](https://www.fastcompany.com/90540288/location-based-salaries-will-kill-your-startups-culture)

[https://about.gitlab.com/handbook/total-rewards/compensation/compensation-calculator/#location-factor](https://about.gitlab.com/handbook/total-rewards/compensation/compensation-calculator/#location-factor)


# WIP

Communication Architecture



    * 
        * 
    * Tools and their respective response-time expectations: 
        * Synchronous Communication
        * VC
            * Switch to Google Meet?
                * Everyone can have full-length meetings
                * Better integration with Jamboard?
                * Less intensive on hardware?
            * 
* Decision Architecture
    * Don’t wait for decisions! If you’re not sure who is the decision maker, raise it to your manager.
    * Big decisions: decisions should be documented in written form _(Slack doesn’t count!)_
* Tools
    * Everyone
        * 2nd device
    * Engineering
        * 2nd device w/touchscreen for whiteboarding/VC
    * Non-engineering
* Location & Pay
* FAQs
    * Can Bay Area based employees move elsewhere?
    * 

Misc



* What is our “in-person” meeting cadence look like? Every 6 months?
* PERKS
    * Do we get lunch $?
        * Weekly lunch with the team?
        * In-person lunch meetings
    * What perks make the most sense for remote?
    * Gym memberships etc?
    * 
* Travel to HQ stipend?
    * Before/after COVID
* Social aspects - how do we recreate those?
    * Weekly games?
    * “Through zoom doesn’t really work”
    * Team challenges - get number of steps/exercise/etc.
        * Health benefits!
    * 
* Awards
    * REDACTED: not doing enough of this. Need to give awards to people who are not getting enough visibility.
    * 
