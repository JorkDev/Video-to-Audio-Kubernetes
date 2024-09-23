
# Video-to-Audio Microservices App on Kubernetes

## Overview

This project is a Python-based microservices application designed to convert video files into audio. Each service is containerized with Docker and orchestrated using Kubernetes. The app uses RabbitMQ for inter-service communication and PostgreSQL for storing conversion data.

## Project Structure

```
microservices-python-app/
├── auth-server/
├── converter-module/
├── database-server/
├── notification-server/
├── k8s/
├── docker-compose.yml
└── README.md
```

## Microservices

- **Auth Server**: Handles user authentication using JWT.
- **Converter Module**: Converts videos to audio using `ffmpeg`.
- **Database Server**: Manages user and conversion data.
- **Notification Server**: Sends notifications to users regarding conversion status.
- **RabbitMQ**: Message broker for communication between microservices.

## Prerequisites

- **Docker** & **Docker Compose**
- **Kubernetes Cluster**
- **Python 3.8+**

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/JorkDev/Video-to-Audio-Kubernetes.git
cd Video-to-Audio-Kubernetes
```

### 2. Build and Run with Docker Compose
```bash
docker-compose up --build
```

### 3. Deploy to Kubernetes
```bash
kubectl apply -f k8s/
```

## Testing the Application

Once deployed, interact with the application through its REST API:

- **Login** to generate a JWT token:
  ```bash
  curl -X POST http://<auth-service-url>/login        -H "Content-Type: application/json"        -d '{"username":"user1", "password":"password1"}'
  ```
  
- **Submit a video for conversion**:
  ```bash
  curl -X POST http://<auth-service-url>/convert        -H "x-access-token: <your_jwt_token>"        -F "file=@path_to_video.mp4"
  ```

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License.
