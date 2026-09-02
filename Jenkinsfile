pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Python program'
                bat '"C:\\Users\\CHATTA NATHAN ARUN\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m py_compile factorial.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing Python program'
                bat '"C:\\Users\\CHATTA NATHAN ARUN\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" factorial.py'
            }
        }
    }
}