from flask import Flask, request, jsonify
import requests
import os
import smtplib
import boto3
import time
from email.mime.text import MIMEText

app = Flask(__name__)

# ==============================
# ENV VARIABLES
# ==============================
SLACK_WEBHOOK = os.environ.get("SLACK_WEBHOOK")

EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USER = os.environ.get("EMAIL_USER")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
EMAIL_TO   = os.environ.get("EMAIL_TO")

AWS_REGION = os.environ.get("AWS_DEFAULT_REGION", "ap-south-1")
LOG_GROUP = os.environ.get("LOG_GROUP", "/devops/notifier")
LOG_STREAM = os.environ.get("LOG_STREAM", "notifier-stream")

# ==============================
# CLOUDWATCH CLIENT
# ==============================
logs_client = boto3.client("logs", region_name=AWS_REGION)


# ==============================
# CLOUDWATCH LOG FUNCTION
# ==============================
def send_log(message):
    timestamp = int(time.time() * 1000)

    try:
        logs_client.create_log_group(logGroupName=LOG_GROUP)
    except:
        pass

    try:
        logs_client.create_log_stream(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM
        )
    except:
        pass

    try:
        logs_client.put_log_events(
            logGroupName=LOG_GROUP,
            logStreamName=LOG_STREAM,
            logEvents=[
                {
                    "timestamp": timestamp,
                    "message": message
                }
            ]
        )
    except Exception as e:
        print("CloudWatch Error:", e)


# ==============================
# SLACK FUNCTION
# ==============================
def send_slack(message):
    if not SLACK_WEBHOOK:
        return

    try:
        requests.post(SLACK_WEBHOOK, json={"text": message})
    except Exception as e:
        print("Slack Error:", e)


# ==============================
# EMAIL FUNCTION
# ==============================
def send_email(subject, body):
    if not EMAIL_HOST or not EMAIL_USER or not EMAIL_PASS:
        return

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_TO

        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)

    except Exception as e:
        print("Email Error:", e)


# ==============================
# MAIN API
# ==============================
@app.route("/notify", methods=["POST"])
def notify():
    try:
        data = request.json
        message = data.get("message", "No message")

        # Send notifications
        send_slack(message)
        send_email("Deployment Notification", message)
        send_log(f"Notification sent: {message}")

        return jsonify({
            "status": "success",
            "message": message
        }), 200

    except Exception as e:
        error_msg = f"Error occurred: {str(e)}"
        send_log(error_msg)

        return jsonify({
            "status": "error",
            "message": error_msg
        }), 500


# ==============================
# HEALTH CHECK
# ==============================
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "running"
    }), 200


# ==============================
# START APP
# ==============================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
