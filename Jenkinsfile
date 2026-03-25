pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nginx:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git url: 'https://github.com/Susan2018-collab/k8.git', branch: 'main'
            }
        }

        stage('Verify Docker') {
            steps {
                echo "Checking Docker availability..."
                sh 'docker ps || { echo "Docker not available"; exit 1; }'
            }
        }

        stage('Security Scan') {
            steps {
                echo "Running Trivy scan on ${IMAGE_NAME}..."
                sh """
                trivy image --scanners vuln --severity HIGH,CRITICAL --exit-code 1 ${IMAGE_NAME}
                """
            }
        }

        stage('Next Step') {
            steps {
                echo "Next stage placeholder..."
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded!"
        }
        failure {
            echo "❌ Pipeline failed — check logs!"
        }
    }
}
