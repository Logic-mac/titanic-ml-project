pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Logic-mac/titanic-ml-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    . venv/bin/activate
                    python train.py
                '''
            }
        }

        stage('Run Prediction') {
            steps {
                sh '''
                    . venv/bin/activate
                    python predict.py
                '''
            }
        }
    }
}
