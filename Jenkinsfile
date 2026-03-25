pipeline {
    agent any

    stages {
        stage('Scale nginx deployment in DEV') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    echo 'Scaling nginx deployment in DEV namespace to 2 replicas...'
                    sh 'kubectl scale deployment nginx-deployment --replicas=2 -n dev'
                }
            }
        }

        stage('Scale nginx deployment in PROD') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-id', variable: 'KUBECONFIG')]) {
                    echo 'Scaling nginx deployment in PROD namespace to 2 replicas...'
                    sh 'kubectl scale deployment nginx-deployment-prod --replicas=2 -n prod'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Scaling completed successfully!'
        }
        failure {
            echo '❌ Scaling failed. Please check the logs.'
        }
    }
}
