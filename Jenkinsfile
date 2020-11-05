pipeline {
    agent { node { label 'client-qe-9.trec.tivo.com' } }

	stages {
		stage('Checkout python module repo from github') {
			steps {
		                echo 'Pull latest from master'
				sh 'ls -al'
				sh 'python3 setup.py sdist'
				sh 'python3 -m twine upload --repository tivo dist/*'
            		}
		}
    	}
     post { 
        always { 
            cleanWs()
        }
    }
}
