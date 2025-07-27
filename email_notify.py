import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email_notification(subject: str, message: str,
                            smtp_server: str, smtp_port: int,
                            username: str, password: str,
                            recipient_email: str,
                            sender_email: str = None):
    sender_email = sender_email or username

    # Create MIME message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
        return True
    except Exception as e:
        raise Exception(f"Email sending failed: {e}")


if __name__ == "__main__":
    # Hardcoded values for local testing (do not commit to Git)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = ""  # Replace with your Gmail
    smtp_password = ""  # Use App Password (not Gmail password!)
    recipient_email = ""  # Replace with actual recipient
    subject = "✅ CI/CD Demo Test Email"
    message = "This is a test email from the CI/CD Integration Demo project."

    try:
        send_email_notification(
            subject=subject,
            message=message,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            username=smtp_user,
            password=smtp_password,
            recipient_email=recipient_email
        )
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
