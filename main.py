from flask import Flask, render_template, request, redirect
from auth import get_access_token
from crm_api import create_lead, get_leads
from config import AUTHORIZATION_URL    
import os

app = Flask(__name__)

ACCESS_TOKEN = None   

@app.route("/")
def form():
    global ACCESS_TOKEN

    if not ACCESS_TOKEN:

        return redirect(AUTHORIZATION_URL)

    return render_template("form.html")

# @app.route("/callback")
# def callback(): 
#     global ACCESS_TOKEN
#     code = request.args.get("code")
#     ACCESS_TOKEN = get_access_token(code)
#     return "OAuth successful. Go back to the form."
@app.route("/callback")
def callback():
    global ACCESS_TOKEN
    code = request.args.get("code")
    ACCESS_TOKEN = get_access_token(code)

    # After OAuth, send user back to app
    return redirect("/")


@app.route("/create-lead", methods=["POST"])
def create_lead_route():
    global ACCESS_TOKEN

    data = {
        "First_Name": request.form["first_name"],
        "Last_Name": request.form["last_name"],
        "Email": request.form["email"],
        "Phone": request.form["phone"]
    }

    create_lead(ACCESS_TOKEN, data)
    return "Lead created successfully. <a href='/'>Go back</a>"

@app.route("/leads")
def view_leads():
    global ACCESS_TOKEN
    leads = get_leads(ACCESS_TOKEN)
    return render_template("leads.html", leads=leads)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

