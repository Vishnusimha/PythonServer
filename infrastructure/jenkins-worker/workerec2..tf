//Import security group module 
module "jenkins_worker_security_group" {
    source                = "./infrastructure/modules/Security-group"
    allowed_ingress_ports = [80, 22, 8080, 50000]
    security_group_name   = "jenkins_sg"
}

data "aws_subnets" "subnets" {
}

//This is configured in HashiCorp Vault and this is the path for it
//vault kv list secrets
data "vault_generic_secret" "jenkins_worker" {
  path = "secrets/jenkins-worker"
} 

module "my_ec2_instances" {
    source            = "./infrastructure/modules/ec2-module"
    instance_count    = var.instance_count
    ami_id            = var.desired_ami_id
    instance_type     = "t2.micro"
    subnet_id         = var.subnet_id
    security_group_id = [module.jenkins_worker_security_group.custom_sg.id]

    user_data = <<-EOF
        #!/bin/bash
        # Include the main script
        $(cat "${path.module}/scripts/jenkins-worker.sh")
        sudo systemctl start jenkins
    EOF

    tags = {
        Name = "Jenkins-Master-Instance"
    }
}