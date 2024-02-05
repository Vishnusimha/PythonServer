variable "aws_key_pair" {
    default = "~/aws/aws_keys/default-ec2.pem"
}

variable "desired_ami_id" {
    description = "The required AMI ID"
    default     = "ami-0c7217cdde317cfec"
}

variable "instance_count" {
    description= "To select number of instances"
    default = 1
}

variable "subnet_id" {
  # Define your default subnet ID
  default = "subnet-0373cf7aaf2597384"
}

