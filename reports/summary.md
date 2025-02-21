This project explored historical international rugby union match results over various eras, from the sport’s early years in the 19th century up to the modern professional era. The main focus was on how scoring has evolved over time and whether that evolution indicates more “exciting” and attack-oriented rugby.

Overall, this project provided an entertaining (poor Italy 🇮🇹) and informative look into how rugby has changed over time. While limited by the available data, it highlights some interesting patterns, particularly the game’s increasing propensity for higher scores and larger winning margins.

I also gave me a fun opportunity to apply some of the basic data analysis skills I learned in the [Python for Data Science](https://www.codecademy.com/learn/getting-started-with-python-for-data-science) Codeacademy course. While the analysis is by no means optimised, it was a great learning opportunity.

## Data Overview
The original csv included match results (home/away scores, teams, match dates, etc.) from 1871 to the 2024.

I created and used some extra columns, specfically:
1. **year**: Extracted from the date column to allow era-based filtering
2. **score_difference**: home_score - away_score
3. **total_points**: Sum of home and away scores

## Approach
 - I grouped the data into distinct eras based on significant rule changes to rugby scoring (e.g., the introduction of points for tries, changes in the value of penalties, tries, and drop goals).

 - I calculated mean total points and mean score difference per era and observed how these metrics changed from the 19th-century rules (when tries were worth 0 or 1 point) to the modern era (tries worth 5 points).

 - I defined an “exciting” match or era by combining high total points with a close score difference

 - I compared the percentage of matches within each era meeting those criteria.

## Key Findings 
### Points per game:
In the earliest recorded matches (pre-1890s), total points per game averaged around 1–2. By the modern era (1992–2024), average total points rose to nearly 46. This trend indicates that changes in scoring rules (and possibly in playing style, professionalism, and fitness) have collectively made rugby more high-scoring over time

### Score differentials:
The mean margin of victory also gradually increased from near 0.4 in the late 1800s to about 4 in the modern era.
While higher-scoring matches can be more entertaining, a larger margin **might** indicate less balance between teams.

### Era-by-era:
 - **1905–1948:** Notable because it combined an increase in total points with a dip in average score difference, suggesting some relatively competitive, higher-scoring games.

 - **1971–1992 vs. 1992–2024:** Both eras have similar margins (~4 points), but the modern era’s total points are much higher (~46 vs. ~32).

 - **Close but High-Scoring Games:** A small percentage (under 2%) in the modern era combined very tight score margins (±4 points) and above-average scoring totals.

### Home vs away trends
 - Certain teams (e.g., New Zealand, South Africa) show consistently higher average score differences at home, highlighting their historical dominance on home soil.

 - Italy often features in very high-scoring home matches but, unfortunately, suffers large defeats, inflating total points while skewing average margins. This probably wouldn't be particulalrly exciting to watch.

## Authors notes:
 **Defining “Excitement”:** Using just total points and final score difference is simplistic; many factors (defensive quality, penalty frequency, weather, etc.) affect the feel of a match. Still, these metrics can give a broad idea of how open or competitive a game might have been.

## Next Steps:
 - **Visualisation:** Plot the evolution of total points and score difference by year or by era to get a clearer picture of trends.

 - **Team-Level Analysis:** Expand the “exciting” definition to find which teams (home or away) most often take part in close, high-scoring matches.