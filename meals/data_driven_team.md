## Factory Annotation Q1 Update


### Aka a recipe for a data-driven decision making process to minimize wasted effort


## Outline
Presentation was here: https://docs.google.com/presentation/d/1IlVmGTL_nCGwWJRD0rP3ey6YSq8cKxd8zIqylekB4DU/edit#slide=id.g22295f532a0_0_155



1. Reminder: Why FA?
    1. (ask the audience?)
2. What was the State of FA in January?
    3. Several months of “Code complete” but…
    4. Very low usage in production, but unclear why
    5. Pushback that it was “too expensive”
    6. Engineering felt lost about what we needed to do next. 
        1. Should we focus on making it “cheaper”, despite nobody using it?
        2. Should we focus on improving precision or recall, e.g. with “last week” view?
        3. Should we focus on ML to automate the work away?
        4. Should we focus on encouraging the Ops team to just use the tools more? 
        5. Should we **force **the Ops team to just use the tools more?
3. What is the state of FA today?
    7. % of work going to prod
    8. precision/recall
    9. Efficiency
4. When is it the right time for a data-first approach
    11. Data Analysis is VERY expensive… if you do it too early you are wasting time. 
    12. But if you do it too late, you will waste time on problems that are NOT actually high ROI.
    13. Rule of thumb: if you are confused about what is _the most important_ thing to do, and talking to people/looking at code doesn’t give a good answer, you should probably look at the data
5. How do you do a data-first approach?
    14. Start with the questions you want to answer
        6. Most people start bottoms-up: “here is some data, let me create a dashboard or report around it.”
        7. I start top-down: “what is the goal I’m trying to accomplish? What data do I need to know if I’m accomplishing that goal or not?”
    15. Once you have the question, figure out how to get the data you need.
        8. Build V1 of the **final tables** you will want.
            1. Add an example here of a finished table.
        9. Reverse engineer the existing data to figure out what you actually have available.
            2. This is hard… Need more here. 
            3. E.g. we currently have 1000s of lines of SQL reverse engineering our existing system.
        10. Figure out what you are missing, and go write code to add that in.
            4. Example: we are not tracking how often people press the “start capture” button on the mobile app. So we can’t really measure how often captures are failing.
        11. Debug it with **spot checks** - find interesting tidbits in the data and go figure out why they don’t match your intuition or expectations.
            5. E.g. average # of human views is low - we expect 2, but have 1, why?
                1. Bug: it turns out we are counting XX as a human. Oops.
            6. E.g. this should be impossible:
    16. Set goals now that you have a baseline!
        12. Defining the goal is hard. It’s OK if it’s not perfect; you will likely iterate on the goal anyhow so the important thing is _defining_ one so you can focus your exploration efforts.
    17. Once you have the question & the data, start running a regular loop
        13. A simple question every week: “why did we miss the goal?”
        14. This starts as a VERY difficult question to answer. Expect to spend a whole week on it the first few weeks.
            7. Ad-hoc queries, talking to people, reading the code…
            8. Start building an understanding of the _failure taxonomy_. 
        15. Iterate on the metrics + dashboards. This is where you start building drill-downs.
            9. E.g. subdivide the failures into different types of failures. 
                2. Show the recall graphs.
            10. Find _dimensions_ that help isolate the problems, and build them into your graphs or filters to make drilling down much faster.
        16. Expect this will take a lot of effort
            11. # of PRs that I submitted?
            12. # of weeks that we’ve been doing this?
        17. Once you’ve run the loop yourself a few times, it’s time to bring in the rest of the team. 
    18. Kick off the Metrics Weekly Review Process
        18. Why?
            13. You’ll need help from others (possibly) to answer the question.
            14. You’ll want others to feel ownership over the goals as well - no better way than having them spend time answering why they _missed_.
        19. “Start” meeting reviewing the goals that were missed. This should be very fast, since your dashboard should show that.
            15. Start at 1 hour, use the time to start drilling into the “why”. If people have opinions, write down those hypotheses and assign AIs to individuals to follow-up.
            16. Anytime you run into an “I don’t know?” that becomes an AI.
        20. “End” meeting, 2-3 days later. Follow-up on the AIs.
            17. Time-bound so people don’t spend **too much time** following up on AIs.
            18. Expect some AIs will NOT be complete. That’s probably OK; it means some work needs to happen to make followup much faster. Add it to your backlog.
            19. **Summarize** in writing so everyone agrees on the core problems + core AIs
        21. Weekly Summary Email
            20. Send this to **a wide audience**
                4. This helps keep you/your team accountable.
                5. This helps spread knowledge about how the project is going and what the top problems are.
                6. This helps train others to use the same process going forward.
            21. Keep it relatively short; for each goal, 1-3 Top Problems and 1-3 Top AIs.
                7. Call out the important differences from last week, especially if you are redefining the goals/found data bugs/etc.
    19. Don’t ever stop!
6. Tools 
    20. Use SQL, not Python!
        22. Fast to “ask new questions” (no code)
        23. Can re-run on historical data (usually) w/o having to wait for Airflow, etc.
        24. Built-in analysis tools: histograms, rollups/cubes (dimensionality), what else?
        25. Materialized Views
    21. Use Mode, not Retool
        26. Good support for dashboards, filters.
        27. Pretty easy for drill downs (but not the best).
        28. Lots of different graphs 
            22. Read that book!
            23. Picking graphs is not random; you need to have a good sense of what you are trying to _say _in the data.
                8. Even things like log axes, ticks, etc matter….
                9. Topic for another day.
7. Why is this hard for most people?
    22. No single thing I did was difficult.
    23. Combination is hard: 
        29. Super organized - process needs to run on-time.
        30. Good knowledge of the tools
        31. Good understanding of the goals.
        32. Comfortable with making people uncomfortable.
        33. Having an OK understanding of stats
        34. Having a good sense of data visualization