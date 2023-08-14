# About

This is an attempt to dockerize and use llama-cpp-python for inference, you can use any LLama Model for inference the requirements are pretty slim

## Build

- Please install docker and allow your user to the access groups (This is very important as not allowing user to access groups may not complete the build process)
- Clone or fork the repo into your local computer/server where docker is installed
- Please run the folowing command to build the docker container
```
docker build -t <give the container a name>:<tag>
```

It is a general good practice to use the git commit as the tag name for uniqueness of the image and container

## How to run the docker container with a custom model

In config.yml there are two places for mentioning the hugging face repo name and also point to the binary file of the model. In this example I have used the model and repo [here](https://huggingface.co/TheBloke/Llama-2-7B-GGML/tree/main)

Once the image is built and inference needs to be run you can run the following command

```
docker run -it -p <port on system>:8000 <image_name>:<tag>
```

## Inference example request

For running inference you can run the following curl command

```
curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Water water everywhere not a drop to drink"}' http://0.0.0.0:8000/chat
```

The important things to notice is that the prompt must be sent as a json input into the container with a POST request on local_host:<port>/chat endpoint

The input json will always be {"prompt": string} and output will be {"response": string}

## Development

In order to contribute you can follow the instructions below to setup the local environment

1. Create a python virtualenv using conda or virtualenv or venv My preferred method is to use miniconda and create a detailed environment
```
conda create -n <env_name> python=3.10
conda activate <env_name>
```
2. Install poetry for package management
```
pip install poetry
```
3. Install the requirements using poetry
```
poetry install
```
4. In order to maintain code style we use pre-commit hooks the first time please d0
```
pre-commit install
```
This will run pre-commit hooks everytime a commit is added



Your dev environment is ready and set to go. 

