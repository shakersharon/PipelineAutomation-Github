import os
import requests
import json

def send_slack_notification(message: str, webhook_url: str = None):
    """
    Send a notification message to Slack using Incoming Webhook URL.

    Args:
        message (str): The message text to send.
        webhook_url (str, optional): Slack webhook URL. If not provided,
                                     reads from SLACK_WEBHOOK_URL env variable.

    Returns:
        response object from requests.post
    """
    if webhook_url is None:
        webhook_url = os.getenv('SLACK_WEBHOOK_URL')

    if not webhook_url:
        raise ValueError("Slack webhook URL not provided or set in environment variable 'SLACK_WEBHOOK_URL'")

    slack_data = {
        "text": message
    }

    headers = {'Content-Type': 'application/json'}

    response = requests.post(webhook_url, data=json.dumps(slack_data), headers=headers)

    if response.status_code != 200:
        raise Exception(f"Request to Slack returned error {response.status_code}, response: {response.text}")

    return response


if __name__ == "__main__":
    # Hardcoded webhook for testing
    webhook_url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"  # Replace with your real URL
    message = "✅ CI/CD Demo: Slack notification test successful!"

    try:
        send_slack_notification(message, webhook_url=webhook_url)
        print("Notification sent successfully.")
    except Exception as e:
        print(f"Error sending notification: {e}")

