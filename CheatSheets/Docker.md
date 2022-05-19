# Docker Commands

Commands primarily come from the learnings of [Programming with Mosh](https://www.youtube.com/watch?v=pTFZFxd4hOI&t).

Self explanatory commands

    docker --version
    docker image ls
  
Build the dockerfile in current working directory ( . is the current directory)

    docker build -t <name-of-docker-image> . 

Run image (Note: will return nothing if there is no console output from dockerfile run)

    docker run <name-of-docker-image>

List docker images

    docker ps
          OR
    docker ps -a
    
Run docker image and enter the terminal

    docker run -it <name-of-docker-image>
    
## Example Dockerfile

Use dockerhub to find the base linux distrobution

    FROM node:alpine
    COPY . /app
    WORKDIR /app
    CMD node app.js
