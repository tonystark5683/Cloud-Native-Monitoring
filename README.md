

# Cloud Native Monitoring Application


Welcome to the Cloud Native Monitoring Application! This project aims to provide a robust DevOps solution for monitoring cloud-native applications using Docker, AWS, and Kubernetes.

## Features

- Docker containerization for efficient application deployment and management.
- Seamless integration with AWS for easy configuration and access to cloud services.
- Creation of an ECR (Elastic Container Registry) repository using the Boto3 library.
- Pushing Docker images to the ECR repository for centralized and reliable deployment.
- Kubernetes Deployment manifest file to deploy the application on a Kubernetes cluster.

## Installation

1. Clone the repository
2. Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
3. Set up an AWS account and configure it with your local machine.
4. Install the required Python dependencies: `pip install -r requirements.txt`
5. Configure the Kubernetes cluster and ensure it is ready for deployment.
6. Apply the Kubernetes Deployment manifest file: `kubectl apply -f deployment.yaml`

## Usage

1. Build the Docker container: `docker build -t monitoring-app .`
2. Tag the Docker image with the ECR repository details: `docker tag monitoring-app aws-account-id.dkr.ecr.region.amazonaws.com/repository-name`
3. Push the Docker image to the ECR repository: `docker push aws-account-id.dkr.ecr.region.amazonaws.com/repository-name`
4. Verify the successful deployment on the Kubernetes cluster: `kubectl get pods`

## Contributing

Contributions are welcome! If you'd like to contribute to the Cloud Native Monitoring Application, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m "Add your changes"`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request.



## Acknowledgements

I would like to express my gratitude to Nasiullah Chaudhari for their valuable guidance and support throughout this project.

