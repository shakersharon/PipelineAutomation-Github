# CI/CD Pipeline Testing Project

## Overview

This demo project runs automated tests on push and pull requests using GitHub Actions. It demonstrates:
```
- Multi-OS and Python version test matrix
- Automated test execution with Pytest
- HTML test report upload as an artifact
- Slack notifications on success/failure
- Email notification on test failure
```
## Running tests locally

```bash
pip install -r requirements.txt
pytest tests/ --html=report.html --self-contained-html
pytest tests/test_api.py --html=report.html --self-contained-html
pytest tests/test_api.py
python slack_notify.py
python email_notify.py
```
## 🔔Slack Notifications Setup
```bash
Go to your Slack("https://api.slack.com/apps")

Click “Create New App” → From Scratch

Name your app (e.g., ci-cd-notifier) and select your workspace

On the left sidebar, go to Incoming Webhooks

Toggle Activate Incoming Webhooks to On

Scroll down and click “Add New Webhook to Workspace”

Choose a Slack channel (e.g., #ci-cd) and click Allow

Copy the generated Webhook URL
```
## How to Use the Webhook
```
✅ Option 1: Hardcoded Webhook

Edit slack_notify.py:

webhook_url = "https://hooks.slack.com/services/XXXX/XXXX/XXXX"
send_slack_notification("Test completed successfully.", webhook_url=webhook_url)
Then run:

python slack_notify.py
```
```
✅ Option 2: Use Environment Variable

Set the environment variable:

macOS/Linux:

export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXXX/XXXX/XXXX"

Windows Command Prompt:

set SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXXX/XXXX/XXXX

Windows PowerShell:

$env:SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXXX/XXXX/XXXX"

Then run:

python slack_notify.py
```
## ✉️ Email Notification Setup
```
✅ Step 1: Enable App Passwords
Go to your Google Account Security Settings

Enable 2-Step Verification if not already enabled

Go to App Passwords

Choose Mail as the app and Windows Computer as the device

Click Generate, and copy the 16-character app password
```
```
✅ Step 2: Update email_notify.py
Edit these variables:

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "your_email@gmail.com"
smtp_password = "your_generated_app_password"
recipient_email = "recipient@example.com"

Then run:

python email_notify.py
```
