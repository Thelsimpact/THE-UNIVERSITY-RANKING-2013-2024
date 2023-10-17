# Times_Higher_Education_Rankings 2013-2024

![THE](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/2048ee8b-8ebf-464a-810b-aaa4b34e3f34)


# INTRODUCTION

The Times Higher Education (THE) World University Ranking is one of the most comprehensive global rankings. 

By now, more than 1,500 universities worldwide have participated in this direct comparison, which is carried out on the basis of bibliometric analyses, surveys and statistical data.
In 2018, the University of Passau took part in these rankings for the first time and was found to be among the best 25 percent of universities worldwide. 
Since then, the University of Passau consistently maintained a steady position among the best 25 percent worldwide
Original data, as well as ranking methodology described per each year, is available on the official

website: www.timeshighereducation.com
It contains 24 columns and this columns are given into different workbook like this 

# DATA MODELLING 

Data modeling in Excel involves structuring your data to make it easier to analyze and visualize. It helps you create a more organized and efficient spreadsheet for tasks like data analysis, reporting, and creating charts or graphs.
So for easy analysis we had to append or concatenate this sheets into one workbook and 1 sheet

# DATA CLEANING

Special characters

We started by removing special Character using power query Feature #65001: Unicode (UTF-8)
This automatically removes any special characters and replaces them with the original characters

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/79575834-8c74-403e-9320-43a37693857e)

# NEXT 
We remove unnecessary columns 

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/b7b59c02-9515-4af2-a6e6-2a73a8102f66)

# NEXT 
We remove unnecessary Rows

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/c3a2fd09-b3d3-4f8f-9d10-6a99a8297c4a)

# NEXT 
To improve our analysis, we should include a "Continent" column in our dataset. This will allow us to align the continent information with the respective country, enhancing the quality of our analysis.

This was achieved using Python. To replicate this, please find the code file or employ the Excel formula shown below:

=VLOOKUP([@country], Table1[[country]:[continent]], 2)

A crucial point to remember is that this method is applicable when there is an existing table containing a 'continent' column, and you intend to populate another sheet or table with this 'continent' column. Also, make sure to sort the data in ascending order before applying the formula for accurate results.

 ![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/89353c2d-eda3-420c-8c83-b1812ef5b2c1)

# Next, we confirmed the absence of null or blank spaces. 

Subsequently, we introduced a "Total Number of Universities per Country" column, set to the year 2023, and included a "Year" column to facilitate straightforward analysis within the sheet.

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/9c205e7a-eff6-4bd9-940a-22428482ede7)

# Next, we delve into Africa-focused analysis using TABLEAU.

# 1.	Country With The Most Universities|THE Ranking 2024 ( Especially comparing Nigeria  with Africa) 

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/9fc71247-8e1f-4455-a456-59b629e0fa1b)

It's important to compare the country with the most universities, especially when comparing Nigeria with the rest of Africa, because it provides valuable insights into the state of higher education in the region. This comparison can help identify disparities in educational infrastructure, funding, and quality, highlight areas for improvement, and inform policymakers and educators about the challenges and opportunities in the African education landscape. 

Additionally, such comparisons can serve as a benchmark for gauging progress and setting future goals to enhance the educational sector in both Nigeria and the broader African context.

# 2.	Countries With Highest Change |THE Ranking2013-2024

This was done by creating a calculated field of from 2013 to 2024 with the tableau formular 

abs(countd(if [Year] = 2013 then [Universities] end) - countd( if [Year] = 2024 then [Universities] end))

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/8901cfcf-014a-4d6f-be31-703e56259443)
In simple terms, this calculation is trying to find the difference between the number of universities in the year 2013 and the number of universities in the year 2024. It counts how many universities existed in each of these two years and then calculates the absolute difference (ignoring whether it's positive or negative) to see how much the number of universities has changed over that time period.

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/78445341-2712-4461-8122-46c031c79294)

# 3.	Number of Unversity Over Time

 ![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/75263973-7b5f-4c2c-a76c-bffb4273c77e)

# 4.	Total Number of University Vs Ranked |THE RANKING 2023

We added the total Number of University column from List of All Universities in the World 2023 – AUBSP

Comparing the total number of universities with their respective rankings in THE RANKING 2023 is important because it provides valuable insights into the quality and competitiveness of higher education institutions. 

By correlating the number of universities with their rankings, we can assess the concentration of top-performing universities in relation to the overall quantity. 

This analysis helps us understand the global landscape of higher education and the distribution of prestigious institutions, shedding light on educational excellence and accessibility worldwide.
 
![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/ad9a5677-b646-459a-be28-2d574aabb6ec)

# 5.	We conducted a visualization project aimed at illustrating the development over time. 

Specifically, we created an interactive filter allowing us to select different years and view the corresponding developments. 

To achieve this, we developed a Python script that reads university ranking data from an Excel file, calculates the difference in the number of universities for each year compared to 2024, and then saves the updated data into a new Excel file.
You can find the Python code file for this data manipulation attached. 

It's important to note that this data preprocessing step is essential before we proceed to perform a more in-depth analysis in Tableau.

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/c0005eb8-6bdd-432a-ae3c-bb92469a8401)

Next we calculated  the percentage increase over-time by creating a calculaeted field  and a dynamic moving text by using the calculate fileld 

IF [Year] >= 2013 AND [Year] <= 2024 THEN
  "Development " + STR([Year]) + "-2024" + CHAR(10) +
  
  STR(ROUND([Percentage Growth2] * 100, 2)) + "% |▲" + STR([Unique Count Difference])
END

Having applied this the percentage was not properply formatted

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/300e77ab-3acc-47f4-8c65-0fcebd55ecb3)

So we had to write a different tableau script which is 

