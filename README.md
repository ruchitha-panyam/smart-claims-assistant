**Smart Claims Assistant: Using GenAI to Automate Insurance Claim Summaries \& Risk Flags**



An AI-powered insurance claim assistant that automates the process of summarizing raw claim descriptions and flags high-risk cases using GPT-4 and rule-based classification logic.



---



**Project Goals**



\- Summarize unstructured insurance claims into concise, 2–3 bullet point summaries using GenAI

\- Classify each claim into Low, Medium, or High Risk using business-defined rules

\- Reduce manual review time, eliminate inconsistency, and help insurance teams prioritize better



---



**Tools \& Technologies**



| Tool               | Purpose                                  |

|--------------------|------------------------------------------|

| OpenAI GPT-4       | Claim summarization + risk reasoning     |

| Python             | Data processing + risk classification    |

| Pandas / JSON      | Data storage and manipulation            |

| Figma              | UI mockups (Input \& Output screens)      |

| Google Slides      | Final presentation deck                  |



---



**Project Folder Structure**



smart-claims-assistant/

│

├── data/ # Raw and processed claims

│ ├── raw\_claims.json

│ ├── raw\_claims\_with\_risk\_flags.json

│ └── processed\_claims.csv

│

├── prompts/ # Prompt engineering experiments

│ ├── prompt\_notes.txt

│ ├── raw\_gpt\_outputs.txt

│ ├── raw\_gpt\_outputs2.txt

│ ├── formatted\_claims.txt

│ └── working\_examples.json

│

├── scripts/ # Python scripts

│ ├── generate\_prompt\_text.py

│ ├── parse\_gpt\_output.py

│ ├── process\_claims.py

│ └── risk\_classifier.py

│

├── docs/ # Strategy and business rules

│ ├── risk\_rules.txt

│ └── classification\_strategy.txt

│

├── ui/ # Figma mockups

│ ├── input\_screen.png

│ └── output\_screen.png

│

├── SmartClaimsAssistant.pdf # Final Presentation

├── processed\_claims\_insights.csv # GPT vs Code accuracy comparison

└── README.md # This file





---



**Business Impact**



\- 50% reduction in time per claim review (8 mins → 3–4 mins)

\- Smarter triage by surfacing high-risk claims instantly

\- Consistency through rule-based logic, reducing human error by up to \*\*35%\*\*

\- Scalable insights and explainable outputs for auditing, fraud detection, and resource allocation



---



**Results**



\- GPT accuracy reached 98% after 5 prompt iterations

\- Risk classifier successfully flagged 100% of high-risk cases based on defined rules

\- Output saved in `processed\_claims.csv` and `working\_examples.json`



---



**How It Works**



1\. Input: Raw JSON claims (type, amount, urgency, description, prior claims)

2\. Step 1: GPT-4 generates a summary and risk reasoning

3\. Step 2: Python classifier applies business rules to tag risk level

4\. Output: Cleaned dataset with summaries + risk flags + reasons



---



**What We Learned**



\- GPT + rule-based logic can deliver powerful, transparent insights

\- Prompt engineering is critical for aligning GenAI with business goals

\- Domain-specific rules reduce reliance on large ML models

\- A hybrid AI-human workflow leads to smarter decisions in claim processing



---



**Future Scope**



\- Integrate GPT-4 with OpenAI API for real-time claims input

\- Add dashboards for risk distribution and fraud pattern analytics

\- Push high-risk alerts to internal systems (CRM, ticketing, etc.)

\- Wrap logic into microservice with REST API support



---



**Authors**



\- Ruchitha Panyam

\- Pranay Shetty



---



**Project Report \& Demo Files**



\- \[Slide Deck – Smart Claims Assistant](./SmartClaimsAssistant.pdf)

\- \[Figma UI Screens (Input + Output)](./ui/)

\- \[Processed Results + GPT Accuracy](./processed\_claims\_insights.csv)



---




