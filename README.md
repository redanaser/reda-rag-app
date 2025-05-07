# reda-rag-app
this is a minimal implementaion for QA RAG model
## Requirements
    - python 3.8 or higher
### Install python using MiniConda
1) Download and install miniconda
2) Creat a new environment using the following command
```bash
$ conda creat -n reda-rag python3.8
```
3) Activate the environment :
```bash
$ conda activate reda-rag
```
## Installation
### Install requiered variables
```bash
$ pip install -r requirements.txt
```
### Setup environment variables

```bash
$ cp .env.example .env
```
set your environment in the `env` file.
## Run Docker Compose Services

```bash
$ sudo docker compose up -d
```
`NOTE` if you are setting up your project on wsl 
make sure you run these commands before composing up docker-compose.yml

```bash
$ mkdir ./mongodb
$ sudo chown -R 999:999 ./mongodb
```
after running these commands compose up the docker-compose.yml (make sure both docker desktop and docker extinsion for vs code are installed)

## Run fastapi server
using uvicorn command :
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```