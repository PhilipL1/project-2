#!/bin/bash

#Install docker 
curl https://get.docker.com | sudo bash 

#add jenkins to docker group 
sudo usermod -aG docker jenkins 

#Log in to Docker 
docker login -u philipl1 $DOCKER_LOGIN_USR -p $DOCKER_LOGIN_PSW