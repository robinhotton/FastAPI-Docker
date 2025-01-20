# Use the official Python image
FROM python:3.11

# Set the working directory
WORKDIR /code

# Copy and install dependencies
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the source code
COPY ./api /code/api
COPY ./tests /code/tests

# Expose port 80
EXPOSE 80

# Start the application
# 0.0.0.0 -> allows listening on all network interfaces (so it is accessible externally)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--reload-dir", "/code/api"]
# '--reload-dir' allows more efficient monitoring of changes in the '/code/api' directory for faster updates
