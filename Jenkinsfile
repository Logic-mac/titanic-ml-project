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
                sh '''
                    pip install --break-system-packages -r requirements.txt
                '''
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
    }
}
