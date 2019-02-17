pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'latexmk -pdf main.tex'
      }
    }
    stage('deploy') {
      when {
        branch 'master'
      }
      steps {
        sh '''WEB_DIR=/var/www/natestemen.com
cp main.pdf $WEB_DIR/main.pdf
rm $WEB_DIR/rudin.pdf
mv $WEB_DIR/main.pdf $WEB_DIR/rudin.pdf'''
      }
    }
  }
}
