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
            echo "✅ Update completed successfully!"
        }
        failure {
            echo "❌ Update failed!"
            echo "✅ Pipeline succeeded!"
        }
    }
}
