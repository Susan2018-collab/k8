pipeline {

  agent { label 'jenkins' }

    triggers {
        pollSCM('* * * * *')   // check every 1 min
    }

    environment {
        NAME = "brad"
    }

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Cloning code from Git..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Running Python build..."

                sh '''
                python3 --version
                python3 python.py --name ${NAME}
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Testing..."

                sh '''
                python3 phon.py --name ${NAME}
                echo "Tests passed"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying..."

                sh '''
                echo "Deploy step for ${NAME}"
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo "SUCCESS ✅"
        }
        failure {
            echo "FAILED ❌"
        }
    }
}
