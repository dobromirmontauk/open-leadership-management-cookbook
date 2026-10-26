1. Evolution of a Team (an Engineer's perspective)
2. 


Scratch
* Engineer -> idea -> code
* Some point the code needs to be "released" (sent to customers). The *deployment* of the code is a separate system than the code!
	* Boxes for testing/building/releasing code
	* The "release" can break -> feedback loop
	* The "production system" can break (not necessarily bugs) -> feedback loop
* Later SREs show up when the *production system* is so complicated that you need full-time team of people just untangling the wires
* Engineer ends up with a lot of information in their brain. Brain gets big, like a ballon.
* Adding another engineer to the team. Now they have to talk back & forth about the code. Small mouths, even smaller ears --> speed does NOT double.
* Keep adding more people, communication becomes complicated. 
* First customer, starts talking to one of the engineers more than the others --> that one becomes "PM light" but still part of the team.
* Lots of customers -> That eng keeps getting pulled AWAY from the team --> finally a "PM box" responsible for this part.
* Eng team keeps growing -> code gets messier --> more "phone lines" between people, gets messy
* Team splits into two -> phone lines get simpler, one major phone line between both teams, but the codebase is still spaghetti between the two (and production is still one prod)
* Going back to customers -> first customer rarely asks for anything, than more & more -- features and bugs. When too many bugs (angry customer), we have to bring in a QA person, "between" the code and the release. As more customers grow (or more teams grow), we may have to increase the amount of QA.
* Also draw a step where engineers are spending more & more of their time testing --> PM or someone angry, "why didn't you catch this bug", but they are looking at the spaghetti crossing multiple teams and yelling "I don't understand it anymore!"
* PM gets overwhelmed with all "need help" requests -> spin up a "support person", support person might have direct access to engineers with important FIRE!s but an arrow to PMs for "please please fix this... someday" (and PM is saying "yes yes of course" (and thinking "we'll never get to this :(")
* We should have a slide where the eng team is surrouned by support people with fires, pushing back against cuxstomers, produc pushing back against customers, and engineers sitting around saying "huh, there really isn't anything to do..."
* Slide around "untangle the mess between teams". Show them debate & debate (maybe multiple panels) while PMs, customers get bored and fall asleep. Then finally they start cutting around the edges before finally cutting it down the  middle and splitting it.
* 3 planning loops: 
	* Fires: pager from prod system, QA filing bugs, support escalating, PM/Manager/CEO posting "Reddi thread". ~hours
	* Tactical: day -> week -> month. "What are we doing this..?" Standups, weekly planning, monthly goals / projects / etc.
		* In some of the slides there shoudl be a "backlog" next to the PM / eng where you can see requests going as we do the slides. This should start verys hort (1-3 items), then a page, than multiple pages with parts dropping the fllo
		 * Actually PM has a different list, it should look "official" like a book, "Product Plan"
	* Strategic: CEO, PMs, EMs, head of Sales, etc all debating
* Design: lots of customer questions "how does this work" --> PM has a bright idea "we need a designer!" --> one more box to coordinate with.
* First eng team split should be FE/BE. Then the release gets complicated -> DevOps. Then customers ask for "intelligence" --> add Data/ML. Then a hacker 'breaks into the system' -> add Security (and a compliance person who also has a list of things going into the roadmap). Architect shows up when we have 4-5 teams and the system starts to look like spaghetti again.
* We should make this Mashgin-specific, so the teams we will eventually have: 
