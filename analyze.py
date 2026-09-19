# Summary: Breakdown risk is driven by operational intensity (km_since_service, avg_daily_km, load_factor).
# Total odometer mileage and vehicle age have virtually zero correlation with breakdowns.

import pandas as pd

# 1. Load dataset
df = pd.read_csv("fleet_history.csv")

# 2. Compare broken down vs healthy vehicles
broken = df[df["broke_down"] == 1]
healthy = df[df["broke_down"] == 0]

print("=== Mean Comparison (Broken vs Healthy) ===")
numeric_cols = df.select_dtypes(include=["number"]).columns
for col in numeric_cols:
    if col != "broke_down":
        r = df[col].corr(df["broke_down"])
        print(f"{col:20s} | Broken: {broken[col].mean():.2f} | Healthy: {healthy[col].mean():.2f} | corr: {r:+.3f}")

# 3. Build a simple risk score (0 to 100) based on separating factors
k_norm = (df["km_since_service"] - df["km_since_service"].min()) / (df["km_since_service"].max() - df["km_since_service"].min())
d_norm = (df["avg_daily_km"] - df["avg_daily_km"].min()) / (df["avg_daily_km"].max() - df["avg_daily_km"].min())
l_norm = (df["load_factor"] - df["load_factor"].min()) / (df["load_factor"].max() - df["load_factor"].min())

df["risk_score"] = (0.50 * k_norm + 0.30 * d_norm + 0.20 * l_norm) * 100

# 4. Print the cars ranked by risk, highest first
ranked_cars = df.sort_values(by="risk_score", ascending=False)

print("\n=== Top 20 Riskiest Vehicles ===")
print(ranked_cars[["vehicle_id", "risk_score", "km_since_service", "avg_daily_km", "load_factor", "broke_down"]].head(20).to_string(index=False))
