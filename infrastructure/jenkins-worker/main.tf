terraform {
    backend "s3" {
        bucket = "flask-docker-ec2-backendbucket"
        key = "remoteBackend/jenkinsWorkerState"
        region = "us-east-1"
        dynamodb_table = "app_backend_locks"
        encrypt = true
    }
}

provider "aws" {
    region = "us-east-1"
}