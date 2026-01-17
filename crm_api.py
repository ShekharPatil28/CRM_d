import requests
from config import CRM_API_BASE

def create_lead(token, lead_data):
    url = f"{CRM_API_BASE}/Leads"
    headers = {
        "Authorization": f"Zoho-oauthtoken {token}",
        "Content-Type": "application/json"
    }

    payload = {"data": [lead_data]}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

def get_leads(token):
    url = f"{CRM_API_BASE}/Leads"
    headers = {
        "Authorization": f"Zoho-oauthtoken {token}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["data"]
