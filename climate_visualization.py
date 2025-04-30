import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"C:\Users\yadav\Downloads\climate_change_upto_2000_1.csv")



df.columns = ['Station_Name', 'Month', 'Period', 'No_of_Years',
              'Mean_Temp_Max', 'Mean_Temp_Min', 'Mean_Rainfall_mm']



# Define Month Order
monthly_order = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
df['Month'] = pd.Categorical(df['Month'], categories=monthly_order, ordered=True)



# 1. Line Plot - Temperature Trend for a Station
station = "Abu"
df_station = df[df["Station_Name"] == station].sort_values("Month")
plt.figure(figsize=(10, 5))
plt.plot(df_station["Month"], df_station["Mean_Temp_Max"], label="Max Temp (°C)", marker="o")
plt.plot(df_station["Month"], df_station["Mean_Temp_Min"], label="Min Temp (°C)", marker="s")
plt.title(f"Monthly Temperature Trends - {station}")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# 2. Bar Plot - Rainfall for a Station
plt.figure(figsize=(10, 5))
sns.barplot(data=df_station, x="Month", y="Mean_Rainfall_mm", palette="Blues_d")
plt.title(f"Monthly Rainfall - {station}")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 3. Heatmap - Avg Max Temp per Station per Month
pivot_temp = df.pivot_table(index="Station_Name", columns="Month", values="Mean_Temp_Max", aggfunc="mean")
pivot_temp = pivot_temp[monthly_order]
plt.figure(figsize=(14, 8))
sns.heatmap(pivot_temp, cmap="YlOrRd", linewidths=0.5, linecolor='gray')
plt.title("Avg Max Temperature per Station per Month")
plt.xlabel("Month")
plt.ylabel("Station")
plt.tight_layout()
plt.show()




# 4. Boxplot - Max Temps across Stations
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x="Station_Name", y="Mean_Temp_Max")
plt.xticks(rotation=90)
plt.title("Max Temperature Distribution by Station")
plt.tight_layout()
plt.show()






# 6. Histogram - Rainfall Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Mean_Rainfall_mm", bins=30, kde=True, color='skyblue')
plt.title("Distribution of Mean Rainfall")
plt.xlabel("Rainfall (mm)")
plt.tight_layout()
plt.show()



# 7. Violin Plot - Min Temp by Month
plt.figure(figsize=(14, 6))
sns.violinplot(data=df, x="Month", y="Mean_Temp_Min", palette="Set2", inner="quartile")
plt.title("Monthly Min Temperature Distribution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# 8. Pairplot - Temp and Rainfall
sample_df = df.sample(n=300, random_state=42) if len(df) > 300 else df
sns.pairplot(sample_df[["Mean_Temp_Max", "Mean_Temp_Min", "Mean_Rainfall_mm"]])
plt.suptitle("Temperature & Rainfall Pairplot", y=1.02)
plt.show()



# 9. Line Plot - Rainfall Comparison for Top 3 Stations
top3 = df["Station_Name"].unique()[:3]
plt.figure(figsize=(12, 6))
for name in top3:
    data = df[df["Station_Name"] == name].sort_values("Month")
    plt.plot(data["Month"], data["Mean_Rainfall_mm"], marker='o', label=name)
plt.title("Rainfall Trends Comparison (3 Stations)")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. Grouped Bar Chart - Avg Max & Min Temp for Top 5 Stations

top5 = df["Station_Name"].value_counts().head(5).index
df_top5 = df[df["Station_Name"].isin(top5)]
avg_temp = df_top5.groupby("Station_Name")[["Mean_Temp_Max", "Mean_Temp_Min"]].mean().reset_index()
avg_temp_melt = avg_temp.melt(id_vars="Station_Name", var_name="Type", value_name="Temp")
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_temp_melt, x="Station_Name", y="Temp", hue="Type")
plt.title("Avg Max & Min Temp - Top 5 Stations")
plt.xlabel("Station")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.show()
