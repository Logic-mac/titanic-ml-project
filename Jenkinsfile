pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Logic-mac/titanic-ml-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Run Prediction') {
            steps {
                sh 'python predict.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t titanic-ml .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name titanic-container titanic-ml'
            }
        }
    }
}
