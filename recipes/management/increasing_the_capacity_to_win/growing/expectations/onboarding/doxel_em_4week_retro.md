## What are we doing well?

* The engineering culture here at Doxel promotes trust, safety, candor, and strong expectations. I have seen evidence of
  people voicing their concerns right away when they feel that something needs to be discussed.
* Monorepo. I don’t have to attach context to arbitrary repository names. Most importantly, it’s very easy to find
  things since everything is in one repository.
* Team collaboration within Engineering. It’s more often than not that teams create silos within Engineering. I’m glad
  to see engineers from different teams collaborating with each other through discussions, TDD’s, and technical book
  club.
* Topgrader session for hiring. This is the personal statement for interviews. The TopGrader portion allows us to get
  deep insight into the challenges the candidates have faced, their accomplishments, and the impact they’ve had at their
  previous positions. Furthermore it allows us to evaluate their quality as a human being, assessing their empathy,
  humility, confidence, etc.
* All Hands. I appreciate the transparency and the deep dive sessions from all the different teams.
* Recorded sessions of important meetings. This is a valuable resource.

## What should we continue doing?

* Continue on improving the onboarding process. There is enough content, but there are things that need to be trimmed
  down so that it is digestible in the first 2 weeks.
* Incrementing on On-Call (this is on my plate) and Postmortem process. Postmortems are very useful to reflect on the
  incident and learn from it. Current process needs to be improved so it’s much more streamlined and less time intensive
  for the person responsible for running the postmortem.
* Continue to be more and more disciplined about unit and integration testing. It is misunderstood that a team can push
  out and deliver more features by skipping thorough requirements gathering, design, and testing. This is a
  misconception, since it will have a cascading effect causing deployment failures, refactoring, and production issues.
  **Much like Doxel helps the customer to find defects as soon as possible on the construction site, we need to find
  development issues as early in the software development lifecycle.**
* Continue to standardize the TDD process. An engineering culture where engineers are encouraged to get feedback on
  their design, is an engineering culture that will excel in my book. It’s a great way for everyone to learn, find out
  what others are doing, and gives everyone an opportunity to make a business impact as one engineering team.
* Continue to focus on priorities through OKR’s and other higher resolution methods. Queuing theory in math tells us as
  utilization approaches 100%, the lead time to getting things done approaches infinity. In other words the more things
  we have on our plate, the slower it takes to get anything done. We need more focus so we can do just the things that
  deliver the most impact with the least amount of work.

## Areas of Improvement

I’d like to use the definition of Doxel as an analogy to what the engineering team needs to become. Below is an excerpt
from :

“Doxel is a real time construction optimization platform that empowers decision makers with predictability and control
over their projects, contextualizing disparate project data and generating timely insights to optimize construction and
business outcomes.”

Much like Doxel -

The engineering team needs to be an organization that empowers teams with predictability and control over their
projects, contextualizing: progress, cost, time, and human capital, generating timely insights to optimize software
delivery and business outcomes.

We must be good to ourselves and implement systems, tooling, and infrastructure akin to what we’re building for Doxel’s
customers. This includes but is not limited to:

### Practices to Follow

* Practice Agile Methodology and Lean Engineering to curate a set of “Doxel” practices that allow action from early
  feedback in order to have better predictability of software delivery, lower defect rates, and increase developer
  productivity. James Shore’s “[The Art of Agile Developmen](https://www.jamesshore.com/v2/books/aoad2)t” and Nicole
  Forsgren’s “[Accelerate](https://www.goodreads.com/en/book/show/35747076-accelerate)” are good references to get some
  ideas going in this area.
* Practice just enough Domain Driven Design, to ensure engineering, product, and domain experts are speaking the same
  language and that the software is written to match the domain. A lightweight group exercise Doxel can do here to
  understand existing software or implement new domain problems is event storming. Alberto Brandolini goes deep into
  this in his book, Event Storming. A DRM free version of the e-book is present in
  Doxel’s [gdrive](https://drive.google.com/drive/u/0/folders/1crPSM8-WFYEiaQqUUruURRtJVfA8kJSk). Event Storming of the
  whole Doxel domain should give us aggregates which would be a good integration test to see if we’ve formed our teams
  right.
* Use user story mapping so that engineering and product are always aligned on where we want to go, where we are headed,
  and what the system is intended to do, so that we don’t build solutions that aren’t enough. Jeff
  Patton’s “[User Story Mapping: Discover the Whole Story, Build the Right Product](https://www.goodreads.com/book/show/22221112-user-story-mapping)”
  is a good resource here.
* Using the [Testing Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) along with testing
  management software to write and maintain tests with different granularity, with fewer tests the higher the level,
  allowing for software engineers to own quality but still develop fast.
* Follow a phased approach to adopting security with something like [CIS Controls](https://www.cisecurity.org/controls/)
  and [OWASP Top Ten](https://owasp.org/www-project-top-ten/) to ensure that an unlikely but detrimental hack won’t
  jeopardize the prosperity of the company.

### Technology to Implement

* Best in class authentication and authorization to seriously secure user data.
* Best in class distributed logging, so that we can identify root cause of system failures and degradations to enforce
  SLAs and save time for engineers.
* Best in class CI/CD pipelines, emphasizing on local development, unit testing, topic branch deployment, integration
  testing, and feature flagging, to minimize risk, maximize correctness, without sacrificing velocity.
* Best in class E2E integration testing, so we can test full functionality frequently.
* Best in class application performance monitoring, metrics monitoring, and distributed tracing.
* Best in class insights from github data to experiment faster, ship reliably, and prevent burnout.

### Caveat

It’s easy to say these things are all important, but investments and short term opportunity costs will need to be made
to adopt these practices and implement these technologies. In most cases this means **Horse Trading** of priorities is
needed but definitely **No Piggy Backing**!

## Summary

**Overall I’m just excited to be here at a pivotal stage at Doxel, and looking forward to taking part in Doxel’s journey
to bring valuable insights to construction, one building at a time!**