IF [Year] >= 2013 AND [Year] <= 2024 THEN

  "Development " + STR([Year]) + "-2024" + CHAR(10) + "▲"+
  
  STR(IIF([Percentage  Growth2] >= 1, ROUND([Percentage  Growth2], 0), ROUND([Percentage  Growth2], 2))) + "% |▲" + STR([Unique Count Difference])
  
END

This formula does a few things:

1. It checks if the value in the "Year" column is between 2013 and 2024.
   
3. If the year falls within that range, it creates a text string that says "Development [Year]-2024" (e.g., "Development 2019-2024").
   
5. It adds a line break (represented by CHAR(10)) to start a new line.

6. It adds a triangle symbol (▲) to indicate an increase.

7. It calculates the percentage growth (rounded to either 0 or 2 decimal places) from the "Percentage Growth2" column and appends it as a percentage (e.g., "▲5%").

8. It also adds a pipe symbol (|) and then appends the value from the "Unique Count Difference" column.

So, in simple terms, if the year is between 2013 and 2024, it creates a text string that describes development, shows whether it increased or decreased, and provides the percentage change and the unique count difference.

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/03138758-2130-447b-8591-3eafb7ff047e)

  
# 6.	Next we created an dynamic moving text for our header such that anytime we filter using year it tell us the particular year the workbook at.

IF [Year] >= 2013 AND [Year] <= 2024 THEN
  " " + STR([Year]) + "-2024" + CHAR(10) +
  
  STR(IIF([Percentage  Growth2] >= 1, ROUND([Percentage  Growth2], 0), ROUND([Percentage  Growth2], 2))) + STR([Unique Count Difference])
END

This formula does the following:

1. It checks if the value in the "Year" column is between 2013 and 2024 (inclusive).
  
3. If the year meets the condition, it creates a text string with the following components:

   - The year itself, like "2024."

   - A line break (represented by CHAR(10)) to move to the next line in a text display.

   - The percentage growth value, rounded to either a whole number or two decimal places, depending on whether it's greater than or equal to 1.

   - Finally, it adds the "Unique Count Difference" value to the text string.

So, in simpler terms, this formula generates a text that shows the year, the percentage growth (rounded to either a whole number or two decimal places), and the unique count difference, but only for years between 2013 and 2024.

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/fc9240d5-d3e6-444d-a9bc-04bfdeea48a6)
 
Now we have  ![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/57a731af-e118-492c-b609-402862d54ac9)


#7.	Number of Universities by Country 2024 on map

 ![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/0471d2ab-fa7f-4035-8c15-e065b3e81b1e)

#8.	Region and country text dynamics 

IF [Continent] != "All" AND [Country] = "All" THEN "Region: All, Land: All"

ELSEIF [Continent] = "All" THEN "Region: All, Land: " + [Country]

ELSEIF [Country] != "All" THEN "Region: " + [Continent] + ", Land: All"

ELSE "Region: " + [Continent] + ", Land: " + [Country]

END

This code helps create a clear description of the region and country you're analyzing based on your selections in a data visualization tool.
 
![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/1e09b814-cb18-4681-9e0c-136269c66588)

# 9.	The  complete dashboard(1) focusing on Africa

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/cd9634df-6cfe-4dc4-b500-ccd1fdd0f2a3)

# 10.	In this analysis, we are comparing two groups of countries: "Nigeria" and "Independence Countries from 1960 and earlier."

We are assessing these countries based on three criteria:

This represents the average overall score, where a lower score indicates better performance.

This is the count of universities in each group of countries.

Ratio of University Count to Overall-Score .

This ratio measures how many universities there are in relation to the overall score. A higher ratio suggests that there are more highly ranked universities relative to the overall score.

The goal is to analyze and compare these two groups based on these three criteria to gain insights into their educational systems and performance.
 
![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/27b31868-1142-4719-8875-a1810bb2f7a8)

In the provided chat link [https://public.tableau.com/app/profile/ikechukwu.osuya/viz/THEUNIVERSITYRANKINGS2/Dashboard2#guest=n](https://public.tableau.com/app/profile/ikechukwu.osuya/viz/THEUNIVERSITYRANKINGS2/Dashboard2#guest=n)
, you can find data on the university rankings for different countries:
1. Singapore:
   
   - Average overall score: 263

   - Number of universities ranked: 2

    - Ratio of overall score to the number of universities ranked: 0.76%

    - Year of independence: 1965

3. United Arab Emirates:
   
   - Average overall score: 4663

   - Number of universities ranked: 6

   - Ratio of overall score to the number of universities ranked: 0.13%

   - Year of independence: 1971

5. Nigeria:
   
   - Average overall score: 15503

   - Number of universities ranked: 15

   - Ratio of overall score to the number of universities ranked: 0.10%

   - Year of independence: 1960
     
In summary we can deduce that:

•	Singapore has the lowest average overall score (263), indicating a strong performance in university rankings with a relatively small number of universities ranked.

•	United Arab Emirates follows with a higher average overall score (4663), but it still performs well, considering the number of universities ranked.

•	Nigeria, while having the highest average overall score (15503), may be considered to have the most room for improvement in university rankings, given the higher score and a relatively larger number of universities ranked.

In this context, lower average overall scores are indeed better, and Singapore appears to have the strongest performance, while Nigeria may benefit from efforts to improve its universities' rankings. 

![image](https://github.com/Hykze1/Times_Higher_Education_Rankings/assets/100960483/a5f6e8ee-4584-4cf2-a933-4260834c9b5f)find

# You can find the Tableau Link of the dasboard here for easy interaction https://public.tableau.com/app/profile/ikechukwu.osuya/viz/THEUNIVERISYRANKINGS/Dashboard1



 

