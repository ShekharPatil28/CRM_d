This project demonstrates a real-world integration between a Python Flask application and Zoho CRM using OAuth 2.0 Authorization Code Flow.  
The application allows users to authenticate with Zoho, create CRM leads via a web form, and view live lead data stored in Zoho CRM.

 
The application automatically redirects users to Zoho’s OAuth consent screen where permissions are granted to create and read Leads.

<img width="1920" height="1080" alt="2" src="https://github.com/user-attachments/assets/2f17b5ba-c8b9-4cd3-94a0-5dd5aa16ceb5" />


Users can enter lead details such as name, email, and phone number using a simple HTML form.

<img width="1920" height="1080" alt="4" src="https://github.com/user-attachments/assets/8d4d66d5-de31-42cc-a0ed-065bcfcd4d20" />


On form submission, the data is securely sent to Zoho CRM using authenticated REST API calls.

<img width="1920" height="1080" alt="Screenshot 2026-01-17 162959" src="https://github.com/user-attachments/assets/fa0ae77f-4249-4f98-9437-73a5fe1c9669" />


This page fetches live lead data from Zoho CRM and displays it in a tabular format.

<img width="1920" height="1080" alt="5" src="https://github.com/user-attachments/assets/eeb4d120-1fd1-4039-9f95-991630007af9" />


The leads created through the application are visible inside the Zoho CRM Leads module, confirming successful integration.

<img width="1920" height="1080" alt="6" src="https://github.com/user-attachments/assets/32fedf40-014c-437e-adbd-511b7cd75fa3" />








