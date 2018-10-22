import smtplib
from utils import get_credentials

MESSAGE = {
    "DRY": "Need to water the plant. DRY SOIL",
    "WET": "Plants are happy."
}


def send_email(wet_status):
    """Gets the credentials from a json file and send the alert."""
    creds = get_credentials()
    server = smtplib.SMTP(creds.get("SMTP_HOST"), 587)
    server.login(creds.get("SMTP_LOGIN"), creds.get("SMTP_PASSWORD"))
    msg = MESSAGE[wet_status]
    for receiver in creds.get("RECEIVERS_EMAILS"):
        server.sendmail(creds.get("SENDER_EMAIL"), receiver, msg)