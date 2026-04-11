GitOps-Based Kubernetes Self-Healing System
Project Overview
This project demonstrates a production-grade DevOps architecture that combines GitOps, Kubernetes, monitoring, and automated self-healing.
A custom Python-based monitoring service continuously checks the health of an application running in Kubernetes. If a failure is detected, it automatically triggers GitOps-based remediation by updating the Git repository, which is then reconciled by Argo CD.

Architecture
Developer → GitHub → Argo CD → Kubernetes Cluster
                                   ↓
                     ┌─────────────┴─────────────┐
                     ↓                           ↓
               Target App                  Monitoring App
               (NGINX)                   (Python Flask)
                     ↓                           ↓
                Health API              Health Check Logic
                                                ↓
                                     Git Update (Helm values)
                                                ↓
                                           Argo CD Sync
                                                ↓
                                          Self-Healing

 Tech Stack
* CI/CD & GitOps: Argo CD, GitHub
* Containerization: Docker
* Orchestration: Kubernetes (Minikube)
* Package Manager: Helm
* Monitoring App: Python (Flask)
* Scripting: Bash
* Cloud/Infra Concepts: AWS, Networking, IAM
* Security: Kubernetes RBAC

Repository Structure
devops-project/
├── monitoring-app/      —> Python monitoring service
├── monitoring-chart/    —> Helm chart for monitoring app
├── nginx-chart/           —> Helm chart for target app
├── jenkins/               —> CI pipeline (optional)
└── README.md


1. Application Deployment (GitOps)
* All Kubernetes manifests and Helm charts are stored in GitHub
* Argo CD continuously monitors the repository
* Any change in Git is automatically applied to the cluster

2. Monitoring System
* A Flask-based Python application runs inside Kubernetes
* It periodically checks the health of the target application (nginx-service)
* Health check runs every 30 seconds

3. Failure Detection
* If the target app is unreachable or returns an error:
    * The monitoring service detects the failure
    * Logs the issue

4. Self-Healing Mechanism (Core Feature)
* Instead of directly modifying the cluster, the system:
    1. Updates Helm values in the Git repository
    2. Commits and pushes changes
    3. Argo CD detects the change
    4. Automatically redeploys the application
 This ensures Git remains the single source of truth (GitOps principle)

 Self-Healing Flow
App Failure → Monitoring Detects → Git Update → Argo CD Sync → App Restored

Setup Instructions
—>  Prerequisites
* Docker
* Kubernetes (Minikube)
* kubectl
* Helm
* Argo CD


  1. Start Minikube
minikube start 
 2. Install Argo CD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

 3. Access Argo CD UI
kubectl port-forward svc/argocd-server -n argocd 8080:443
Get password:
kubectl get secret argocd-initial-admin-secret -n argocd -o yaml
echo <password> | base64 --decode
Open: —>  https://localhost:8080

 4. Build & Push Monitoring App
docker build -t <your-dockerhub>/monitor-app:latest ./monitoring-app
docker push <your-dockerhub>/monitor-app:latest

 5. Connect Git Repo in Argo CD
* Go to Argo CD UI
* Create new application
* Select repo and path (monitoring-chart or nginx-chart)
* Enable auto-sync

6. Deploy Applications
Argo CD will automatically deploy:
* Target application (NGINX)
* Monitoring application

Testing Self-Healing  Simulate Failure
kubectl scale deployment nginx-app --replicas=0

Observe
* Monitoring app detects failure
* Git repository is updated
* Argo CD syncs changes
* Application is restored

 Security (RBAC)
* Implemented Kubernetes RBAC for controlled access
* Monitoring app uses a dedicated ServiceAccount
* Permissions restricted to required resources only

 Key Features
-  GitOps-based deployment using Argo CD
-  Automated monitoring using Python
-  Self-healing via Git-driven updates
-  Helm-based Kubernetes deployments
-  RBAC-secured cluster access
-  Fully automated CI/CD-ready architecture

Screenshots
### Argo CD Dashboard
![ArgoCD](screenshots/argocd.png)

### Kubernetes Pods
![Pods](screenshots/pods.png)

### Self-Healing Demo
![Self Healing](screenshots/self-healing.png)

### Application UI
![App UI](screenshots/app-ui.png)

 👤 Author
Susan Daniel DevOps Engineer 
