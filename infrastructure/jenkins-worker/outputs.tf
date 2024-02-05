output "public_dns" {
  description = "Public DNS of the created EC2 instances"
  value       = aws_instance.ec2_instance.public_dns
}

output "public_ip" {
  description = "Public IP of the created EC2 instances"
  value       = aws_instance.ec2_instance.public_ip
}
