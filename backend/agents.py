from typing import Dict

def lead_agent(prompt: str) -> Dict:
    return {
        "agent": "Lead Agent",
        "task": "Trova potenziali lead",
        "output": [
            "Hostel One Barcelona",
            "Free Walking Tours BCN",
            "Bike Rental Barcelona"
        ]
    }


def outreach_agent(leads: list) -> Dict:
    messages = []
    for lead in leads:
        messages.append(f"""
Ciao {lead},

stiamo lanciando un progetto innovativo a Barcellona:
distribuzione gratuita di acqua ai turisti con visibilità brand.

Ti interessa collaborare come partner distributivo?

Parliamone 10 min.

— Gennaro
""")

    return {
        "agent": "Outreach Agent",
        "messages": messages
    }


def sales_agent() -> Dict:
    return {
        "agent": "Sales Agent",
        "strategy": "Chiudere sponsor €25K campagne"
    }