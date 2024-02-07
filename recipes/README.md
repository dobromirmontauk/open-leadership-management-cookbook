# Table of Contents

1. [Leadership⚠️](leadership/): rough notes, I don't recommend visiting yet.
1. [Management✅](management/): starting to come together with some useful content.

# "Leadership" vs "Management"
'Leadership' and 'management' are hard to define & distinguish. It's almost tempting to throw up our hands, give up, and shove all the recipes together.

But there _is_ a difference, and we believe that not attempting to untangle the best leader patterns from the best manager patterns hurts our ability to grow the next generation of both. An illustration of this confusion comes from [TWIG](need_link_here), the Engineering Leadership class that Dobromir founded at Twitter. This was a course aimed at Individual Contributors, not managers, and yet a frequent question was "should I take this class if I want to become a manager?" One of the few strong, uncompromising positions we'll take in this cookbook is that _leadership is not just for people managers_. We strongly believe that teams cannot become [High Performing](need_link_here) without _every_ member's leadership voice. 

So, as a very rough cut, recipes that mainly apply to people managers will go under the [management](management/) tree, while all other recipes will go under the [leadership](leadership/) tree. When there is ambiguity on where to find a set of recipes we will link them from both sides to make navigation easier.


# Explaining the Difference

We've seen the question "what is the difference between Leadership & Management?" come up often enough that it deserves its own set of recipes. Please contribute your own explanation here, or link to really good ones you find online!

## Dobromir's Recipe

Both Leadership & Management are fundamentally about changing how people think. Change how they think, and they'll
behave differently. Change how they behave, and they'll reach different outcomes. Like the physics equivalents of
acceleration, velocity, and position, to reach a certain (x, y, z, t) one must focus on the correct acceleration. To
create the necessary outcomes, we must focus on how people think. But if they are both about changing how people think,
why do we have two words for them? What is the difference? Admittedly, this is something we have struggled with
throughtout our careers, as have many others. We encounter so much confusion with these words, confusion that causes
folks to make bad career choices! Are leaders managers? It's obviously not a hard requirement. Are managers leaders?
Sometimes, sometimes not. Can you manage without direct reports? Well, yeah... Look at any Product Manager helping their
engineering team deliver. Or even those talented Tech Leads mentoring junior team members via 1:1s. Can you have direct
reports and not do 'management'? Unfortunately yes...

If we can accomplish one thing with this cookbook it would be to demystify these two terms and in the process create a
new generation of "non-manager" leaders and "I-love-management" managers.

So how do we come up with a useful definition of Leadership & Management that allows us to organize recipes in a helpful
way?

[TODO(dmontauk): I want to add 5-6 examples here that make it intuitively clear what the difference is]

We hope that the examples above motivate one specific realization: _leadership_ seems much more dangerous! There's a
certain _step change_ needed to make something qualify as 'leadership' instead of 'management'. When a management
approach fails you kind of end up where you started. When a leadership approach fails, things might be _much worse_ than
before. Why is that?

Since we're all engineers here we'll try to illustrate this fundamental difference between the two using an engineering
concept. Let's imagine our organization as a complex system with some optimization function. For a business it could be
the 'Net Present Value' of that business; for an engineering team, it could be "NPV created per $ spent" or some-such.
In real life these functions become incredibly complex and we try to capture approximations of them using OKRs. The
exact function isn't important here; what's important is (almost) all these functions have one commonality: _local
maximums_. Here is an illustration:

[TODO(dmontauk): picture here: 'you are here, here would be better']

Management is about moving up the gradient curve of the optimization function. Most team members (_see below_) will
agree this makes sense and it won't be a controversial move. It may still be a lot of work, you're not guaranteed
success, yadda yadda. For example, you want to roll out a
better [hiring process](management/increasing_the_capacity_to_win/hiring). You write a bunch of scorecards, you do a
bunch of training, but then you get distracted with some fires and 3 months later it turns out your team is kinda hiring
the way they were before. Maybe they're incrementally better at identifying talent. Maybe you improved things slightly,
not worth it looking at how much energy you put in, but if you quit now the organization isn't worse off. Maybe you can
even pick up where you left off, and folks will be excited to help again. Not a huge fail.

This is common.

Leadership is about moving towards a _better global optimum_. We can illustrate it like this:

