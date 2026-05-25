pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Logic-mac/titanic-ml-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 train_model.py'
            }
        }

        stage('Run Prediction') {
            steps {
                sh 'python3 predict.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t titanic-ml-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --name titanic-container titanic-ml-app'
            }
        }
    }
}
