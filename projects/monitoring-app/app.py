from flask import Flask, jsonify
import requests
import subprocess
import time
import logging
import threading

#  App Name
APP_NAME = "K8s Self-Healing Monitor"

app = Flask(APP_NAME)

#  Target Application (nginx running in cluster)
TARGET_URL = "http://nginx-service"

# Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def check_application_health():
    """
    Checks if the target application is reachable.
    Returns True if UP, False if DOWN.
    """
    try:
        response = requests.get(TARGET_URL, timeout=5)
        if response.status_code == 200:
            logging.info(" Target application is UP")
            return True
        else:
            logging.warning(f" Unexpected status code: {response.status_code}")
            return False
    except Exception as e:
        logging.error(f" Application is DOWN: {e}")
        return False


def trigger_gitops_self_healing():
    """
    Updates Git repo to trigger Argo CD redeployment.
    """
    logging.info("Triggering GitOps-based self-healing...")

    try:
        # Update replica count (simulate recovery)
        subprocess.run(
            "sed -i 's/replicaCount:.*/replicaCount: 2/' ../nginx-chart/values.yaml",
            shell=True,
            check=True
        )

        # Git operations
        subprocess.run("git add .", shell=True, check=True)
        subprocess.run(
            "git commit -m 'Auto-heal: scaling nginx replicas'",
            shell=True,
            check=True
        )
        subprocess.run("git push", shell=True, check=True)

        logging.info(" GitOps update pushed successfully")

    except subprocess.CalledProcessError as e:
        logging.error(f"Self-healing failed: {e}")


@app.route("/")
def home():
    return jsonify({
        "app": APP_NAME,
        "status": "running"
    })


@app.route("/health")
def health():
    status = check_application_health()
    return jsonify({
        "target_status": "UP" if status else "DOWN"
    })


def monitoring_loop():
    """
    Continuous monitoring loop.
    """
    while True:
        is_healthy = check_application_health()
        if not is_healthy:
            trigger_gitops_self_healing()
        time.sleep(30)


if __name__ == "__main__":
    thread = threading.Thread(target=monitoring_loop)
    thread.start()

    app.run(host="0.0.0.0", port=5000)
