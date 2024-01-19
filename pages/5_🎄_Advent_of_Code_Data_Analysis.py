# Third party imports
import streamlit as st
import pandas as pd

# Local imports
import st_utils

# Paths
DATA_PATH = 'data/advent_of_code/'
TITLE_IMG_PATH = 'data/advent_of_code/aoc_title1.png'


st.set_page_config(page_title="Advent-of-Code-Data-Analysis", page_icon="🎄", layout="wide")
st.markdown(f'<style>{open("style.css").read()}</style>', unsafe_allow_html=True)



# Table of Contents
st.sidebar.markdown("""
    # Contents
    1. [Introduction](#intro)
    2. [Data Collection](#data-collection)
    3. [Puzzle Completions](#puzzle-completions)
    4. [Submission Times](#submission-times)
    5. [User Stats](#user-stats)
    6. [Final Thoughts](#final-thoughts)
""")
st.sidebar.divider()
st_utils.get_sidebar_links()


st.title('Advent of Code Data Analysis')
st.caption('Collecting and analyzing [Advent of Code](https://adventofcode.com) public stats 2015-2023')

st.image(TITLE_IMG_PATH, caption='Image created with DALL·E')

st.markdown('<a name="intro"></a>', unsafe_allow_html=True)
st.write('## Introduction')
st.write('''
If you're not familiar with Advent of Code, here's a quick description from their [website](https://adventofcode.com):
> *Advent of Code is an annual Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.*

I'm a huge fan of these puzzles and the incredibly supportive community of people that grew around it. They helped me learn a ton about problem solving, data parsing, data structures & algorithms, how and when to use various python libraries, how to write clean & pythonic code and much more.
After having solved hundreds of these puzzles I decided to embark on the passion project of building [my own website](https://aoc-puzzle-solver.streamlit.app/) devoted to AoC, where visitors can get tips about how to approach each puzzle, interactively engage with my puzzle solutions using their own puzzle input, decipher ascii letter grids and more.
Since I'm always looking to improve my data analysis skills, I thought it would be nice to explore any available public data about these puzzles and the community of people who compete at each annual event, so I made it into a data analysis/visualzation project.
There are 3 main aspects to this project:   
1. **Data Collection:** I collected and compiled the data for this project myself.
2. **Data Visualization:** Most of my time was spent deepening my understanding of how to create a diverse set of visually appealing and insightful plots.
3. **Data Storytelling:** My hope is that my graphs and the way I sorted them into the categories of *completions*, *submissions* and *users* communicate a coherent story about the current state and history of advent of code. Wherever I felt appropriate, I added some texts which contextualize the plots and/or add further information.
''')



st.divider()
st.markdown('<a name="data-collection"></a>', unsafe_allow_html=True)
st.write('## Data Collection')
st.write('''
- **Scraping the Data:** 
    - Using python's native `urllib.request` library together with `BeautifulSoup`, I scraped the data directly from the original website
    - This amounted to a total of 459 requests (225 *Puzzle* pages + 225 *Leaderboard* pages + 9 *Stats* pages)
    - I'm ashamed to admit that I only discovered Advent of Code's officially stated [guidelines](https://old.reddit.com/r/adventofcode/wiki/faqs/automation/) afterwards and I promise, that if I collect any of their data again, I will do so in the heavily throttled fashion they request. While I'm still learning about such best practices, I should have intuited that a single person sending 225 requests within a few minutes can pose a challenge for the servers and I apologize.
- **Compiling the Data:**
    - Technically it's possible to keep all the data in a single table, but it makes sense to retain two distinct tables: *completions* & *leaderboard*
    - *Completions* has 225 rows, each representing a single puzzle (25 days for each of the 9 years)
    - *Leaderboard* has 45,000 rows, each representing a single submission (100 submissions for each of the 2 parts of each of the 225 puzzles)
    - I kept both csv files very lean, avoiding redundance. For example *leaderboard* has a single *timestamp* column specifying the year & day of the puzzle as well as the time of the submission. When loading the data, it is recommended to unpack these variables.
    - It's not necessary to update *leaderboard* more than once a year, since the data, once uploaded, is unchanging
    - On the other hand, the columns *gold* and *silver* in *completions* change every time anybody completes a new puzzle – I might update it every couple of months or so
- **Uploading the Data to Kaggle:**
    - I made the dataset publicly available on [kaggle](https://www.kaggle.com/datasets/michaeltezak/advent-of-code-public-stats)
    - One can also find the [kaggle notebook](https://www.kaggle.com/code/michaeltezak/visualizing-advent-of-code-stats) which I used to create all the plots
    - Anyone is welcome to copy & edit it, to create their own visualizations
''')

