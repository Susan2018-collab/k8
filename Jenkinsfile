pipeline {
    agent any
    environment {
        // Path to kubeconfig inside Jenkins container
        KUBECONFIG = '/var/jenkins_home/.kube/config'
    }
    stages {
        stage('Scale DEV Deployment') {
            steps {
                echo "Scaling Nginx deployment in DEV namespace..."
                // Get current replicas
                script {
                    def currentReplicas = sh(
                        script: "kubectl get deployment nginx-deployment -n dev -o jsonpath='{.spec.replicas}'",
                        returnStdout: true
                    ).trim()
                    echo "Current DEV replicas: ${currentReplicas}"

                    // Scale to 2 replicas (example)
                    sh "kubectl scale deployment nginx-deployment --replicas=2 -n dev"
                    echo "DEV deployment scaled to 2 replicas."
                }
            }
        }

        stage('Scale PROD Deployment') {
            steps {
                echo "Scaling Nginx deployment in PROD namespace..."
                script {
                    def currentReplicas = sh(
                        script: "kubectl get deployment nginx-deployment-prod -n prod -o jsonpath='{.spec.replicas}'",
                        returnStdout: true
                    ).trim()
                    echo "Current PROD replicas: ${currentReplicas}"

                    // Scale to 3 replicas (example)
                    sh "kubectl scale deployment nginx-deployment-prod --replicas=3 -n prod"
                    echo "PROD deployment scaled to 3 replicas."
                }
            }
        }
    }
    post {
        success {
            echo "✅ Scaling completed successfully!"
        }
        failure {
            echo "❌ Scaling failed. Check logs."
        }
    }
}
