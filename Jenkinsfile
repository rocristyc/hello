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
				// run these from a docker python container (client-qe-9 has python3, setuptools and twine installed)
		                sh 'python3 setup.py sdist'
				sh 'python3 -m twine upload --verbose --repository-url http://repo-vip.tivo.com:8081/artifactory/api/pypi/pypi-local dist/*'
            		}
		}
    	}
     post { 
        always { 
            cleanWs()
        }
    }
}
