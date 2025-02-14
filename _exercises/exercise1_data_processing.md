# Exercise 1 - Data processing repetition

In this exercise sheet, you will get repetition of data processing using pandas and graphing.

> [!NOTE]
> These exercises covers lecture 02.

## 0. Supahcoolsoft employee data

In a company `Supahcoolsoft`, there are a lot of employees within data fields.

> [!NOTE]
> This is a synthetic dataset generated by GPT-4o, so the information does not reflect reality.

Read this dataset from the data directory and

&nbsp; a) Do some initial EDA on this dataset. For example checking null values, look at some statistical properties.

&nbsp; b) See if there are some null values that you can fill in based on your domain knowledge within the data field.

&nbsp; c) Find out some statistical information about the salary, e.g. mean, median, min, max, 10 percentile and 90 percentile.

&nbsp; d) Group by different roles and take the median and average salaries for each group.

&nbsp; e) Group by different departments and take the median and average salaries for each group.

&nbsp; f) Graph different data engineers salary. There are many approaches to graph this, try different and reason about pros and cons of each you choose.

&nbsp; g) You are getting interview to this company as a junior data analyst, and you have this dataset. Find out some statistical information about that role and similar role to make a case on what salary you should have.

&nbsp; h) Do some additional analysis of your choice.

## 1. Olympic games in Paris 2024

Here is the [wikipedia page for olympic games in paris 2024](https://en.wikipedia.org/wiki/2024_Summer_Olympics). We will use it for some data analysis. We'll use pandas `pd.read_html()` to scrape different tables in this site.

&nbsp; a) How many sports are represented in total?

For b,c,d it's good to make functions that can be reused.

&nbsp; b) Make a bar chart over the top five countries in medal count.

&nbsp; c) Make a bar chart over the top five countries in gold medal count.

&nbsp; d) Choose a sport from and and make a bar chart over top five countries.

Note that there are several tables that need to be considered for these tasks and some data cleaning are required.

&nbsp; e) How many venues are there in total?

&nbsp; f) How many venues were built for the games?

&nbsp; g) How much capacity does this correspond to?

&nbsp; h) How much percentage of capacity does this correspond to in total?

## 2. Working with livsmedelsverkets API

Livsmedelsverket provides an open API for accessing data on different food and their nutritional contents and more. Access the [documentation of this API here](https://dataportal.livsmedelsverket.se/livsmedel/swagger/index.html).

&nbsp; a) Go into different sections and click `Try it out` to try out the API, and you'll get the request URL links.

&nbsp; b) Now go into this endpoint `/api/v{version}/livsmedel/{nummer}` and try it out to find its request URL.

&nbsp; c) Use requests in python to try out this API endpoint and request a few data points.

&nbsp; d) Now find a number and find and print out its corresponding nutrient values. Example for number 10. Filter out all nutrients that are 0. 

```
Namn
Flytande margarin fett 82% berikad typ Milda culinesse

Näringsvärden
Vitamin E                               23.7mg
Vitamin D                               7.5µg
Vitamin A                               693.1RE/µg
Vatten                                  16.7g
Retinol                                 645.0µg
Summa fleromättade fettsyror            28.7g
Salt, NaCl                              1.5g
Natrium, Na                             600mg
Summa enkelomättade fettsyror           42.5g
Summa mättade fettsyror                 7.3g
Fett, totalt                            82.0g
Energi (kJ)                             3034kJ
Energi (kcal)                           725kcal
Arakidinsyra C20:0                      0.6g
Linolensyra C18:3                       8.8g
Linolsyra C18:2                         19.8g
Oljesyra C18:1                          41.0g
Stearinsyra C18:0                       2.1g
Palmitoljesyra C16:1                    0.2g
Palmitinsyra C16:0                      3.6g
Myristinsyra C14:0                      0.1g
Betakaroten/β-Karoten                   577µg
Aska                                    1.3g
```

This requires some more steps, but can be fun to explore. 

&nbsp; e) Make a dictionary of names as key and number as value. Then implement embeddings that finds closest distance between two strings. Now you can search for a specific food and find the closest one in your dictionary. Use the value that is a number and search for its corresponding nutrients. 

## 3. Theory questions

These study questions are good to get an overview of how snowflake works.

&nbsp; a) When should you use median over mean in statistics?

&nbsp; b) Salary for 90th percentile is 40000, what does this mean?

&nbsp; c) What are the main data structures used in pandas, and what are their primary use cases?

&nbsp; d) How does a pandas Series differ from a DataFrame, and when would you choose to use each?

&nbsp; e) Describe the various ways to select and filter data in a pandas DataFrame. How do these methods differ?

&nbsp; f) What are the differences between .loc[], .iloc[]? When should each be used?

&nbsp; g) How can you transform data in a pandas DataFrame using apply(), map(), and applymap()? What are the differences between these methods?

&nbsp; h) Why should you in general not loop through a dataframe? What can you do instead?

&nbsp; i) What type of ways are there to create dataframes in pandas?

## Glossary

Fill in this table either by copying this into your own markdown file or copy it into a spreadsheet if you feel that is easier to work with.

| terminology    | explanation |
| -------------- | ----------- |
| series         |             |
| dataframe      |             |
| concatenation  |             |
| join           |             |
| merge          |             |
| synthetic data |             |
| API            |             |
| clutter        |             |
| endpoint       |             |
| get request    |             |
| response       |             |
| json           |             |
| REST           |             |
| payload        |             |
| imputation     |             |
| aggregation    |             |
| data cleaning  |             |
| EDA            |             |
| outliers       |             |
| index (pandas) |             |
|                |             |
