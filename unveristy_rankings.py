
import pandas as pd
import os

# Load your Excel file into a DataFrame
df = pd.read_excel(r'C:\Users\GLOBALLY HYKZE\Desktop\PYTHON\WEB SCRAPING\uni rankings.xlsx')

# Assuming you have already loaded your data into the 'df' DataFrame

# Create a DataFrame for 2023
count_2024 = df[df['year'] == 2024]['Universities'].nunique()

# Calculate the unique count difference for each year
unique_count_difference = {}
for year in range(2013, 2025):  # Includes 2013 to 2023
    if year == 2024:
        unique_count_difference[year] = count_2024
    else:
        count_per_year = df[df['year'] == year]['Universities'].nunique()
        unique_count_difference[year] = abs(count_per_year - count_2024)

# Convert the result to a DataFrame
result_df = pd.DataFrame(list(unique_count_difference.items()), columns=['year', 'Unique_Count_Difference'])

# Display the result
#print(result_df)


# Assuming 'result_df' contains the calculated unique count differences and 'df' is your original DataFrame

# Merge the 'Unique_Count_Difference' column into your original DataFrame 'df' based on the 'Year' column
df = pd.merge(df, result_df, on='year', how='left')

pd.set_option("display.max_rows",None)

# Display the updated DataFrame

df = df.to_excel("UNI_RANKING_UPDATE.xlsx", index=False)
print(f'the data saved to {df}')










