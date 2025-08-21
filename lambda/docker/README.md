# AlexaSkills Lambda Docker Setup

This README explains how to build the Docker image for the AlexaSkills Lambda project.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system.

## Building the Docker Image

To build the Docker image, run the following command from the project root directory:

```bash
sudo docker build . -f docker/Dockerfile
```

This command uses the `docker/Dockerfile` to build the image.

## Next Steps

After building the image, you can run or deploy it as needed for your workflow.