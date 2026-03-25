pipeline {
    agent any

    environment {
        DEV_NS = "dev"
        PROD_NS = "prod"
        DEPLOYMENT_DEV = "nginx-deployment"
        DEPLOYMENT_PROD = "nginx-deployment-prod"
    }

    stages {
        stage('Scale DEV Deployment') {
            steps {
                echo "Scaling DEV deployment..."
                sh '''
                    # Get current replicas
                    CURRENT=$(kubectl get deployment $DEPLOYMENT_DEV -n $DEV_NS -o jsonpath='{.spec.replicas}')
                    echo "Current DEV replicas: $CURRENT"
                    # Increment replicas by 1
                    NEW=$((CURRENT+1))
                    kubectl scale deployment $DEPLOYMENT_DEV --replicas=$NEW -n $DEV_NS
                    echo "Scaled DEV deployment to $NEW replicas"
                '''
            }
        }

        stage('Scale PROD Deployment') {
            steps {
                echo "Scaling PROD deployment..."
                sh '''
                    # Get current replicas
                    CURRENT=$(kubectl get deployment $DEPLOYMENT_PROD -n $PROD_NS -o jsonpath='{.spec.replicas}')
                    echo "Current PROD replicas: $CURRENT"
                    # Increment replicas by 1
                    NEW=$((CURRENT+1))
                    kubectl scale deployment $DEPLOYMENT_PROD --replicas=$NEW -n $PROD_NS
                    echo "Scaled PROD deployment to $NEW replicas"
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Scaling completed successfully!"
        }
        failure {
            echo "❌ Scaling failed!"
        }
    }
}
