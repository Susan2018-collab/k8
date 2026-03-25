pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Cloning repository..."
                git url: 'https://github.com/Susan2018-collab/k8.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo "Running a simple build step..."
                sh 'echo Hello, Jenkins! Your pipeline is working.'
            }
        }

        stage('Test') {
            steps {
                echo "Running a simple test step..."
                sh 'echo Testing complete!'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline succeeded!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
