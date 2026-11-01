import pandas as pd
import matplotlib.pyplot as plt

# Data for 6 wards
data = {
    "ward": [
        "ward 1", "ward 2", "ward 3", "ward 4", "ward 5", "ward 6"
    ],
    "population": [
        61661, 163702, 101612, 157573, 107934, 63686
    ],
    "area_km2": [
        5.2, 7.5, 3.5, 5.0, 3.2, 2.8
    ],
    "green_km2": [
        0.65, 0.45, 0.40, 0.55, 0.25, 0.30
    ]
}
df = pd.DataFrame(data)


# Add density (people per km2) and green share (% of ward area)
# Values keep full precision here; we round only when printing
def add_indicators(df):
    df['density'] = df['population'] / df['area_km2']
    df['green_share'] = (df['green_km2'] / df['area_km2']) * 100
    return df


# Calculate summary numbers for the whole table
def summarize(df):
    summary = {
        "total_population": df['population'].sum(),
        "mean_density": df['density'].mean(),
        "max_density": df['density'].max(),
        "mean_green_share": df['green_share'].mean(),
    }
    return summary


df = add_indicators(df)
print(df.round(1))   # round for display only


# Print the summary with a loop
summary = summarize(df)

for key, value in summary.items():
    if key == "total_population":
        print(f"{key}: {value:,}")      # whole number with commas
    else:
        print(f"{key}: {value:,.1f}")   # 1 decimal place


# Find the ward with the highest density
highest_density_index = df['density'].idxmax()
highest_density_ward = df.loc[highest_density_index, "ward"]
print(f"Highest density ward is: {highest_density_ward}")


# Bar chart of green share by ward (save BEFORE show)
plt.bar(df['ward'], df['green_share'], color='grey')
plt.title("Green Share by Ward")
plt.xlabel("Ward")
plt.ylabel("Green Share (%)")
plt.savefig("ward_summary_green_share.png")
plt.show()