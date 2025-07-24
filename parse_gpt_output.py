import re
import json

def clean_text(text):
    replacements = {
        "\u00e2\u2030\u00a4": "≤",
        "\u00e2\u2030\u00a5": "≥",
        "\u00e2\u20ac\u201d": "—",
        "\u00e2\u20ac\u2122": "'",
        "\u2013": "–",
        "\u00e2\u20ac\u201c": "–"
    }
    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)
    return text

def parse_gpt_output(text):
    entries = []
    blocks = text.strip().split("Claim ID:")
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        claim_id = lines[0].strip()
        summary_lines = []
        risk_level = ""
        reasoning = ""

        i = 1
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("Summary:"):
                i += 1
                while i < len(lines) and not lines[i].startswith("Risk Level:"):
                    summary_lines.append(lines[i].strip())
                    i += 1
            elif line.startswith("Risk Level:"):
                risk_level = line.replace("Risk Level:", "").strip()
                i += 1
            elif line.startswith("Reason:"):
                reasoning = lines[i].replace("Reason:", "").strip()
                i += 1
            else:
                i += 1

        summary_cleaned = clean_text(", ".join(summary_lines))
        reasoning_cleaned = clean_text(reasoning)

        entry = {
            "claim_id": claim_id,
            "summary": summary_cleaned,
            "risk_flag": risk_level,
            "reasoning": reasoning_cleaned
        }
        entries.append(entry)

    return entries

def main():
    with open('C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/raw_gpt_outputs.txt', 'r', encoding='utf-8') as f:
        gpt_text = f.read()

    parsed_entries = parse_gpt_output(gpt_text)

    with open('C:/Users/panya_gct7/OneDrive/Documents/Smart_Claims_Assistant/claims_assistant/working_examples.json', 'w', encoding='utf-8') as f:
        json.dump(parsed_entries, f, indent=2, ensure_ascii=False)

    print("✅ Parsed output saved to prompts/working_examples.json")

if __name__ == "__main__":
    main()
