# 🚀 GitOps-Based CI/CD & Self-Healing Kubernetes Platform

## 📌 Overview

This project implements a **GitOps-driven CI/CD pipeline with automated deployment and self-healing capabilities** using:

- Jenkins (CI/CD automation)
- Docker (containerization)
- Kubernetes (Minikube cluster)
- Argo CD (GitOps continuous deployment)
- Helm (Kubernetes packaging)

The system automates the full lifecycle:
> Code → Build → Image → Helm Update → Git Push → Argo CD Sync → Kubernetes Deployment



## 🏗️ Architecture

<img width="2313" height="1611" alt="mermaid-diagram (1)" src="https://github.com/user-attachments/assets/22b58ba0-18dc-4a02-94b2-9f2cc7c6245d" />


The system follows a GitOps workflow where Git acts as the single source of truth. Any change pushed to Git automatically triggers deployment via Argo CD.



## 🚀 Deployment Flow

<img width="3976" height="512" alt="mermaid-diagram (2)" src="https://github.com/user-attachments/assets/26f970f9-3602-4c01-95b0-ea94a45f5d91" />


![Deployment Diagram](docs/deployment.png)

### CI/CD Flow:
1. Developer pushes code to GitHub
2. Jenkins pipeline is triggered
3. Docker image is built
4. Helm chart is updated with new image tag
5. Changes are committed back to Git
6. Argo CD detects changes
7. Kubernetes automatically deploys updated application



## 🔁 Self-Healing Mechanism

The monitoring application continuously checks system health:

- If application failure is detected:
  - Git is updated with corrective changes
  - Argo CD re-syncs cluster state
  - Kubernetes redeploys healthy version


## 🧩 Components

### ⚙️ Jenkins
- Builds Docker images
- Updates Helm charts
- Pushes updates to GitHub

### 🔁 Argo CD
- Watches Git repository
- Syncs Kubernetes cluster state
- Ensures drift correction

### ☸️ Kubernetes (Minikube)
- Runs application workloads
- Handles scaling and recovery

### 📊 Monitoring App (Python Flask)
- Provides health check API
- Triggers GitOps-based recovery workflow


## 📸 Screenshots

### 1. Argo CD UI
![ArgoCD UI](docs/screenshots/argocd.png)

### 2. Jenkins Pipeline
![Jenkins Pipeline](docs/screenshots/jenkins.png)

### 3. Kubernetes Pods
![K8s Pods](docs/screenshots/k8s-pods.png)

### 4. Application UI
![App UI](docs/screenshots/app.png)

---

## ⚙️ Tech Stack

- Kubernetes (Minikube)
- Argo CD
- Jenkins
- Docker
- Helm
- Python Flask
- GitHub (GitOps)

---

## 📊 Key Features

- GitOps-based deployment pipeline
- Automated CI/CD workflow
- Self-healing infrastructure loop
- Helm-based Kubernetes deployments
- Continuous reconciliation using Argo CD

---

## 🔮 Future Improvements

- Multi-cloud deployment (AWS, Azure, On-prem)
- Prometheus + Grafana observability
- Security scanning (Trivy integration)
- Canary deployments
- RBAC + policy enforcement

---

## 👨‍💻 Author

DevOps / Platform Engineering Project demonstrating GitOps, CI/CD automation, and Kubernetes self-healing architecture.
