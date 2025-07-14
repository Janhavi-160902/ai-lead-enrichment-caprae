import pandas as pd
import random

industries = ["Software", "Finance", "Retail", "Healthcare"]
sizes = ["1–10", "11–50", "51–200", "201–500", "500+"]
email_statuses = ["Yes", "No"]

def enrich_company_data(df):
    enriched_data = []

    for _, row in df.iterrows():
        domain = row['domain']
        base_name = domain.split('.')[0].replace("-", " ").title()
        industry = random.choice(industries)
        size = random.choice(sizes)
        email_verified = random.choice(email_statuses)

        score = 0
        if industry == "Software": score += 30
        if size == "51–200": score += 25
        if email_verified == "Yes": score += 20

        if score >= 70:
            tier = "🔥 Hot"
        elif score >= 40:
            tier = "⚠️ Warm"
        else:
            tier = "❌ Cold"

        enriched_data.append({
            "domain": domain,
            "company_name": base_name,
            "industry": industry,
            "employee_range": size,
            "linkedin": f"https://linkedin.com/company/{base_name.replace(' ', '').lower()}",
            "email_verified": email_verified,
            "score": score,
            "tier": tier
        })

    return pd.DataFrame(enriched_data)
