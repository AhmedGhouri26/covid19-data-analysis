# COVID-19 Data Analysis - Top 10 Countries by Confirmed Cases

import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('covid_19_data.csv')
df.rename(columns={'ObservationDate': 'Date', 'Country/Region': 'Country'}, inplace=True)

# Group and sort
top_countries = df.groupby('Country')['Confirmed'].sum().sort_values(ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 6))
top_countries.plot(kind='bar', color='coral')
plt.title('Top 10 Countries by Total Confirmed COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Confirmed Cases')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('top_10_countries.png')  # Save image
plt.show()
