pipeline {
    agent any

    environment {
        KUBECONFIG_FILE = '/tmp/kubeconfig' // Temporary kubeconfig path
        DEPLOYMENT_NAME = 'nginx-deployment'
        NAMESPACE = 'dev'
        REPLICAS = '5' // Desired number of replicas
    }

    stages {
        stage('Setup Kubeconfig') {
            steps {
                // 'kubeconfig-base64' is your Jenkins string secret ID
                withCredentials([string(credentialsId: 'kubeconfig-base64', variable: 'KUBECONFIG_B64')]) {
                    sh '''
                        echo "$KUBECONFIG_B64" | base64 --decode > $KUBECONFIG_FILE
                        kubectl --kubeconfig=$KUBECONFIG_FILE config view
                    '''
                }
            }
        }

        stage('Scale Deployment') {
            steps {
                sh '''
                    echo "Scaling deployment $DEPLOYMENT_NAME in namespace $NAMESPACE to $REPLICAS replicas"
                    kubectl --kubeconfig=$KUBECONFIG_FILE scale deployment $DEPLOYMENT_NAME --replicas=$REPLICAS -n $NAMESPACE
                    
                    echo "Verifying scaling..."
                    kubectl --kubeconfig=$KUBECONFIG_FILE get deployment $DEPLOYMENT_NAME -n $NAMESPACE -o wide
                '''
            }
        }
    }

    post {
        always {
            // Clean up temporary kubeconfig
            sh 'rm -f $KUBECONFIG_FILE'
        }
    }
}
