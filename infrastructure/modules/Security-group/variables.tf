variable "allowed_ingress_ports" {
    type        = list(number)
    description = "List all required ports" 
}

variable "security_group_name" {
    type        = string
    description = "Name of Security Group"
}
