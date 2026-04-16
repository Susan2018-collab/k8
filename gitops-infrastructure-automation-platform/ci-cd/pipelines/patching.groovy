def call() {

    pipeline {
        agent any

        parameters {
            string(name: 'EMAIL_TO', defaultValue: 'susan.joffin@gmail.com', description: 'Report recipient')
            choice(name: 'ENV', choices: ['test', 'prod'], description: 'Target environment')
        }

        stages {

            stage('Apply Security Patches') {
                steps {
                    sh """
                    ansible-playbook \
                    -i infrastructure/ansible/inventory/hosts.ini \
                    infrastructure/ansible/patching.yml \
                    --extra-vars "email_to=${params.EMAIL_TO} env=${params.ENV}"
                    """
                }
            }

            stage('Validation') {
                steps {
                    sh """
                    echo "Running post-patch validation for ${params.ENV}"
                    """
                }
            }

        }

        post {
            success {
                echo "Patching successful for ${params.ENV}"
            }

            failure {
                echo "Patching FAILED for ${params.ENV}"
            }
        }
    }
}