st.write('**Leaderboard Dataframe (unpacked):**')
st.dataframe(pd.read_csv(DATA_PATH + 'leaderboard_head.csv'))
st.write('**Completions Dataframe (unpacked):**')
st.dataframe(pd.read_csv(DATA_PATH + 'completions_head.csv'))



st.divider()
st.markdown('<a name="puzzle-completions"></a>', unsafe_allow_html=True)
st.write('## Puzzle Completions')
st.write('''
    - Last update: 2024-01-08
    - 19,016,811 stars have been attained on Advent of Code in total
    - 9,978,376 part 1 completions
    - 9,038,435 part 2 completions
''')
st.image(DATA_PATH + 'completion_plot.png')
st.write('''
    - Puzzle completions decrease per day as puzzles get harder
    - Puzzle completions increase per year, although 2015 and 2023 currently break this trend
    - The relatively low completions of 2023 can be explained by the recency of the event
    - The relatively high completions of 2015 can probably be explained in two ways:
        1. people are curious to see how it all started
        2. people are planning to do all of the years in chronological order, but haven't gotten very far yet 
    - There is a significant jump from 2019 to 2020 where completions double – I wonder if this can partially be explained by the Covid lockdowns (although they happened in 2020 before the event, so maybe not) 
''')
st.image(DATA_PATH + 'completion_plot_2.png')



st.divider()
st.markdown('<a name="submission-times"></a>', unsafe_allow_html=True)
st.write('## Submission Times')
st.write('''
    - On average the first leaderboard entry occurs around 7 minutes for part 2 (4 minutes for part 1)
    - On average it takes a bit less than 30 minutes for the leaderboard to fill up for part 2 (16 minutes for part 1)
    - However, these numbers vary strongly across the 25 days
    - Day 22 has the highest mean submission time: 46 minutes (part 2)
    - The longest it ever took to fill up the leaderboard was day 19, 2015: 3 hours and 52 minutes
    - There are 3 leaderboard entries under 20 seconds (*highly sus if you ask me...*):
        1. 2022–3–1: 10 seconds by ostwilkens 
        2. 2023–1–1: 12 seconds by (anonymous user #640116)
        3. 2022–4–1: 16 seconds by max-sixty
''')    
st.image(DATA_PATH + 'submission_times_plot.png')



st.divider()
st.markdown('<a name="user-stats"></a>', unsafe_allow_html=True)
st.write('## User Stats')
st.write('''
    - 5,460 users in total on the leaderboard
    - Somewhat significant but weak positive correlation between having a high number of total accumulated points and being a supporter
    - Much weaker (perhaps insignificant) correlations between one's points and being a sponsor (pos) or participating anonymously (neg)
    - For the last two years there have been just as many old users on the leaderboard as new users 
''')  
st.image(DATA_PATH + 'user_info_plot.png')
st.write('''
    *Anonymity*
    - Anonymous AoC'ers are almost equally as likely to have high performances and be financially supportive
    - 5 among the top 100 AoC-ers are anonymous, which is only slightly subproportional (they represent 7.8% of the total leaderboard)
    - The highest annual score ever achieved was by an anonymous user
    - Why be anonymous? Perhaps they don't seek fame at all and are just in it for the love of the game. Perhaps they don't want their bosses finding out, what they spend much of their productive energy on :-P
''') 
st.image(DATA_PATH + 'top10_annual_plot.png')
st.image(DATA_PATH + 'top100_accumulated_plot.png')
st.write('''
    *All-Time MVPs*
    - For most of AoC's history, **Robert Xiao** has been at the top in terms of total annually accumulated points
    - However, **betaveros** has had a very steep rise from 2017 till 2022 and if his trajectory had continued into 2023, he'd be #1 right now
    - Everybody in the the top 10 has been competing since 2017 at least
''')
st.image(DATA_PATH + 'top10_accumulated_plot.png')



st.divider()
st.markdown('<a name="final-thoughts"></a>', unsafe_allow_html=True)
st.write('## Final Thoughts')
st.write('''
    - I'm quite happy with this project overall, I love Advent of Code and I love exploring data, so this was a lot of fun
    - However, using only the data that AoC publishes on their website, it was somewhat limited in its scope
    - It could be interesting to gain an insight into more than the 100 top ranked competitors of each puzzle, or to get information about the competitors' timezones and to what degree it correlates with their performance
    - Another interesting avenue to explore perhaps in the future, is the public data on the [AoC subreddit](https://www.reddit.com/r/adventofcode/): For example I could find out how many people upvote a specific puzzle's solutions thread or participate in posting their own solutions and which programming languages are being used
''')