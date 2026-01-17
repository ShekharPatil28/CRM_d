import os

CLIENT_ID = os.environ.get("1000.F2JLI34I993NA0K3VT15M7X3WUOMKY")
CLIENT_SECRET = os.environ.get("4073b74de4581a236a273097de38eca9f84ecb1922")
REDIRECT_URI = os.environ.get("http://localhost:8000/callback")


AUTH_URL = "https://accounts.zoho.in/oauth/v2/auth"
TOKEN_URL = "https://accounts.zoho.in/oauth/v2/token"

CRM_API_BASE = "https://www.zohoapis.in/crm/v2"

AUTHORIZATION_URL = (
    "https://accounts.zoho.in/oauth/v2/auth"
    "?scope=ZohoCRM.modules.Leads.CREATE,ZohoCRM.modules.Leads.READ"
    f"&client_id={CLIENT_ID}"
    "&response_type=code"
    "&access_type=offline"
    f"&redirect_uri={REDIRECT_URI}"
)







