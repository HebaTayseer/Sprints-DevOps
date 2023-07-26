resource "aws_instance" "private_instance_1" {
  ami           = data.aws_ami.ubuntu_20_04.id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.private_1.id
  vpc_security_group_ids = [aws_security_group.private.id]
  associate_public_ip_address = false

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo systemctl enable apache2
              EOF

  tags = {
    Name = "private-instance-1"
  }

  # Use local-exec to print the public IP address of the instance
provisioner "local-exec" {
  command = "echo '${aws_instance.private_instance_1.public_ip}' > all-ips.txt"
}

}

resource "aws_instance" "private_instance_2" {
  ami           = data.aws_ami.ubuntu_20_04.id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.private_2.id
  vpc_security_group_ids = [aws_security_group.private.id]
  associate_public_ip_address = false

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo systemctl enable apache2
              EOF
              
  tags = {
    Name = "private-instance-2"
  }

  # Use local-exec to print the public IP address of the instance
provisioner "local-exec" {
  command = "echo '${aws_instance.private_instance_2.public_ip}' > all-ips.txt"
}

}

resource "aws_instance" "public_instance_1" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.public_1.id
  vpc_security_group_ids = [aws_security_group.public.id]
  associate_public_ip_address = true

  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install nginx -y",
      "sudo amazon-linux-extras install nginx1 -y",
      "sudo systemctl start nginx",
      ]
  }
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/Downloads/heba.pem")
    host = self.public_ip
  }
  tags = {
    Name = "public-instance-1"
  }

  # Use local-exec to print the public IP address of the instance
provisioner "local-exec" {
  command = "echo '${aws_instance.public_instance_1.public_ip}' > all-ips.txt"
}

}

resource "aws_instance" "public_instance_2" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  key_name      = var.key_name
  subnet_id     = aws_subnet.public_2.id
  vpc_security_group_ids = [aws_security_group.public.id]
  associate_public_ip_address = true
    provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install nginx -y",
      "sudo amazon-linux-extras install nginx1 -y",
      "sudo systemctl start nginx",
      ]
  }
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/Downloads/heba.pem")
    host = self.public_ip
  }
  tags = {
    Name = "public-instance-2"
  }

  # Use local-exec to print the public IP address of the instance
provisioner "local-exec" {
  command = "echo '${aws_instance.public_instance_2.public_ip}' > all-ips.txt"
}

}