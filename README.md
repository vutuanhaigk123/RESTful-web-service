# RESTful-web-service using DOCKER container

Created a Python RESTful services using Flask and use docker to run this application.                              
First docker need to be installed. Link: https://docs.docker.com/toolbox/toolbox_install_mac/                  
once docker installed we can see docker quick terminal on our system

# Steps
1. Get inside the app folder in terminal                          
2. Build the docker image:                
   ```bash
   docker build -t flask-test-sample .
   ```
3. once the docker image is created, run the "flask-test-sample" in docker container                        
  ```bash
  docker run -d -p 5000:5000 flask-test-sample
  ```
4.Now, app will run locally. i.e, if it is run on normal terminal, address will be localhost else docker ip address.                   
  Go to http://localhost:5000/getrestuarants/  to list all restuarants data.                                   
  Go to http://localhost:5000/getrestuarants/22/ for specific restuarant with id "22" (example: 22)                        
  Go to http://localhost:5000/getrestuarants/type/pizza for specific restuarants with food type "Pizza" (example: pizza)            
  
## COMMANDS (useful)
1. List all images: docker images
2. List all containers: docker ps
3. Stop all running containers: docker stop $(docker ps -aq)
4. Remove all containers: docker rm $(docker ps -aq)                    
5. Remove all docker images: docker rmi $(docker images -q)

  
