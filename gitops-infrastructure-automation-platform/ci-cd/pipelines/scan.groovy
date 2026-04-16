def call() {

    pipeline {
        agent any

        parameters {
            string(name: 'EMAIL_TO', defaultValue: 'susan.joffin@gmail.com', description: 'Report recipient')
            choice(name: 'ENV', choices: ['test', 'prod', 'all'], description: 'Target environment')
        }

        stages {

            stage('Security Vulnerability Scan') {
                steps {
                    sh """
                    ansible-playbook \
                    -i infrastructure/ansible/inventory/hosts.ini \
                    infrastructure/ansible/scan.yml \
                    --extra-vars "email_to=${params.EMAIL_TO} env=${params.ENV}"
                    """
                }
            }

        }

        post {
            always {
                echo "Security scan completed"
            }
        }
    }
}
