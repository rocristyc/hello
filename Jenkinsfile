pipeline {
    agent { node { label 'client-qe-9.trec.tivo.com' } }

	stages {
		stage('Checkout python module repo from github') {
			steps {
                echo 'Pull latest from master'
				sh 'mkdir -p build'
				// Get master from GitHub
				checkout([  
					$class: 'GitSCM', 
					branches: [[name: 'refs/heads/master']],
					//Jenkins job will checkout from master 
					doGenerateSubmoduleConfigurations: false, 
					extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: 'build']], 
					submoduleCfg: [], 
					userRemoteConfigs: [[credentialsId: 'github-tivobot-jenkins-tivo', url: 'https://github.com/rocristyc/hello.git']]
				])
            }
		}
		stage('check my python module repo') {
            steps {
			script {
					echo 'list my dir' 
					dir('build') {
						sh 'pwd'
						sh 'ls -alh'
                        }
					}
				}
        }
    }
}
