pipeline {
    agent any

    environment {
        DEV_NAMESPACE = 'dev'
        PROD_NAMESPACE = 'prod'
        DEPLOYMENT_NAME = 'nginx-deployment'
        IMAGE_NAME = 'nginx:latest'
        GIT_REPO = 'https://github.com/Susan2018-collab/k8.git'
        BRANCH = 'main'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning Git repository..."
                git branch: "${BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Ensure Minikube & Kubernetes') {
            steps {
                echo "Starting Minikube..."
                sh 'minikube start --driver=docker'
                sh 'kubectl get nodes'
            }
        }

        stage('Deploy to DEV') {
            steps {
                echo "Deploying to DEV namespace..."
                sh "kubectl apply -f nginx-configmap.yaml -n ${DEV_NAMESPACE}"
                sh "kubectl apply -f nginx-service.yaml -n ${DEV_NAMESPACE}"
                sh "kubectl apply -f nginx-deployment.yaml -n ${DEV_NAMESPACE}"
                sh "kubectl config set-context --current --namespace=${DEV_NAMESPACE}"
                sh "kubectl get pods -n ${DEV_NAMESPACE}"
                sh "kubectl get svc -n ${DEV_NAMESPACE}"
                sh "minikube service nginx-service -n ${DEV_NAMESPACE} --url"
            }
        }

        stage('Deploy to PROD') {
            steps {
                echo "Deploying to PROD namespace..."
                sh "kubectl apply -f nginx-configmap.yaml -n ${PROD_NAMESPACE}"
                sh "kubectl apply -f nginx-service.yaml -n ${PROD_NAMESPACE}"
                sh "kubectl apply -f nginx-deployment.yaml -n ${PROD_NAMESPACE}"
                sh "kubectl config set-context --current --namespace=${PROD_NAMESPACE}"
                sh "kubectl get pods -n ${PROD_NAMESPACE}"
                sh "kubectl get svc -n ${PROD_NAMESPACE}"
                sh "minikube service nginx-service -n ${PROD_NAMESPACE} --url"
            }
        }

        stage('Rolling Update DEV') {
            steps {
                echo "Updating nginx image in DEV deployment..."
                sh "kubectl set image deployment/${DEPLOYMENT_NAME} nginx=${IMAGE_NAME} -n ${DEV_NAMESPACE}"
                sh "kubectl get pods -n ${DEV_NAMESPACE}"
            }
        }

        stage('Git Commit & Push') {
            steps {
                echo "Initializing Git and pushing changes..."
                sh 'git init || echo "Already initialized"'
                sh 'git remote remove origin || true'
                sh "git remote add origin ${GIT_REPO}"
                sh 'git add .'
                sh 'git commit -m "CI/CD pipeline commit" || echo "Nothing to commit"'
                sh "git push -u origin ${BRANCH} || echo 'Push may require authentication'"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. DEV pods:"
            sh "kubectl get pods -n ${DEV_NAMESPACE}"
            echo "Pipeline finished. PROD pods:"
            sh "kubectl get pods -n ${PROD_NAMESPACE}"
        }
        success {
            echo "CI/CD pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}
