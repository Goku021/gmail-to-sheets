import base64


def parse_email(service, msg_id):
    message = service.users().messages().get(
        userId="me",
        id=msg_id,
        format="full"
    ).execute()

    headers = message["payload"]["headers"]
    header_map = {h["name"]: h["value"] for h in headers}

    body = ""
    parts = message["payload"].get("parts", [])

    for part in parts:
        if part["mimeType"] == "text/plain":
            body = base64.urlsafe_b64decode(
                part["body"]["data"]
            ).decode("utf-8")

    return {
        "from": header_map.get("From", ""),
        "subject": header_map.get("Subject", ""),
        "date": header_map.get("Date", ""),
        "body": body.strip()
    }
