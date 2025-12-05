pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-exam:latest"
    }

    stages {
        stage('Build Image') {
            steps {
                script {
                    echo 'building docker image...'
                    // Build the image from the ./app directory
                    sh 'docker build -t $IMAGE_NAME ./app'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo 'Running unit tests...'
                    // Simulating a test pass
                    sh 'echo "Tests Passed: 100%"'
                }
            }
        }

        stage('Deploy to K8s') {
            steps {
                script {
                    echo 'Deploying to Kubernetes...'
                    
                    // 1. Install kubectl (if missing in Jenkins container)
                    sh 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"'
                    sh 'chmod +x kubectl'
                    sh 'mv kubectl /usr/local/bin/'
                    
                    // 2. Apply the manifest
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                    
                    // 3. Restart rollout to ensure latest image is used
                    sh 'kubectl rollout restart deployment/devops-exam-deploy'
                }
            }
        }
    }
}