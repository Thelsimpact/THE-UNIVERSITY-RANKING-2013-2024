from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
import pandas as pd

# Load your Excel file into a DataFrame

df2 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2013_rankings.xlsx')
df3 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2014_rankings.xlsx')
df4 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2015_rankings.xlsx')
df5 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2016_rankings.xlsx')
df6 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2017_rankings.xlsx')
df7 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2018_rankings.xlsx')
df8 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2019_rankings.xlsx')
df9 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2020_rankings.xlsx')
df10= pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2021_rankings.xlsx')
df11 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2022_rankings.xlsx')
df12 = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Documents\TIC INTERNSHIP\the-world-university-rankings-2011-2023\UNIVERSITY RANKING\2023_rankings.xlsx')

# Define a function to convert country names to continents
def convert(row):
    try:
        # Convert the country name to country alpha-2 code
        country_alpha2 = country_name_to_country_alpha2(row['country'])
        
        # Convert the country alpha-2 code to continent code
        continent_code = country_alpha2_to_continent_code(country_alpha2)
        
        return continent_code
    except Exception as e:
        return "Unknown"  # Handle cases where conversion is not possible

# Apply the conversion function to the DataFrame and create a new 'continent' column
df12["continent"] = df12.apply(convert, axis=1)

# Print the updated DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#print(df)
# Set the option to display all rows
# Map continenet code to country name
continent_names = {
    "NA": "North America",
    "OC": "Oceania",
    "SA": "South America",
    "EU": "Europe",
    "AF": "Africa",
    "AS": "Asia",
    "AN": "Antarctica"
}

df12["continent"] = df12["continent"].map(continent_names)
#print(df)
#df2 = pd.DataFrame(df2)
#df3 = pd.DataFrame(df3)
#df4 = pd.DataFrame(df4)
#df5 = pd.DataFrame(df5)
#df6 = pd.DataFrame(df6)
#df7 = pd.DataFrame(df7)
#df8 = pd.DataFrame(df8)
#df9 = pd.DataFrame(df9)
#df10 = pd.DataFrame(df10)
#df11= pd.DataFrame(df11)
df12= pd.DataFrame(df12)

#df2.to_excel("2013_University_data.xlsx")
#df3.to_excel("2014_University_data.xlsx")
#df4.to_excel("2015_University_data.xlsx")
#df5.to_excel("2016_University_data.xlsx")
#df6.to_excel("2017_University_data.xlsx")
#df7.to_excel("2018_University_data.xlsx")
#df8.to_excel("2019_University_data.xlsx")
#df9.to_excel("2020_University_data.xlsx")
#df10.to_excel("2021_University_data.xlsx")
#df11.to_excel("2022_University_data.xlsx")
df12.to_excel("2023_University_data.xlsx")

print(df12)


