pipeline {
    agent {node {label 'aliyun_ecs_linux_p4_2'}}
    options {
        timestamps()
    }

    parameters{
        choice choices: ['branch', 'tag'], description: 'git branch or git tag version to build', name: 'GIT_KEY'
        string defaultValue: 'main', description: 'branch of larkbot repo', name: 'GIT_VALUE', trim: true
    }

    environment {
        CONFIG_PATH = "/mnt/lijialun/larkbot_config/sso_config.yaml"
    }

    stages {
        stage('Git checkout') {
            steps {
                dir('sso_token_service') {
                    retry(3) {
                        script {
                            def value = "${params.GIT_VALUE}"
                            if ("${params.GIT_KEY}" == "tag") {
                                value = "refs/tags/${params.GIT_VALUE}"
                            }
                            checkout([$class: 'GitSCM', branches: [[name: "$value"]], extensions: [[$class: 'CloneOption', shallow: false, depth: 0, reference: '']], userRemoteConfigs: [[credentialsId: 'github_lijialun', url: 'https://ghproxy.com/https://github.com/APX103/sso_token_service.git']]])
                        }
                    }
                }
            }
        }

        stage('Build & Start Service') {
            steps {
                dir('sso_token_service') {
                    script {
                        script {
                            try {
                                sh """
                                    docker stop mm_lark_bot
                                """
                            } catch(e) {
                                echo """Container not exist."""
                            }
                        }
                        sh """
                            cp ${CONFIG_PATH} ./config.yaml
                            sh build.sh
                        """
                    }
                }
            }
        }

        stage('Check Service') {
            steps {
                dir('sso_token_service') {
                    script {
                        sh """
                            docker logs sso_token_service
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