[TODO(dmontauk): picture here: 'you are here, going this way, but if you can end up here it would be WAY better!']

Hopefully this picture is a good example of the explanatory power of good [Visualization](/tools/visualization.md). A
few things should jump out:

1. If you start down this 'leadership' direction, you may have to immediately make things worse!
1. For some period of time it feels like a slog -- things keep getting worse, not better!
1. When things to start to get better, they are still worse than they were before!
1. If you quit halfway, you're in a worse position than when you started!

We can illustrate this using our hiring process example. Perhaps you've determined that your recruiter can't
do [Consultative Selling](/tools/consultative_selling.md) and keeps losing candidates to big companies. You've also seen
that some of your engineers don't value Fit and are only looking for technical strengths. When you propose your new
hiring process it isn't seen as an incremental improvement; you actually get hostility from the team. They think you're
being wishy-washy and proposing a way to hire your friends that don't meet the technical bar but have this vague 'fit'
thing going on. Your recruiter resists any changes to his approach because it 'worked great at Google' and what do you
know about recruiting, anyway? You're a new Head of Engineering and he's been doing this for thirty years.

You take a deep breath, fire the recruiter, and take some of your top ICs off the interview loop. That might be
Leadership, with a capital L. It also might be plain foolish. Guess what: you won't know until you reach the
destination, or fail to.

### It Gets Worse

We said above that "Most team members will agree this makes sense". They unfortunate fact is that it's unlikely that
everyone in your organization even has the same optimization function in their head (if they do, congrats! You must be
doing something really well!!). Reality looks more like this:

[TODO(dmontauk): add a picture here]

That means the 'obvious' management proposal you might be making gets judged differently by different people -- and they
probably won't even tell you. To some, those scorecards you proposed feel like a massive waste of time. Just more
paperwork. They might not even be wrong -- perhaps the last Head of Engineering tried this a year ago and the office
floor is still littered with crumpled rating systems. So what you judged to be 'just a management challenge' is turning
out to be a management _and_ leadership challenge, interwined, with no easy way to tell what recipes you need to use
with which individual. Oyyyyy....

This is why we can't have a leadership cookbook without a management section, or management recipes without referring to
leadership ingredients...

### It Gets Even Worse

All this talk of optimization functions, local maximas and global maximas... It makes the situation feel way more
certain than it really is! Let's try to get an even more accurate drawing:

[TODO(dmontauk): drawing of a peak that is foggy and perhaps not taller, and in the other direction another peak as well...]

That's more like it. Leadership isn't just challenging because we may have to make things worse of our organization (
temporarily we hope), or because it's an awful lot of work to climb the hill on the other side. It's also challenging
because _we cannot be certain we are right._ Perhaps we spend 3 months refactoring our entire hiring process and then
the CEO announces layoffs and a hiring freeze because revenue missed expectations because engineering didn't deliver on
some features it had promised because some key engineers quit out of annoyance that their 'technical contributions'
weren't enough anymore. Perhaps there was an entirely other direction we could have gone in that would have given us a '
bigger win' with 'less effort'.

Leadership is hard because we just don't know, but we have to pretend that we do.

## That's Why I Split Leadership and Management

Leadership is not for the faint of heart.

Management is not for the impatient.

You really need a wallop of each to 'change how people think', which is ultimately the goal. How much of a wallop? That,
dear friend, is really up to you. That choice defines your style. We don't have a recipe for it. You get to choose how
much you want to grow as a leader, how much you want to grow as a manager, and how you mix & match the two. Don't worry
about being perfect, we haven't met anybody who's achieved perfection in either, let alone can flex in both!

Hopefully, this cookbook will give you recipes where you need them most. 


## TODO
My recipe has a TON of stuff I want to expand on. Notes here:

1. My L/M recipe: leadership is about risk to yourself, to your reputation, to your career. If there is no risk, it’s not leadership. 
2. Small leadership ‘bumps’ for a Sr. EM might be huge leadership moments for more junior employees. That’s why leadership/management is a spectrum. 
3. See all my notes I wrote up in Google Docs [here](https://docs.google.com/document/d/1LwOIhMI0MsCYePKU7sz2eigs-PcSJ6tuVXIbZGtUJdk/edit#heading=h.gu4ti1e72vvr). Need to integrate that here.
1. Need to use examples of a strong leader / bad manager and poor leader / strong manager to distinguish between the two types.