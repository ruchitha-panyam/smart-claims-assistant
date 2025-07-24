def classify_risk(claim):
    amount = claim["amount"]
    urgency = claim["urgency"].strip().lower() == "yes"
    prior = claim["prior_claims"]
    claim_type = claim["type"].strip().lower()

    # Define thresholds
    thresholds = {
        "health insurance": (50000, 250000),
        "auto insurance": (35000, 75000),
        "renters insurance": (10000, 25000),
        "burglary & theft": (10000, 25000),
        "property damage": (75000, 250000)
    }

    low, high = thresholds.get(claim_type, (0, 10000))
    upper_third = high - (high - low) / 3

    # High Risk Rules
    if prior >= 5:
        return "High"
    if prior >= 4 and urgency:
        return "High"
    if amount > high:
        return "High"
    if urgency and prior >= 3 and amount > upper_third:
        return "High"

    # Medium Risk Rules
    if prior in [2, 3]:
        return "Medium"
    if urgency and low < amount <= high:
        return "Medium"
    if not urgency and (0.9 * high) < amount <= high:
        return "Medium"
    if not urgency and prior >= 4:
        return "Medium"

    # Low Risk Rule
    if prior <= 1 and amount <= low:
        return "Low"

    return "Low"  # fallback
