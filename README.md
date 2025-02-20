# 📝 Data Science Learning Project: Rugby Union Internationals (1871 - 2024)

## 📖 About This Project

This is an **ongoing project** that is part of my learning journey in Python for Data Science, which I recently completed on Codecademy.

Right now, I’m focusing on:

 - **Importing** and **modifying** CSV files 📂
 - **Cleaning** and **analysing** data using pandas and NumPy 🧼🔍

Later, I’ll add data visualisations using Seaborn and Matplotlib after completing the Data Visualisation 📊 course on Codecademy.

## 🏉 Some History 

*In the original game of rugby, no points were given for scoring a try!*

In modern rugby (since 1992), a try is worth five points, and a successful conversion is worth two points. 

In the early days of rugby, the only way to score points was by kicking a goal (equivalent two one point) after a try. 

The scoring system for rugby has gradually changed, with the aim of:
1. encouraging **more attacking play**
2. making the game **more exciting**. 

**Early Scoring System (Pre-1890s)**
 - A team could only win a match if they successfully kicked a goal, either from a try or a drop goal.
 - If no goals were scored, tries were used as a tiebreaker.

**Introduction of Points for Tries (1890s)**
 - The Rugby Football Union (RFU) introduced a points system where tries and goals had different values.
 - This change placed more emphasis on try-scoring rather than just kicking.
 - **_1891:_** A try was worth 1 point, a conversion 2 points, a penalty goal 3 points, and a drop goal 4 points.

**Standardisation and Adjustments (1890s–1950s)**
 - The value of a try steadily increased to encourage attacking play.
 - **_1905:_** A try increased to 3 points.
 - **_1948:_** A penalty try (awarded for a foul that prevents a certain try) was introduced.
 - **_1948:_** Drop goals were reduced from 4 points to 3 points, to ensure they didn’t outweigh tries.

**Modernisation and More Try-Focused Scoring (1960s–1990s)**
 - **_1971:_** A try increased to 4 points to reward attacking rugby.
 - **_1992:_** A try increased to 5 points, which remains the standard today.

**Current Scoring System (Since 1992)**
 - Try = 5 points
 - Conversion = 2 points
 - Penalty goal = 3 points
 - Drop goal = 3 points
 - Penalty try = 7 points (since 2017, no conversion needed)

## 🎯 Project goal

**"To investigate whether the scoring system changes have made the game of rugby more exciting by encouraging more attacking play."**

My initial thoughts were to split the data into different playing "eras" and compare the average number of tries per game, with a higher number of tries per game indicating a greater level of excitement. Unfortunately the dataset I am using does not have the number of tries for each game (only the home and away team scores).

I have decided to analyse attacking trends over time using **total points per game** as an indicator of how attacking the game has become.

There are several key limitations to this approach, but I will discuss those more in the project summary (and this project is just for fun so...why be so serious 🤷)

### Other interesting questions:
1. Which team has won the most matches since records began? Does the same team have the highest win rate?
2. Which team(s) have the highest home/away/neutral win rates?
3. Which teams have the highest points differential across time?
4. What are the average number of points scores per game for each stadium?
5. How do different teams' win rates change over time and which is the most improved team?

## 📂 Project Structure

```markdown
📁 my_data_project/
│
├── 📁 data/                    # Where I will store my CSV files
│   ├── results.csv
│
├── 📁 notebooks/               # Where I will store my Jupyter notebooks for analysis
│   ├── data_cleaning.ipynb
│   ├── data_analysis.ipynb
│
├── 📁 scripts/                 # Where I will create and store Python scripts for reusable functions
│   ├── example_scriptfile.py   # Scripts to analyse/summarise/format data
│
├── 📁 reports/                 # Where I will save any exported charts or summaries
│   ├── summary.txt
│   ├── charts.png
│
├── .gitignore                
├── requirements.txt          
├── README.md                 👋 You are reading me right now! 👋
```

## 🚀 Getting Started

### **1️⃣ Install Required Packages** 

You need Python and the following libraries:

```bash
  pip install pandas NumPy jupyter matplotlib seaborn
```
### **2️⃣ Open the Jupyter Notebook**

Open the notebooks/ folder and start exploring the data!

## 🛠 Features I am currently working on...

- Load and clean CSV files with pandas
- Basic data analysis (mean, median, missing values, etc.)
- Filtering and modifying datasets

## 🔜 Coming Soon:

- Data visualisations using Matplotlib & Seaborn
- Insights from real-world datasets

## 📌 Learning Resources

[Python for Data Science – Codecademy](https://www.codecademy.com/learn/getting-started-with-python-for-data-science)

[Pandas Documentation](https://pandas.pydata.org/docs/)

[Matplotlib Documentation](https://matplotlib.org/stable/index.html) _(not used yet)_

[Seaborn Documentation](https://matplotlib.org/stable/index.html) _(not used yet)_

## 🤝 Contributing

This project is just for my learning, but if you have suggestions, feel free to open an issue!

## 📜 License

This project is for educational purposes only.

