pipeline {
    agent any

    environment {
        DEV_NAMESPACE  = "dev"
        PROD_NAMESPACE = "prod"
        DEV_DEPLOYMENT  = "nginx-deployment"
        PROD_DEPLOYMENT = "nginx-deployment-prod"
        NGINX_IMAGE     = "nginx:latest"
        KUBECONFIG      = "/root/.kube/config"
    }

    stages {
        stage('Update Nginx in DEV') {
            steps {
                echo "Updating Nginx in DEV namespace..."
                sh '''
                    kubectl set image deployment/${DEV_DEPLOYMENT} nginx=${NGINX_IMAGE} -n ${DEV_NAMESPACE}
                    kubectl rollout status deployment/${DEV_DEPLOYMENT} -n ${DEV_NAMESPACE}
                '''
            }
        }

        stage('Update Nginx in PROD') {
            steps {
                input message: "Approve update for PROD namespace?"
                echo "Updating Nginx in PROD namespace..."
                sh '''
                    kubectl set image deployment/${PROD_DEPLOYMENT} nginx=${NGINX_IMAGE} -n ${PROD_NAMESPACE}
                    kubectl rollout status deployment/${PROD_DEPLOYMENT} -n ${PROD_NAMESPACE}
                '''
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
            echo "✅ Update completed successfully!"
        }
        failure {
            echo "❌ Update failed!"
        }
    }
}
