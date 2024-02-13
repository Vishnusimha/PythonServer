resource "aws_default_vpc" "default" {

}

resource "aws_security_group" "custom_sg" {
    name = var.security_group_name
    
    dynamic "ingress" {
        for_each = var.allowed_ingress_ports
        content {
          from_port   = ingress.value
          to_port     = ingress.value
          protocol    = "tcp"
          cidr_blocks = ["0.0.0.0/0"]
        }      
    }
    egress {
        from_port   = 0
        to_port     = 0
        protocol    = -1
        cidr_blocks = ["0.0.0.0/0"]
    }
    tags = {
      name = var.security_group_name
    }
}