pipeline {
    agent any

    environment {
        // You can define any additional environment variables here
    }

    stages {
        stage('Scale Nginx in DEV') {
            steps {
                echo "Scaling Nginx deployment in DEV namespace..."
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    // Scale DEV deployment to 2 replicas
                    sh '''
                        kubectl get deployment nginx-deployment -n dev
                        kubectl scale deployment nginx-deployment --replicas=2 -n dev
                        kubectl get deployment nginx-deployment -n dev
                    '''
                }
            }
        }

        stage('Scale Nginx in PROD') {
            steps {
                echo "Scaling Nginx deployment in PROD namespace..."
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    // Scale PROD deployment to 3 replicas
                    sh '''
                        kubectl get deployment nginx-deployment-prod -n prod
                        kubectl scale deployment nginx-deployment-prod --replicas=3 -n prod
                        kubectl get deployment nginx-deployment-prod -n prod
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Scaling completed successfully for DEV and PROD!"
        }
        failure {
            echo "❌ Scaling failed. Check Jenkins logs for details."
        }
    }
}
