1. Which sub-questions of the central business question did you expect to be easy vs. hard, before building anything? ----> I expected measuring scheduled transport supply to be relatively easy using static data. However, identifying areas with insufficient transport compared to actual demand seemed harder because real ridership data is not publicly available. Detecting recurring delays also requires historical data collected over several weeks.

2.Your prediction for why the static GTFS feed doesn't also refresh every 15 minutes : Static GTFS data describes scheduled routes, stops and trips. It does not change every 15 minutes, so refreshing it that frequently would waste resources and create unnecessary downloads. A monthly refresh is more appropriate.

3.Your prediction for what breaks when two files' "same" ID column gets auto-typed independently and then joined :
The join may fail because one file stores IDs as integers while the other stores them as strings. This creates type mismatches, preventing matching records and potentially producing missing data. Reading all GTFS IDs as strings avoids this problem.

4.Order-of-magnitude row-count comparison: per-route vs. per-stop logging over a semester, and what question the per-route choice makes harder::

However, per-route aggregation makes it harder to identify which specific stops experience repeated delays.

5.Your proposed alternative to the delay chart's early-good/late-bad color encoding, and what decision it would change : i would use a symmetrical color scale based on the absolute delay from the scheduled time. Both significantly early and late services would appear red, while services close to schedule would appear green.
This would help identify routes with unreliable service in either direction, rather than considering early arrivals automatically good.

6.The real reasoning for both halves of the static-vs-real-time scheduling mismatch : Refreshing static GTFS every 15 minutes is unnecessary because schedules, routes and stops change infrequently. Conversely, collecting real-time data only once a month would miss daily disruptions and delay variations, making the dashboard outdated and unsuitable for monitoring the network.

7.What you actually found when you sanity-checked one delayed route against reality? I selected route C4, which showed an average delay of 272.5 seconds and a maximum delay of 780 seconds in my snapshot. I checked SETRAM's official information and found service information concerning this route. However, I could not independently confirm the specific 13-minute delay at the exact snapshot time


8.A concrete case where population would mislead as a demand proxy?
A commune with a small residential population but a large commercial area or major employer could generate high transport demand from commuters and visitors. Population alone would underestimate its actual transport needs.

9.Your chosen supply-vs-population metric, and a real commune where it misleads?I calculated scheduled stop level trip counts per 1,000 inhabitants by dividing the total daily trip counts at stops by the commune population and multiplying by 1,000.
La Chapelle-Saint-Aubin ranks first with 1,010.35, but this may overestimate actual accessibility because a small population and stops serving commercial or external passengers can produce a high ratio. The indicator does not measure accessibility for residents directly.

10.Your proposed approach to aggregating stop-level delay events without blowing up the history file. ?
I would aggregate stop level delays by stop id and time period, such as every hour/day. I would store the number of observations, average delay, maximum delay and number of skipped stops instead of logging every individual update. This would reduce storage while preserving useful information about recurring problems.

11.How your Reflection 1 predictions compared to what you actually found ?
My initial prediction was mostly correct. Static transport supply was relatively easy to calculate using GTFS data, while comparing supply with actual demand remained difficult because real ridership data was unavailable. I also found that interpreting delays and identifying misleading supply indicators required human judgment. Finally, identifying recurring patterns requires several weeks of historical snapshots.
