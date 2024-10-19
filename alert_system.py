import smtplib
from email.mime.text import MIMEText
from config import ALERT_THRESHOLD, LOCATIONS

def send_alert(message):
    # Sample Email Sending (SMTP)
    msg = MIMEText(message)
    msg['Subject'] = 'Weather Alert'
    msg['From'] = 'youremail@example.com'
    msg['To'] = 'receiver@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("youremail@example.com", "password")
        server.send_message(msg)

def check_alerts(data):
    for record in data:
        if record.temperature > ALERT_THRESHOLD:
            send_alert(f"Temperature exceeded in {record.city}: {record.temperature}°C")
