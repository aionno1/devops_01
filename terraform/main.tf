provider "aws" {
    region = "us-east-1"
}

resource "aws_instance" "devops_01" {
    ami = "ami-04b9e92b5572fa0d1"
    instance_type = "t2.micro"
    key_name = "devops_01_ssh"

    tags = {
        Name = "web"
    }
}

resource "aws_instance" "devops_02" {
    ami = "ami-04b9e92b5572fa0d1"
    instance_type = "t2.micro"
    key_name = "devops_01_ssh"

    tags = {
        Name = "jenkins"
    }
}

