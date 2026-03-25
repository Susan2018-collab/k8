pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/yourusername/k8s-demo.git'
            }
        }
        stage('Deploy to DEV') {
            steps {
                sh 'minikube -n dev kubectl apply -f nginx-configmap.yaml'
                sh 'minikube -n dev kubectl apply -f nginx-deployment.yaml'
                sh 'minikube -n dev kubectl apply -f nginx-service.yaml'
            }
        }
        stage('Rolling Update') {
            steps {
                sh 'minikube -n dev kubectl set image deployment/nginx-deployment nginx=nginx:latest'
            }
        }
    }
}
