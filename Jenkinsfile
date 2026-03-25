pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nginx:latest'
    }

    stages {

        // 🔹 1. Checkout Code
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/Susan2018-collab/k8.git'
            }
        }

        // 🔹 2. Verify Docker
        stage('Verify Docker') {
            steps {
                echo "Checking Docker availability..."
                sh 'docker ps'
            }
        }

        // 🔹 3. Security Scan (Trivy)
        stage('Security Scan') {
            steps {
                echo "Running optimized Trivy scan..."

                sh """
                docker run --rm \
                  -v /var/run/docker.sock:/var/run/docker.sock \
                  -v \$HOME/.cache/trivy:/root/.cache/ \
                  aquasec/trivy:latest image \
                  --scanners vuln \
                  --severity HIGH,CRITICAL \
                  --timeout 10m \
                  --exit-code 1 \
                  ${IMAGE_NAME}
                """
            }
        }

        // 🔹 4. Dummy Next Step (example)
        stage('Next Step') {
            steps {
                echo "Security scan passed. Ready for deployment..."
            }
        }
    }

    post {
        success {
            echo "✅ Security scan passed — pipeline continues"
        }
        failure {
            echo "❌ Security scan failed — vulnerabilities detected"
        }
        always {
            echo "Pipeline execution completed"
        }
    }
}

