pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nginx:latest'  // your image to scan
    }

    stages {
        stage('Security Scan') {
            steps {
                echo "Scanning container image for vulnerabilities using Trivy..."
                script {
                    // Install Trivy if not already installed (optional for Jenkins agents)
                    sh '''
                    if ! command -v trivy &> /dev/null
                    then
                        echo "Trivy not found, installing..."
                        brew install aquasecurity/trivy/trivy || curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh
                    fi
                    '''

                    // Run the security scan
                    def result = sh(
                        script: "trivy image --severity HIGH,CRITICAL --exit-code 1 ${IMAGE_NAME}",
                        returnStatus: true
                    )

                    if (result != 0) {
                        error "Security scan failed: HIGH or CRITICAL vulnerabilities found in ${IMAGE_NAME}"
                    } else {
                        echo "Security scan passed: No HIGH or CRITICAL vulnerabilities found."
                    }
                }
            }
        }
    }
}
