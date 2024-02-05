//Import security group module 
module "jenkins_master_security_group" {
    source                = "./infrastructure/modules/Security-group"
    allowed_ingress_ports = [80, 22, 8080]
    security_group_name   = "jenkins_sg"
}

data "aws_subnets" "subnets" {
}

module "my_ec2_instances" {
    source            = "./infrastructure/modules/ec2-module"
    instance_count    = var.instance_count
    ami_id            = var.desired_ami_id
    instance_type     = "t2.micro"
    subnet_id         = var.subnet_id
    security_group_id = [module.jenkins_master_security_group.security_group_id]

    user_data = <<-EOF
        #!/bin/bash
        # Include the main script
        $(cat "${path.module}/scripts/jenkins-master.sh")
        sudo systemctl start jenkins
    EOF


}