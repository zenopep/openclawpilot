from typing import Dict, List
import requests
import os


# =========================
# LEAD AGENT (REALI - SERPAPI)
# =========================
def lead_agent(prompt: str) -> Dict:
    api_key = os.getenv("SERPAPI_KEY")

    if not api_key:
        return {
            "agent": "Lead Agent",
            "error": "Missing SERPAPI_KEY",
            "output": []
        }

    query = "hostel bike rental walking tours Barcelona"

    url = "https://serpapi.com/search.json"

    params = {
        "q": query,
        "hl": "en",
        "gl": "es",
        "api_key": api_key
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        data = response.json()

        leads = []

        for result in data.get("organic_results", [])[:5]:
            link = result.get("link")

            email = extract_email_from_website(link) if link else None

            leads.append({
                "name": result.get("title"),
                "link": link,
                "email": email
            })

        return {
            "agent": "Lead Agent",
            "task": "Lead reali da Google",
            "output": leads
        }

    except Exception as e:
        return {
            "agent": "Lead Agent",
            "error": str(e),
            "output": []
        }
import re

def extract_email_from_website(url: str) -> str:
    try:
        res = requests.get(url, timeout=10)
        html = res.text

        # regex semplice email
        emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", html)

        if emails:
            return emails[0]

        return None

    except Exception:
        return None

# =========================
# OUTREACH AGENT (COMPATIBILE CON LEAD REALI)
# =========================
def outreach_agent(leads: List[Dict]) -> Dict:
    results = []

    for lead in leads:
        name = lead.get("name")
        email = lead.get("email")

        if not email:
            continue

        prompt = f"""
Write a short cold email for this company:

{name}

Context:
- Location: Barcelona
- Project: free water bottles for tourists funded by sponsors
- Goal: partnership for distribution

Language:
- Use English as default
- If the company is clearly Spanish/local, you may use Spanish

Tone:
- direct
- business
- concise
"""

        body = ask_openrouter(prompt)

        subject = "Partnership opportunity in Barcelona tourism"

        sent = send_email(email, subject, body)

        results.append({
            "name": name,
            "email": email,
            "sent": sent,
            "preview": body[:120]
        })

    return {
        "agent": "Outreach Agent",
        "results": results
    }
# =========================
# SALES AGENT (STRATEGIA)
# =========================
def sales_agent() -> Dict:
    return {
        "agent": "Sales Agent",
        "strategy": {
            "target": "Brand turistici, beverage, telecom, travel",
            "offer": "Visibilità su bottiglie + landing page",
            "pricing": "€5K - €25K per campagna",
            "approach": [
                "cold email",
                "LinkedIn outreach",
                "intro tramite contatti locali"
            ]
        }
    }