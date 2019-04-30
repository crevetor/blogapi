pipeline {
  agent {
    docker {
      image 'test'
    }

  }
  stages {
    stage('test') {
      steps {
        archiveArtifacts(artifacts: 'test', onlyIfSuccessful: true)
      }
    }
  }
}