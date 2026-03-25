pipeline {
    agent any

    environment {
        DEV_NAMESPACE  = "dev"
        PROD_NAMESPACE = "prod"
        DEV_DEPLOYMENT  = "nginx-deployment"
        PROD_DEPLOYMENT = "nginx-deployment-prod"
        NGINX_IMAGE     = "nginx:latest"  // or specify a version
    }

    stages {
        stage('Update Nginx in DEV') {
            steps {
                echo "Updating Nginx in DEV namespace..."
                sh """
                    kubectl set image deployment/${DEV_DEPLOYMENT} nginx=${NGINX_IMAGE} -n ${DEV_NAMESPACE}
                    kubectl rollout status deployment/${DEV_DEPLOYMENT} -n ${DEV_NAMESPACE}
                """
            }
        }

        stage('Update Nginx in PROD') {
            steps {
                input message: "Approve update for PROD namespace?"
                echo "Updating Nginx in PROD namespace..."
                sh """
                    kubectl set image deployment/${PROD_DEPLOYMENT} nginx=${NGINX_IMAGE} -n ${PROD_NAMESPACE}
                    kubectl rollout status deployment/${PROD_DEPLOYMENT} -n ${PROD_NAMESPACE}
                """
            }
        }
    }

    post {
        success {
            echo "✅ Nginx updated successfully in DEV and PROD!"
        }
        failure {
            echo "❌ Update failed in one or more namespaces."
        }
    }
}
