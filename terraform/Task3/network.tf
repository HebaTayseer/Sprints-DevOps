
# Create VPC, subnets, and Internet Gateway
resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidr_block

  tags = {
    Name = "my-vpc"
  }
}

resource "aws_subnet" "public_1" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = var.public_subnet_cidr_block_1
  map_public_ip_on_launch = true
  availability_zone = "us-east-1a"

  tags = {
    Name = "public-subnet-1"
  }
}

resource "aws_subnet" "public_2" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = var.public_subnet_cidr_block_2
  map_public_ip_on_launch = true
  availability_zone = "us-east-1b"

  tags = {
    Name = "public-subnet-2"
  }
}

resource "aws_subnet" "private_1" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = var.private_subnet_cidr_block_1
  availability_zone = "us-east-1a"

  tags = {
    Name = "private-subnet-1"
  }
}

resource "aws_subnet" "private_2" {
  vpc_id     = aws_vpc.vpc.id
  cidr_block = var.private_subnet_cidr_block_2
  availability_zone = "us-east-1b"

  tags = {
    Name = "private-subnet-2"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "my-igw"
  }
}

resource "aws_route_table" "public_1" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table-1"
  }
}

resource "aws_route_table_association" "public_1" {
  subnet_id      = aws_subnet.public_1.id
  route_table_id = aws_route_table.public_1.id
}

resource "aws_route_table" "public_2" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table-2"
  }
}

resource "aws_route_table_association" "public_2" {
  subnet_id      = aws_subnet.public_2.id
  route_table_id = aws_route_table.public_2.id
}

# Create NAT Gateway and Elastic IP
resource "aws_eip" "nat" {
  vpc = true

  tags = {
    Name = "my-nat-eip"
  }
}

resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public_1.id

  tags = {
    Name = "my-nat-gateway"
  }
}

# Add NAT Gateway to Private Subnet Route Table
resource "aws_route_table" "private_1" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = {
    Name = "private-route-table-1"
  }
}

resource "aws_route_table_association" "private_1" {
  subnet_id      = aws_subnet.private_1.id
  route_table_id = aws_route_table.private_1.id
}

resource "aws_route_table" "private_2" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.nat.id
  }

  tags = {
    Name = "private-route-table-2"
  }
}

resource "aws_route_table_association" "private_2" {
  subnet_id      = aws_subnet.private_2.id
  route_table_id = aws_route_table.private_2.id
}