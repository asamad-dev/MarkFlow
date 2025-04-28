
---

    # 🐳 Second: `Dockerfile`
    
    Create a file `Dockerfile` at the root:
    
    ```dockerfile
    # Use official Python image
    FROM python:3.11-slim
    
    # Set environment variables
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    # Set work directory
    WORKDIR /code
    
    # Install dependencies
    COPY requirements.txt /code/
    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt
    
    # Copy project
    COPY . /code/
    
    # Expose port
    EXPOSE 8000
    
    # Run the server
    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    