import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset
df = pd.read_excel("Air_Quality_Data.xlsx")

#Basic information
print("Dataset Overview:")
print(df.info())

#Missing values - check 
print("\nMissing Values:")
print(df.isnull().sum())

#Summary statistics
summary_stats = df.describe()
print("\nSummary Statistics:")
print(summary_stats)

#Average pollutant levels by city
location_avg = df.groupby("Location")[["CO2 (ppm)", "NO2 (ppb)", "PM2.5 (µg/m³)", "AQI"]].mean()
print("\nAverage Pollutant Levels by City:")
print(location_avg)

#Bar chart average pollutant levels
plt.figure(figsize=(10,6))
location_avg.plot(kind='bar', figsize=(10,5))
plt.title("Average Pollutant Levels by City")
plt.ylabel("Concentration")
plt.xticks(rotation=45)
plt.legend(title="Pollutants")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()  

#AQI
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x="Date", y="AQI", hue="Location", marker='o')
plt.title("AQI over 30 days")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.legend(title="City")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() 

#HouseKeeping
cleaned_file = "Cleaned_Air_Quality_Data.xlsx"
df.to_excel(cleaned_file, index=False)
print(f"Cleaned dataset saved as {cleaned_file}")