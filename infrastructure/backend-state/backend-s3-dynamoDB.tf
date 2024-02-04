provider "aws" {

  region     = "us-east-1"
}

//s3 bucket
resource "aws_s3_bucket" "enterprice_backend_state" {
    bucket = "django-docker-ec2-backendbucket"

    lifecycle {
        prevent_destroy = true
    }
}
resource "aws_s3_bucket_versioning" "versioning_example" {
    bucket = aws_s3_bucket.enterprice_backend_state.bucket
    versioning_configuration {
        status = "Enabled"
    }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
    bucket = aws_s3_bucket.enterprice_backend_state.bucket
    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
    }
}

//locking for encryption using dynamoDB

resource "aws_dynamodb_table" "ent_backend_lock" {
  name         = "app_backend_locks"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}