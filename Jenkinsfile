pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'latexmk -pdf main.tex'
      }
    }
    stage('deploy') {
      steps {
        sh '''WEB_DIR=/var/www/natestemen.com
cp main.pdf $WEB_DIR/main.pdf
rm rudin.pdf
mv $WEB_DIR/main.pdf $WEB_DIR/rudin.pdf'''
      }
    }
  }
}