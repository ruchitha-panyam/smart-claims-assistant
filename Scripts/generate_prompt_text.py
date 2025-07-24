import json

# Function to format each claim
def format_claim(claim):
    return f"""--- Claim ID: {claim['claim_id']} ---
Type: {claim['type']}
Description: {claim['description']}
Amount: {claim['amount']}
Urgency: {claim['urgency']}
Prior Claims: {claim['prior_claims']}

"""

# Main function
def main():
    # Load the raw claims
    with open('C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/raw_claims.json', 'r') as f:
        claims = json.load(f)

    # Generate formatted strings for all claims
    formatted_text = ""
    for claim in claims:
        formatted_text += format_claim(claim)

    # Write to output file
    with open('C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/formatted_claims.txt', 'w') as out_file:
        out_file.write(formatted_text)

    print("✅ All formatted claims have been saved to 'formatted_claims.txt'.")

if __name__ == "__main__":
    main()
