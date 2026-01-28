# End to end Linear regression Project

This project implements a linear regression model to predict house prices based on various features. The model is trained using the provided dataset and can be used to make predictions on new data.

## Table of Contents
- [Live Demo](#live-demo)
- [Local Setup](#local-setup)
  - [Training the Model](#training-the-model)
- [Docker Setup](#docker-setup)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [Using DockerHub Image](#using-dockerhub-image)
  - [Pulling the Image](#pulling-the-image)
  - [Running the Container](#running-the-container)

## Live Demo

The application can be containerized using Docker for easy deployment.

## Local Setup

Clone the repository:

```bash
git clone https://github.com/rashedulalbab253/end_to_end_Ml_Linear_Regression.git
cd end_to_end_Ml_Linear_Regression
```

Create a virtual environment:

**Windows:**
```bash
python -m venv env
env/scripts/activate
```

**macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

### Training the Model

To train the model, run the training script:

#### On Windows:
```bash
python train.py
```

#### On Ubuntu/Linux:
```bash
python3 train.py
```

If you encounter any issues on Ubuntu, ensure you have proper permissions:
```bash
chmod +x train.py
python3 train.py
```

## Docker Setup

### Building the Docker Image

Build the Docker image using the Dockerfile provided in the repository:

```bash
docker build -t end-to-end-ml-linear-regression .
```

### Running the Docker Container

Run the Docker container with:

```bash
docker run -p 8000:8000 end-to-end-ml-linear-regression
```

This will:
1. Start the container
2. Expose the prediction API on port 8000
3. Load the pre-trained model

## Using DockerHub Image

### Pulling the Image

Pull the pre-built Docker image from DockerHub:

```bash
docker pull rashedulalbab253/end-to-end-ml-linear-regression:latest
```

### Running the Container

Run the container from the DockerHub image:

```bash
docker run -p 8000:8000 rashedulalbab253/end-to-end-ml-linear-regression
```
