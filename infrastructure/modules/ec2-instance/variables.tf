variable "instance_count" {
  description = "Number of EC2 instances to create"
  default     = 1
}

variable "ami_id" {
  description = "AMI ID for the EC2 instance"
}

variable "instance_type" {
  description = "Instance type for the EC2 instance"
}

variable "subnet_id" {
  description = "Subnet ID where EC2 instance will be launched"
}

variable "security_group_id" {
  description = "Security Group ID for the EC2 instance"
}

variable "user_data" {
  description = "User data for EC2 instances"
}

