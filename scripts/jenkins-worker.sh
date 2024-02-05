#!/bin/bash

#for All instances
sudo apt-get update

#Jenkins worker setup for 3rd instances

#Java Installation
sudo apt-get install -y openjdk-17-jdk
sudo apt-get update -y
#create a workDir for jenkins
mkdir -p /var/jenkins
#Download Jenkins worker JAR
curl -sO http://localhost:8080/jnlpJars/agent.jar
#Run Jenkins worker
java -jar agent.jar -jnlpUrl http://localhost:8080/computer/aws/jenkins-agent.jnlp -secret ${data.vault_generic_secret.jenkins_worker.data.secret} -workDir "/var/jenkins"


sudo usermod -aG jenkins ubuntu