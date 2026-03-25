pipeline {
    agent any

    stages {
        stage('Scale Nginx in DEV') {
            steps {
                echo "Scaling Nginx deployment in DEV namespace..."
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    sh '''
                        echo "Current DEV replicas:"
                        kubectl get deployment nginx-deployment -n dev -o wide
                        echo "Scaling DEV to 2 replicas..."
                        kubectl scale deployment nginx-deployment --replicas=2 -n dev
                        echo "Updated DEV replicas:"
                        kubectl get deployment nginx-deployment -n dev -o wide
                    '''
                }
            }
        }

        stage('Scale Nginx in PROD') {
            steps {
                echo "Scaling Nginx deployment in PROD namespace..."
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    sh '''
                        echo "Current PROD replicas:"
                        kubectl get deployment nginx-deployment-prod -n prod -o wide
                        echo "Scaling PROD to 3 replicas..."
                        kubectl scale deployment nginx-deployment-prod --replicas=3 -n prod
                        echo "Updated PROD replicas:"
                        kubectl get deployment nginx-deployment-prod -n prod -o wide
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
            echo "❌ Scaling failed. Check logs for details."
        }
    }
}
