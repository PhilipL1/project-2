
## Contents
* [Introduction](#introduction) 
  * [Objective](#objective)
  * [Proposal](#proposal)
* [Architecture](#architecture)
  * [Risk Assessment](#Risk-Assessment)
  * [Project Management](#Project-Management)
  * [Test Analysis](#Analysis-of-Testing)
  * [Continuous Integration pipeline](#continuous-integration)
* [Infrastructure](#development)
  * [Jenkins](#Jenkins)
  * [Entity Diagram](#Entity-Diagram)
  * [Docker Swarm](#Interactions-Diagram)
  * [The 4 Services](#The-4-Services)
* [Development](#development)
  * [Unit Testing](#Unit-Testing)
  * [Front-End Design](#Front-End)
* [Footer](#Footer)
* 
## Introduction

### Objective
The objective provided for this project is as follows:
> To create a service-orientated architecture for your application, this application must be composed of at least 4 services that work together.
<br/>

More specifically, these 4 services should comprise of 1 front-end wrapper service, 2 (or more) back-end services, and 1 other back-end service that relies on data from the previous 2 back-end services in some way.

For this to be achieved, the following is required:
* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git - using the feature-branch model
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Reverse Proxy: NGINX
* Database Layer: MySQL

### Proposal

To meet all of the requirements and to ensure the MVP was produced in the time-frame provided. I first had to concure the important aspect of the project which were the infrastructure and implementation of my CI/CD. This meant a basic application that hit the MVP requirements was create in the first sprint. 

### Fortune Generator 
* Service 1 (front-end): displays the results of the following 3 services for the user to see, as well as a brief history of past results.
* Service 2: returns a random number for the fortune. 
* Service 3: a random date from a given range is formed. The day of that random date is then calculated. The date and day is then returned.
* Service 4: returns a fortune is generated based on the random number. The date and day that the fortune will take place will also be returned.

# Architecture
## Risk Assessment
My detailed Risk Assessment can be seen below, outlining the major and minor risks associated with this project.
<br/>
Here is a screenshot of my risk assessment at the start of my project :
<br/>

![risk assessment image](https://i.imgur.com/RkGAg0G.png)
<br/><br/>
Below is a screenshot of additional risks that where added at the end of my project when the risks became clear :
<br/>

![risk assessment image2](https://i.imgur.com/knTGlbx.png)
<br/>

The full risk assessment for this project can be found [here](https://docs.google.com/spreadsheets/d/1mq4bsv15Pg1NkuiAYihON9s1pke3uN9twct9S83Fh0c/edit?usp=sharing). 
<br/>

## Project Management 
Trello was used to track the progress of the project (pictured below). You can find the link to this board [here](https://trello.com/b/4UYzCR2H). I used Trello board rather than other project management tools such as Jira because it is free to use and user friendly which helps with visualisation of the project so that task can be completed efficiently.  
<br/>

![trello board image 1](https://i.imgur.com/xRolMUn.png)
![trello board image 2](https://i.imgur.com/qeHTB02.png)
<br/>

## Analysis of Testing
Having a test driven approach is essential for any successful project. Since this project is using an CI/CD approach, it is key to plan out what areas of the application will need to be tested. Also, to implement a system to run automated tests. 
<br/>
To start this process, I first had to understand the scope of the testing for this project.
<br/>

![image of testing](https://i.imgur.com/FxDBNDQ.png)
<br/>
Based on this result and the Moscow priorisitation, it is clear that unit testing is the only essential form of testing required to produce the MVP. 
I then went on to plan the test that needed to be done, as well as pseudo-code for my own personal reference as a kick start before writing my code. This tables helped me keep track on what test needs to be implemented.
![image of testing 2](https://i.imgur.com/OX0APtR.png)
<br/>

[View the original documentation](https://docs.google.com/spreadsheets/d/1wvi8PupgVidEtxT-IOtfdUEc5q0HvxSPXRxG-yZY_QA/edit?usp=sharing)
<br/>

# Infrastructure 
Continuous deployment is implemented throughout my project in order to allow rapid and smooth development-to-deployment. The approach I have taken allows deploying new versions of the application with limited down-time.

## Jenkins
Whenever new content is pushed to the dev branch, Github will send a webhook to Jenkins which tells it to run the following pipeline:

**1.** Unit Test: Pytest

```
Test the functionality of individual routes 
```
<br/>

**2. & 3.** Build & Push: docker-compose
```
Jenkins' credentials system is used to handle logging into DockerHub, before the new images are  pushed to the repository specified.
```
<br/>

**4.** Configure: ansible
```
Ansible configures several things:

Installing dependencies (such as docker and docker-compose),
Setting up the swarm, and joining the swarm on all worker nodes,
Reloading NGINX with any changes to the nginx.conf file.
```
<br/>

**5** Deploy: docker swarm/stack
```
Jenkins copies the docker-compose.yaml file over to the manager node, SSH's onto it, and then runs docker stack deploy
```
<br/>

The commands used in Jenkins' pipeline can be seen in the[ Jenkinsfile](https://github.com/PhilipL1/project-2/blob/test/jenkins/Jenkinsfile)
<br/>

![pipeline image](https://i.imgur.com/qKtGg9A.png)

## Entity Diagram 
The project database only has one table which is shown below. Outlining the elements in a table means that the validation required for each element is outlined explicitly, and can be tested accordingly. The results of the fortune is stored in the SQL database, so if the end-user previous Fortune it is available upon request.  
<br/>
![Entity Diagram image](https://i.imgur.com/4FlhZgg.png)

## Interactions Diagram
The diagram below shows the layout of the virtual machines as used in this project. This displays where the information is taken from as a user connects to the NGINX machine on port 80.
<br/>

![user interface image](https://i.imgur.com/KGv5xpO.png)
<br/>
Using an orchestration tool (ansible), Docker Swarm. software developers are able to create a network of virtual machines that are all able to be accessed by end-users to provide the same service. 
<br/>
Anonther layer has been added to the system in a form of an NGINX load-balancer which  up-streams the user to the VM with the least connections. By adding this layer, the efficiency of the application improves as well as security as end-users have another stage in the application.
<br/>

 ## The 4 Services
 The diagram below shows how the services interact with one another. 
 <br/>
 ![services](https://i.imgur.com/ho2SPg1.png)
 Summary
 * The front-end sends GET requests to API-1 and API-2
 * API-1 & API-2 sends their response to API-3 as a POST request 
 * API-3 returns the appropriate information to the front end as a POST request 
 * The front-end can send requests to the MySQL instance to INSERT the new entry and SELECT the old entries in order to display a history to the user as required.
 <br/>

 ## Development
 ### Front-End 
 When navigating to port 80 (default http port) on the NGINX's IP, the steps the end user will be taking has been mentioned previously, using a these diagram to help visualise the structure [here](https://i.imgur.com/ho2SPg1.png) and [here](https://i.imgur.com/KGv5xpO.png). The relevant information is displayed using HTML (with jinja2) for layout and CSS for styling. 
 ![web application](https://i.imgur.com/Z41L2Y4.png)
 
 ### Unit Testing 
 Unit testing is used here by seperating the route functions and testing each function with various scenarios. Each function should return the expected response under each given scenario for the test to be successful. These tests are run automatically after every Git push using Jenkins. Jenkins prints out whether or not the tests were successsful.Each tests were ran individual using a bash for-loop.
 <br/>

 ![test 1](https://i.imgur.com/NOH1JTA.png)
 ![test 2](https://i.imgur.com/T0Jj64y.png)
 ![test 3](https://i.imgur.com/vAz7FUa.png)
 ![test 4](https://i.imgur.com/5bePqpg.png)
 <br/>

A coverage report is also displayed noting the percentage of the application that was tested. This information helps the developer understand how much of the code in the app has been successfully tested.
If any of the unit testing fails, the entire Jenkins build is marked as a fail. However, this project had a 100% coverage indicating efficiency as all the lines in  in each of my routes was fully tested and there were no unnecessary syntax in my code.
<br/>

The results also produces a junit.xml file which is used by the Jenkins Junit plug-in to produce advanced testing reports, further easing traceback for the developer.

## Footer
### Future Improvements
* Using Integration testing to test the app as a whole, by the selenium approach would be ideal.
* Add a background colour for each fortune so the application is more apealing to end-users
* add functionality that allows user to input data. 
### Author
Philip Lartey

### Acknowledgements
* [Harry Volker](https://github.com/htr-volker)
* [Oliver Nichols](https://github.com/OliverNichols)