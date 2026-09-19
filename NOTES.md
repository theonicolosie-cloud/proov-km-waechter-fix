# What I checked, and what the agent got wrong

Write this yourself, in your own words. It is the part of the repo that proves the work is yours.

## What the agent got wrong
The agent initially failed to handle edge cases in the fleet service report, including potential floor-division errors during wear percentage calculation and handling vehicles missing a "last_service_km_" value without crashing.

## What I checked before I accepted its work
I checked that all unit tests passed and verified that the 15,000 km service interval and the 80% warning threshold remained intact. I verified that a vehicle at 14,900 km correctly flags roughly 99.3% wear instead of rounding down to zero, and that vehicles with missing service readings are handled safely without raising exceptions. Finally, I ran "python verify.py" to conform that all logic, unit conversations, and test sites passed

## What the data actually said
The data broke the common assumption that older or higher-mileage cars break down more often: both "odometer_km" (r=+0.002) and "age_years"(r=-0.001) had near-zero correlation with breakdowns, averaging roughly 53,400 km and 5.9 years across both healthy and broken-down vehicles. Instead, the strongest predictors were "km_since_service"(r=+0.40, averaging 11,678km vs 7,261km), "avg_daily_km"(r=+0.25), and "load_factor"(r=+0.22). Combining these three into a risk score places 55% of breakdowns in the top 20 riskiest cars, capturing vehicles driven hard at high loads before they hit the fixed 80% interval threshold
