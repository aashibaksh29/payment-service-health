pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t payment-service-health:latest .'
            }
        }

        stage('Tag') {
            steps {
                sh 'docker tag payment-service-health:latest payment-service-health:${BUILD_NUMBER}'
            }
        }

        stage('Health check') {
            steps {
                sh '''
                    docker rm -f payment-service-jenkins || true

                    docker run -d \
                        --name payment-service-jenkins \
                        -p 5002:5001 \
                        -e ENVIRONMENT=development \
                        payment-service-health:${BUILD_NUMBER}

                    sleep 5

                    curl --fail http://localhost:5002/health

                    docker rm -f payment-service-jenkins
                '''
            }
        }
    }
}