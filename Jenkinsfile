pipeline {
    agent any

    triggers {
        githubPush()
        cron('H 5 * * *')
    }

    stages {
        stage('Clone from GitHub') {
            steps {
                echo 'Fetching latest code from GitHub repository'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Checking workspace files'
                sh 'ls -la'
                echo 'Building the Docker image for Python app'
                sh 'docker build -t python-jenkins-task .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running the Docker container'
                sh 'docker run -d -p 5000:5000 --name python-jenkins-task-container python-jenkins-task'
                echo 'Container started successfully at http://localhost:5000'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage in progress'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment and removing old containers'
            sh 'docker stop python-jenkins-task-container || true'
            sh 'docker rm python-jenkins-task-container || true'
            cleanWs()
            echo 'Cleanup completed. Pipeline finished'
        }
    }
}
