pipeline{
        agent any
        stages{
            stage('Make Directory'){
                steps{
                    sh "mkdir ~/fortune-test"
                }
            }
            stage('Make Files'){
                steps{
                    sh "touch ~/fortune-test/file1 ~/fortune-test/file2"
                }
            }
        }
}