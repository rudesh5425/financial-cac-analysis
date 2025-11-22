"""
Financial CAC Analysis - GA8
Author: Rudesh
Email: 24ds2000104@ds.study.iitm.ac.in
This file was generated with the help of ChatGPT (LLM-assisted).
"""

import pandas as pd
import matplotlib.pyplot as plt

# Quarterly CAC data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "CAC": [225.22, 225.56, 228.82, 236.41]
}

df = pd.DataFrame(data)

# Compute average CAC
average_cac = df["CAC"].mean()
print("Average CAC:", average_cac)

# Plot CAC trend vs industry benchmark
plt.figure(figsize=(8, 6))
plt.plot(df["Quarter"], df["CAC"], marker='o', label="CAC Trend", linewidth=3)
plt.axhline(150, color='red', linestyle='--', label="Industry Target (150)")

plt.title("Customer Acquisition Cost - Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("CAC ($)")
plt.legend()
plt.grid(True)

plt.savefig("cac_plot.png", dpi=120)
print("Plot saved as cac_plot.png")
print("Analysis completed successfullly.")