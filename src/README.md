
# Before Getting Started

Before getting started, make sure you have Docker installed.

# Setting Up

To build the Docker image, run the following command in the Terminal or on WSL if on Windows:

```bash
docker build -t back-end .
```

To run the app, we use docker-compose. Execute the command below to do so:

```bash
docker-compose build && docker-compose up -d
```

# Shutting Down Machine

To shut down the machine, we also use docker-compose. Use the command below:

```bash
docker-compose down
```
