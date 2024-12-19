# FastAPI-Docker

This is an example of a FastAPI application using MariaDB as a database, fully containerized with Docker.

## Project Structure

```bash
.
├── api/                # Application source code
├── tests/              # Test files

├── .gitignore          # Files and directories to ignore in Git
├── Dockerfile          # Dockerfile to build the FastAPI app
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (e.g., database URL)
└── README.md           # Project documentation
```

## Running the Application

### 1. Build the Application

To build the Docker image and start the containers:

```bash
docker-compose up --build
```

The application will be accessible at:  
**[http://localhost:80](http://localhost:80)**

### 2. Run the Application

To start the application without rebuilding:

```bash
docker-compose up
```

The application will again be accessible at:  
**[http://localhost:80](http://localhost:80)**

### 3. Stop the Application

To stop and remove the containers:

```bash
docker-compose down
```

## Running Tests

### Option 1: Run Tests in Docker Compose

Run the following command to execute the tests within the FastAPI container:

```bash
docker-compose run --rm tests
```

### Option 2: Run Tests in the FastAPI Container

Access the FastAPI container shell and run the tests manually:

```bash
docker-compose exec fastapi bash
pytest
```
