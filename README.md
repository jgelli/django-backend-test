# Project Setup Guide

## Prerequisites
To run this project, you need to have <a href="https://docs.docker.com/get-docker/" target="_blank" rel="noopener noreferrer">Docker</a> installed on your machine.

## Quick Start
To start the project, you only need to run the following commands:

1. **Start the containers:**
```sh
make up
```

2. **Apply database migrations:**
```sh
make migrate
```

After these steps, the application should be up and running at <a href="http://localhost:8000" target="_blank" rel="noopener noreferrer">localhost:8000</a>.

---

## Available Commands
This project uses a `Makefile` to simplify common tasks. Below is a list of available commands:

### Build the Containers
```sh
make build
```
Builds the Docker containers.

### Start the Containers
```sh
make up
```
Starts the containers in detached mode (`-d`).

### Stop the Containers
```sh
make down
```
Stops and removes the containers.

### Create Database Migrations
```sh
make migrations
```
Generates new Django migrations based on model changes.

### Apply Migrations
```sh
make migrate
```
Applies the migrations to the database.

### Create a Superuser
```sh
make superuser
```
Creates a Django superuser for admin access.

### Seed Database with Initial Data
```sh
make seed
```
Populates the database with initial data using a predefined script.

### Run Tests
```sh
make test
```
Runs the test suite.

---

