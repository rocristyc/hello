pipeline {
    agent { node { label 'client-qe-9.trec.tivo.com' } }
    environment {
	ARTIFACTORY_CREDS	= credentials('artifactory-deploy')
	TWINE_USERNAME		= "${ARTIFACTORY_CREDS_USR}"  
        TWINE_PASSWORD		= "${ARTIFACTORY_CREDS_PSW}"
    }

	stages {
		stage('Checkout python module repo from github') {
			steps {
		                echo 'Pull latest from master'
				sh 'ls -al'
				sh 'python3 setup.py sdist'
				//sh 'python3 -m twine upload --repository tivo dist/*'
				sh 'python3 -m twine upload --repository-url http://repo-vip.tivo.com:8081/artifactory/api/pypi/pypi/simple --non-interactive dist/*'
            		}
		}
    	}
     post { 
        always { 
            cleanWs()
        }
    }
}
