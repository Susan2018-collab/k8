pipeline {
    agent any

    environment {
        // Temporary KUBECONFIG path
        KUBECONFIG_PATH = '/tmp/kubeconfig'
    }

    stages {
        stage('Setup Kubeconfig') {
            steps {
                withCredentials([string(credentialsId: 'kubeconfig-base64', variable: 'KUBECONFIG_BASE64')]) {
                    sh '''
                        # Decode the base64 kubeconfig into a file
                        echo $KUBECONFIG_BASE64 | base64 --decode > $KUBECONFIG_PATH
                        chmod 600 $KUBECONFIG_PATH
                        export KUBECONFIG=$KUBECONFIG_PATH
                        kubectl config view
                    '''
                }
            }
        }

        stage('Scale Deployment') {
            steps {
                sh '''
                    export KUBECONFIG=$KUBECONFIG_PATH
                    kubectl scale deployment nginx-deployment --replicas=3 -n dev
                    kubectl get deployment nginx-deployment -n dev -o wide
                '''
            }
        }
    }

    post {
        always {
            // Clean up temporary kubeconfig file
            sh 'rm -f $KUBECONFIG_PATH'
        }
        success {
            echo 'Deployment scaled successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
