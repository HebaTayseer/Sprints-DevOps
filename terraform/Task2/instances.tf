# Create public EC2 instance with Apache
resource"aws_instance" "public_ec2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.public.id
  associate_public_ip_address = true
  vpc_security_group_ids = [
    aws_security_group.public.id,
  ]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              service httpd start
              chkconfig httpd on
              echo "<h1>Welcome to my website!</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "public-ec2-instance"
  }
}

# Create private EC2 instance with Apache
resource "aws_instance" "private_ec2" {
  ami           = var.ami_id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.private.id
  vpc_security_group_ids = [
    aws_security_group.private.id,
  ]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              service httpd start
              chkconfig httpd on
              echo "<h1>Welcome to my website!</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "private-ec2-instance"
  }
}