# Define variables

variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "vpc_cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

variable "public_subnet_cidr_block_1" {
  type    = string
  default = "10.0.1.0/24"
}

variable "public_subnet_cidr_block_2" {
  type    = string
  default = "10.0.2.0/24"
}

variable "private_subnet_cidr_block_1" {
  type    = string
  default = "10.0.3.0/24"
}

variable "private_subnet_cidr_block_2" {
  type    = string
  default = "10.0.4.0/24"
}

variable "ami_id" {
  type    = string
  default = "ami-0c94855ba95c71c99" # Amazon Linux 2 AMI ID for us-east-1
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "key_name" {
  type    = string
  default = "heba"
}

variable "dynamo_table" {
  type    = string
  default = "terraform-state-locks"
}

variable "bucket_name" {
  description = "The name of the S3 bucket where the object is stored"
  type    = string
  default = "terraform-statefile1999"
}

variable "object_key" {
  description = "The key of the object in the S3 bucket"
  type    = string
  default = "terraform.tfstate"
}

# Use the aws_ami data source to get the latest Amazon Linux 2 AMI ID
data "aws_ami" "amazon_linux_2" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }
}

data "aws_ami" "ubuntu_20_04" {
  most_recent = true

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"]  # Canonical owner ID for us-east-1 region
}