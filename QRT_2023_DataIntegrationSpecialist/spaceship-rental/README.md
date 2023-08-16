# Spaceship Rental

## Setup, Linux or macOS
To setup the env, run the following command
```
make dep
```

To activate the virtual environment
```
source ./venv/bin/activate
```



## Run, Linux or macOS

To run the app locally

```
make run-local
```

To build the docker image

```
make build
```

To start the docker container 

```
make run-docker
```


## Run, Windows

To build and run the docker container
```
docker build -t spaceship-app .
docker run -p 8080:8080 spaceship-app
```
