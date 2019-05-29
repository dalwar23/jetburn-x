/*
File: Jenkinsfile
Author: Dalwar Hossain (dalwar.hossain@protonmail.com)
Copyright: Dalwar Hossain
*/

pipeline {
    agent any
    environment {
        REPOSITORY_NAME = sh (script: 'echo $(echo "${JOB_NAME}" | cut -d "/" -f 1)', returnStdout: true).trim()
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '1'))
    }
    stages {
        stage ('Sanity Check') {
            parallel {
                stage ('Check Python3') {
                    steps {
                        sh 'python3 --version'
                    }
                }
                stage ('Python3 virtualenv') {
                    steps {
                        sh 'virtualenv --version'
                    }
                }
                stage ('Check Setup') {
                    steps {
                        sh 'test -f setup.py'
                        sh 'echo \$?'
                    }
                }
            }
        }
        stage ('Policy Check') {
            environment {
                SCANNER_HOME = tool 'ScannerQube'
                PROJECT_VERSION = sh (script: 'python3 setup.py --version', returnStdout: true).trim()
            }
            steps {
                withSonarQubeEnv ('SonarQube') {
                    /*
                    Double quote is necessary for variable management in groovy syntax
                    REPOSITORY_NAME is a custom ENV Variable that resolves to
                    REPOSITORY_NAME=$(echo $JOB_NAME | cut -d '/' -f 1)
                    [Valid only for multibranch pipeline]
                    */
                    sh "${SCANNER_HOME}/bin/sonar-scanner " +
                    "-Dsonar.projectKey=${REPOSITORY_NAME}-${BRANCH_NAME} " +
                    "-Dsonar.projectName=${REPOSITORY_NAME}-${BRANCH_NAME} " +
                    "-Dsonar.projectVersion=${PROJECT_VERSION} " +
                    "-Dsonar.sources=. "
                }
            }
        }
        stage ('Quality Gate') {
            /*
            1. SonarQube server 6.2+ is required
            2. A web-hook in SonarQube server pointing to <jenkins server>/sonarqube-webhook/ (The trailing slash is important)
            3. Use withSonarQubeEnv step in your pipeline (so that SonarQube taskId is correctly attached to the pipeline context).
            */
            steps {
                timeout (time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage ('Initialize') {
            steps {
                sh '''
                virtualenv --always-copy -p python3 venv
                source venv/bin/activate
                pip install --upgrade pip
                pip --version
                '''
            }
        }
        stage ('Pre-Build') {
            parallel {
                stage ('Dev Dependencies') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        pip install --upgrade setuptools wheel twine
                        deactivate
                        '''
                    }
                }
                stage ('Pkg Dependencies') {
                    when {
                        expression {
                            fileExists('requirements.txt')
                        }
                    }
                    steps {
                        sh '''
                        source venv/bin/activate
                        pip install -r requirements.txt
                        deactivate
                        '''
                    }
                }
            }
        }
        stage ('Build') {
            steps {
                sh '''
                source venv/bin/activate
                python3 setup.py build
                deactivate
                '''
            }
        }
        stage ('Package') {
            parallel {
                stage ('Source') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python3 setup.py sdist
                        deactivate
                        '''
                    }
                }
                stage ('Wheel') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python3 setup.py bdist_wheel
                        deactivate
                        '''
                    }
                }
                stage ('Egg') {
                    steps {
                        sh '''
                        source venv/bin/activate
                        python3 setup.py bdist_egg
                        deactivate
                        '''
                    }
                }
            }
        }
        /*stage ('Deploy') {
            parallel {
                stage ('Archive Artifacts') {
                    steps {
                        archiveArtifacts artifacts: 'dist/*'
                    }
                }
                stage ('Upload to Artifactory') {
                    when {
                        anyOf {
                            branch 'master'
                            branch 'dev'
                        }
                    }
                    steps {
                        rtUpload (
                            serverId: "JFrog-local",
                            buildName: "${REPOSITORY_NAME}-${BRANCH_NAME}",
                            buildNumber: "${BUILD_NUMBER}",
                            specPath: 'jfrog-spec.json',
                            failNoOp: true
                        )
                    }
                }
            }
        }
        stage ('Publish Build Info') {
            when {
                anyOf {
                    branch 'master'
                    branch 'dev'
                }
            }
            steps {
                rtPublishBuildInfo (
                    serverId: "JFrog-local",
                    buildName: "${REPOSITORY_NAME}-${BRANCH_NAME}",
                    buildNumber: "${BUILD_NUMBER}"
                )
            }
        }*/
    }
}
