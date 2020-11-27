# Arrange All

This is the code for an application to make reservations to go to certain stores, restaurants or other businesses. The idea is to create a platform that facilitates social distancing measures and makes a more pleasing and consistent experience for the customer. 

## Requirements
To run this application locally, you must have nodejs, npm, Docker and docker-compose installed. We also assume whoever is running this app has their development environment set up in WSL, Linux or MacOS.

## Running for the First Time
Most of the things that need to be done to run the application can be taken care of by Docker. However, one brief step must be taken before being able to run the Docker commands:

```bash
cd ui/aa-app/ 
npm install
```

This installs the dependencies for the frontend locally to ease access for the container to start off. It will take a couple of minutes, but it is generally a one time thing.

After this step, run the following command at the root of the project:

```bash
docker-compose build && docker-compose up -d
```

This builds and runs the network described in the docker-compose.yml file. The flag -d is to have it running in the background and not having the terminal occupied per se. It will take a couple of minutes the first time it is done, but thanks to volumes, it will be significantly faster any subsequent time.

The application will be running on the localhost:3000.

## Tearing Down the Network
To tear down the network, run the following command in the root of the project:

```bash
docker-compose down
```