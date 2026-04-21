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

## ⚙️ Implementation Steps

### 1. Kubernetes Cluster Setup
- Initialized local Kubernetes cluster using Minikube
- Verified node readiness using kubectl

### 2. Argo CD Installation (GitOps Layer)
- Created `argocd` namespace
- Installed Argo CD using official manifest
- Exposed Argo CD server using NodePort / port-forward
- Configured initial admin credentials

### 3. Application Deployment (Helm-based)
- Created Helm charts for:
  - Nginx application
  - Monitoring application
- Defined deployment, service, and configuration templates

### 4. CI/CD Pipeline Setup (Jenkins)
- Configured Jenkins in Docker container
- Installed required plugins (Docker, Git, Pipeline)
- Created Jenkins pipeline to:
  - Build Docker image
  - Update Helm chart image tag
  - Commit changes back to GitHub

### 5. GitOps Workflow Integration
- Connected GitHub repository to Argo CD
- Configured Argo CD Application to track:
  - `projects/monitoring-chart`
  - `projects/nginx-chart`
- Enabled automated sync and self-healing

### 6. Deployment Flow Validation
- Triggered Jenkins pipeline via code commit
- Verified Docker image build
- Confirmed Helm chart update in Git
- Observed Argo CD auto-sync
- Verified Kubernetes pod rollout

### 7. Monitoring & Self-Healing Validation
- Deployed monitoring application (Flask-based)
- Exposed health check endpoint
- Simulated failure scenario
- Verified automatic reconciliation via GitOps loop

## 📸 Screenshots

### 1. Argo CD UI
<img width="3456" height="1908" alt="image" src="https://github.com/user-attachments/assets/c4af0c07-f5e3-445a-8741-9f37bec0a58b" />
<img width="1728" height="954" alt="+ orpo" src="https://github.com/user-attachments/assets/a071b4f0-aa3f-49da-91fb-0e7ed2afddd3" />
<img width="1728" height="954" alt="Pasted Graphic 18" src="https://github.com/user-attachments/assets/61fd58c0-16cd-4709-a9f6-90032f4955a3" />

### 2. Jenkins Pipeline
<img width="1713" height="952" alt="Pasted Graphic 29" src="https://github.com/user-attachments/assets/6f3a2a10-e58c-458a-a16e-b3ec3d861ac3" />
<img width="1713" height="952" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/02e8a0e8-9023-444b-ae75-469ee9b53183" />

### 3. Kubernetes Pods
<img width="980" height="89" alt="Pasted Graphic 20" src="https://github.com/user-attachments/assets/31c00d8b-e149-4b12-9bfa-235ee857f66e" />
<img width="980" height="123" alt="Pasted Graphic 21" src="https://github.com/user-attachments/assets/56143223-7353-456d-89b8-20419928863d" />
<img width="1728" height="909" alt="Pasted Graphic 24" src="https://github.com/user-attachments/assets/fae53b42-9eb7-4d57-951f-c6012a7f2d6a" />

### 4. Application UI
<img width="1447" height="716" alt="Pasted Graphic 23" src="https://github.com/user-attachments/assets/24dcb5c2-8160-4780-9211-a8c92fe7ce6e" />

## ⚙️ Tech Stack

- Kubernetes (Minikube)
- Argo CD
- Jenkins
- Docker
- Helm
- Python Flask
- GitHub (GitOps)

## 📊 Key Features

- GitOps-based deployment pipeline
- Automated CI/CD workflow
- Self-healing infrastructure loop
- Helm-based Kubernetes deployments
- Continuous reconciliation using Argo CD


## 🔮 Future Improvements

- Multi-cloud deployment (AWS, Azure, On-prem)
- Prometheus + Grafana observability
- Security scanning (Trivy integration)
- Canary deployments
- RBAC + policy enforcement


## 👨‍💻 Author
Susan Daniel
DevOps Engineer
