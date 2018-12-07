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
        sh 'cp main.pdf /var/www/natestemen/rudin.pdf'
      }
    }
  }
}
