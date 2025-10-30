pipeline {
    agent any

    triggers {
        githubPush()
        cron('H 5 * * *')
    }

    stages {
        stage('Clone from GitHub') {
            steps {
                echo 'Starting pipeline... Fetching latest code from GitHub repository!'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Checking workspace files...'
                bat 'dir'
                echo 'Building the Docker image for our Python app...'
                bat 'docker build -t python-jenkins-task .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running the Docker container in detached mode...'
                bat 'docker run -d -p 5000:5000 --name python-jenkins-task-container python-jenkins-task'
                echo 'Container started successfully! You can access the app at http://localhost:5000'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment stage in progress... (Placeholder for future deployment steps)'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up environment and removing old containers...'
            bat 'docker stop python-jenkins-task-container || exit 0'
            bat 'docker rm python-jenkins-task-container || exit 0'
            cleanWs()
            echo 'Cleanup completed. Pipeline finished!'
        }
    }
}
