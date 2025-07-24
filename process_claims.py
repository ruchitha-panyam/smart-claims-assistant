import json
import pandas as pd
from risk_classifier import classify_risk

# Load raw claims
with open("C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/raw_claims.json", "r") as f:
    claims = json.load(f)

# Apply classification
for claim in claims:
    claim["risk_flag"] = classify_risk(claim)

# Convert to DataFrame and export
df = pd.DataFrame(claims)
df.to_csv("C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/processed_claims.csv", index=False)

print("Data processed and saved to processed_claims.csv")
