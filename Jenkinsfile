pipeline{
    agent any
    environment {
        DATABASE_URI = credentials("DB_URI")  
        DOCKER_LOGIN = credentials("DOCKER_LOGIN")
        rebuild_db = "true" 
    }
    stages{
        stage('Test'){
            steps{
                sh "bash jenkins/test.sh"
            }
        }
        stage('Setup Docker'){
            steps {
                sh 'bash jenkins/setup-docker.sh'
            }
        }
        stage('Build'){
            steps{
                sh "docker-compose build --parallel "
            }
        }
        stage('Push'){
            steps{
                sh "docker-compose push"
            }
        }
        stage('Run'){
            steps{
                sh 'docker rm -f $(docker ps -qa)'
                sh "docker-compose up -d --build"
                script{
                    if (env.rebuild == 'true'){
                        sh 'pip3 install -r ./service-1/requirements.txt'
                        sh 'python3 ./service-1/create.py'
                        }
                    }    
            }
        }
    }
    post{
        always {
             // publish junit and cobertura reports
             junit '**/*.xml'
             cobertura coberturaReportFile:'coverage.xml', failNoReports:false 
        }
    }
}