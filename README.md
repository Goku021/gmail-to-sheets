Name: Sagar
📖 Project Overview

This project is a Python automation system that reads real unread emails from a Gmail inbox and logs them into a Google Sheet using official Google APIs.

The system:

Authenticates using OAuth 2.0

Reads unread emails from Inbox

Extracts sender, subject, date, and content

Appends data to Google Sheets

Prevents duplicate entries

Marks emails as read after processing

🎯 Objective

Each qualifying email is appended as a new row in Google Sheets with the following columns:

Column	Description
From	Sender email address
Subject	Email subject
Date	Date & time received
Content	Plain text email body


🧱 Project Structure
gmail-to-sheets/
│
├── src/
│   ├── gmail_service.py
│   ├── sheets_service.py
│   ├── email_parser.py
│   ├── state_manager.py
│   └── main.py
│
├── credentials/
│   └── credentials.json   (NOT COMMITTED)
│
├── proof/
│   ├── gmail_unread.png
│   ├── google_sheet.png
│   └── oauth_consent.png
│
├── requirements.txt
├── config.py
├── README.md
└── .gitignore

🏗️ High-Level Architecture

Gmail Inbox
     |
     | (Gmail API - OAuth 2.0)
     |
Email Fetcher
     |
Email Parser
     |
Duplicate Check (State File)
     |
Google Sheets API
     |
Google Sheet

🔐 OAuth 2.0 Authentication Flow

Uses OAuth 2.0 (Desktop Application)

User logs in via Google Consent Screen

Access token is stored in credentials/token.json

Token is reused in subsequent runs

No service accounts are used (as per requirement)

Scopes used:

https://www.googleapis.com/auth/gmail.modify

https://www.googleapis.com/auth/spreadsheets

⚙️ Functional Flow

Authenticate with Gmail API

Fetch unread emails from Inbox

Parse sender, subject, date, and body

Check if email was already processed

Append email data to Google Sheet

Mark email as read

Save email ID to prevent duplicates

🛡️ Duplicate Prevention Logic

Each Gmail email has a unique message ID

All processed message IDs are stored locally

Before processing, the script checks if the ID already exists

This guarantees no duplicate rows, even if the script is run multiple times

📂 State Persistence Method (IMPORTANT)

Method Used: Local file-based storage

File: processed_ids.txt

Why this approach?

Simple and reliable

Persistent across script executions

No additional database required

Fast lookup using Python sets

Stored Data Example:

18c9a1a7d83
18c9a1b29f1

🚀 Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd gmail-to-sheets

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Google Cloud Setup

Create Google Cloud project

Enable Gmail API & Google Sheets API

Configure OAuth Consent Screen (External)

Add your Gmail as Test User

Download credentials.json

Place it in credentials/ folder

5️⃣ Configure Spreadsheet

Create Google Sheet

Add headers:

From | Subject | Date | Content


Copy Spreadsheet ID

Paste into config.py

6️⃣ Run the Script
python src/main.py

📸 Proof of Execution

Included in /proof/ folder:

Gmail inbox with unread emails

Google Sheet populated with email data

OAuth consent screen

Screen recording explaining execution flow

🧪 What Happens on Re-run?

Already processed emails are skipped

Only new unread emails are processed

No duplicate rows are created

Script exits cleanly if no unread emails exist

🧠 Challenges Faced & Solution
Challenge:

OAuth authentication did not open browser automatically on some systems.

Solution:

Used console-based OAuth flow (run_console) to manually authenticate via URL, ensuring compatibility across environments.

⚠️ Limitations

Only processes unread Inbox emails

Plain text email body only (no attachments)

State stored locally (not cloud-synced)


⭐ Bonus Features Implemented

Console logging for each step

Duplicate prevention

Safe token reuse

Clean project structure


🔄 Post-Submission Modification Readiness

The modular design allows easy changes such as:

Filtering emails by subject

Adding new columns

Processing emails from last 24 hours

Excluding automated senders

🔐 Security Notes

credentials.json is NOT committed

OAuth tokens are excluded via .gitignore

Repository follows security guidelines strictly

✅ Conclusion

This project demonstrates:

Real-world API integration

Secure OAuth authentication

Data persistence

Clean architecture

Production-ready automation logic
