#Base Image - Build Stage
FROM python:3.8-slim AS build
WORKDIR /app

#metadata
LABEL maintainer="Nithin"
LABEL description="This is a Flask application and target is to setup jenkins and deploy in AWS"

#Execution steps for logging and monitoring purpose
# It ensures that the logs and outputs are immediately visible in real-time
ENV PYTHONUNBUFFERED 1
#Copy only requirements to leverage Docker Cache
COPY requirements.txt .

#Install dependencies
RUN pip install -r requirements.txt

#Production Stage
FROM build AS production
WORKDIR /app
#Copy only necessary files from BuildStage
COPY . .

#Create a non-root user
RUN useradd -ms /bin/bash myuser
USER myuser

#Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

#Exposing the port
EXPOSE 5000

#Running final application
CMD ["python3", "-m", "flask", "run"]
