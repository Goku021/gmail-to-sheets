from gmail_service import get_gmail_service, fetch_unread_emails
from email_parser import parse_email
from sheet_service import get_sheets_service, append_row
from state_manager import load_processed_ids, save_processed_id


def main():
    print("🚀 Script started")

    # Step 1: Authenticate Gmail
    print("🔐 Authenticating with Gmail API...")
    gmail_service = get_gmail_service()
    print("✅ Gmail authentication successful")

    # Step 2: Create Google Sheets service
    print("📊 Initializing Google Sheets service...")
    sheets_service = get_sheets_service(gmail_service._http.credentials)
    print("✅ Google Sheets service ready")

    # Step 3: Load processed email IDs (state)
    print("📂 Loading processed email IDs...")
    processed_ids = load_processed_ids()
    print(f"✅ Loaded {len(processed_ids)} processed email IDs")

    # Step 4: Fetch unread emails
    print("📩 Fetching unread emails from Inbox...")
    emails = fetch_unread_emails(gmail_service)
    print(f"📨 Total unread emails found: {len(emails)}")

    # Step 5: Process each email
    for index, email in enumerate(emails, start=1):
        print(f"\n➡️ Processing email {index} with ID: {email['id']}")

        if email["id"] in processed_ids:
            print("⚠️ Email already processed, skipping")
            continue

        # Step 6: Parse email
        print("📝 Parsing email content...")
        data = parse_email(gmail_service, email["id"])
        print("✅ Email parsed successfully")

        # Step 7: Append to Google Sheet
        print("📥 Appending email data to Google Sheet...")
        append_row(
            sheets_service,
            [
                data["from"],
                data["subject"],
                data["date"],
                data["body"]
            ]
        )
        print("✅ Data appended to Google Sheet")

        # Step 8: Mark email as read
        print("📌 Marking email as read...")
        gmail_service.users().messages().modify(
            userId="me",
            id=email["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()
        print("✅ Email marked as read")

        # Step 9: Save processed email ID
        print("💾 Saving processed email ID...")
        save_processed_id(email["id"])
        print("✅ Email ID saved")

    print("\n🎉 Script execution completed successfully")


if __name__ == "__main__":
    main()
