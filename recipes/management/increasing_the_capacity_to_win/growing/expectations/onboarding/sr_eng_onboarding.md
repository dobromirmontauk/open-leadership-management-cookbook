# 30-Day Objective

This is an example of what we expect from you in the first 30 days. The objectives set out below are owned by you: if you feel they are not aggressive enough, or not even the right objectives, just let us know! As a senior engineer, I expect you to very quickly have an excellent judgment of what is important and the ownership to Get It Done.

Our Data Pipeline is not providing enough value to our Operations team - they are still spending significant effort on running the Rover, aligning our point clouds, and annotating objects. Our technology is “almost there” and we need to get it 100% there in the next month. This is a great time to jump into this team, have great technical impact, and start displaying the leadership we need to accelerate the company.

My expectations is that in the next 30 days you are one of the experts on our Airflow data pipeline and C++ codebase. I would love to see you improve our code (in particular: make it more stable, scalable, and well-tested) and improve our engineering processes (in particular: code reviews, production pushes, on-call). After 30 days you should have a great sense of a big chunk of [COMPANY] and start deciding where you contribute next.

Your mentor will be **[PEER]**. Please set up regular syncs with him in the first few weeks. I’ll be setting up regular 1:1s with you as well.


# Day 1 [Done]



1. Go through [[COMPANY] Onboarding Guide](https://docs.google.com/document/d/1PPX8XP4jNpYc14z2oWBaQPuyk36pk4qzvN8w7ZarhDY/edit#heading=h.ojoml789wx4). Make sure you’re done with Logistics and have scheduled all the Analytics Pipeline training sessions in the first week.
2. Review our current [Engineering Plan](https://docs.google.com/document/d/1viNjkQzRuNLl6x99oN6s92uXEZmwH893VIqbvUcdaAM/edit#heading=h.xizhcc6tre0r) and start coming up with questions (especially terms/things you don’t understand).
3. Read everything in our [Software Engineering Wiki](https://doxel-ai.atlassian.net/wiki/spaces/SE/overview).
    1. Please make improvements to it :) Organize things, clarify things, update/delete out-of-date information!
4. Pick one code base and read through it. Recommendations:
    1. [Monorepo](): contains our Airflow and Infrastructure-as-code. Will eventually contain everything (when we are done with Monorepo migration).
    1. [Alignment](): this code finds the markers in our scans and uses them to align the scan to our model.
    4. [Cropping](): this code iterates through our model objects and cuts out the point cloud in the same volume, to use for annotation and next steps in pipeline.
    5. [Matching](): This code figures out the error in objects that have been installed.


# Week 1: Get familiar with [COMPANY]



1. Write one unit test for cropping, get it reviewed by [PEER] (CC me) and checked-in. Build and push the Docker image.
    1. Bonus points if you can find bugs in the cropping code! [Done]
2. Write one unit test for matching, get it reviewed by [PEER] (CC me) and checked-in. Build and push the Docker image. 
    1. Bonus points if you can find bugs in the Matcher code!
3. Add yourself as an email contact for Cropping DAG, get it reviewed by [PEER]  (CC me) , and push the new configuration.
4. Go through all Onboarding training [Done].
    1. For each training, improve our documentation in the [Wiki]()
5. Hiring: Shadow one interview and provide notes on the candidate. [Done]
6. 1:1s: set up 30 minute 1:1s with the following people (whom you might not meet in Onboarding) [Done]
    1. [PEER]: leads the Web team
    1. [PEER]: building the Simulator for our Matcher


# Week 2: Starter Project



1. Set up our Airflow checkpointing system for **Cropping **and **Annotation**.
    1. Every stage in Airflow currently outputs metadata in log files or CSV files, as well as outputs used in the next stage (e.g. cropped OBJ files). Currently, accessing this data requires looking in S3 for the right files and then processing them; this makes it difficult for the next stage in the pipeline to be re-run with different configurations (e.g. only process crops with X points in them) or to do simple statistics on our pipeline (e.g. what % of objects with > 4096 point are marked INSTALLED by our pipeline but NOT_INSTALLED by human annotators?). \
 \
Proposal: each stage should have a SQL table in which it dumps its metadata. This metadata should be easily joinable with other metadata from the same run and our global object database.  \
 \
Please work with **[PEER]** and **[PEER]** to understand what metadata should be emitted from cropping and implement this piece. Also, work with **Ebot** on how to tie this into the **Matcher** checkpointing. 

        [Came up with a big project proposal and now the implementation will start]

2. Start researching cropping parallelization. Put together a proposal on how we can bring cropping down to &lt;10 minutes across ~100K objects. 
    1. Work with **[PEER]** who will be doing the same thing for Matcher. We should re-use similar technologies/frameworks across our systems.
    3. Email it to [REDACTED]

	[[EMPLOYEE]] Started making the python stuff parallel and working with ebot on refactoring the code and making it more modular which will help us in taking the common libraries out and use those in all the components.



3. Code Reviews: start reviewing all cropping PRs.
4. Hiring: Shadow one interview and provide notes on the candidate. [Done]
5. 1:1s: set up 30 minute 1:1s with the following people [Done]
    1. [COFOUNDER]: get to know his vision for the technology and product.
    5. Shrikant: get to know his views on the product and design.
    6. Matt: understand how customers see what we are building.


# Week 3-4: Speed Up Cropping



1. Based on your analysis in Week 2, bring cropping time down to &lt;10 minutes for all objects in a BIM model.
    1. Today, we are guessing what objects **might be installed** and only cropping those. These will likely be bad guesses and it should be safer to just crop everything for every scan - assuming it’s fast enough and cheap enough.
2. Code Reviews: start reviewing all C++ PRs (alignment, matcher in particular).
3. Hiring: lead one interview with [MANAGER] shadowing. [Done]
4. Write up a 4-week summary of [COMPANY] engineering (technical and non-technical). Email it to [REDACTED] for comments.
    1. What are we doing well?
    3. What should we improve?
