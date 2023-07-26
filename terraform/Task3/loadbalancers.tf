resource "aws_lb" "public_lb" {
  name               = "public-lb"
  internal           = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.public.id]
  subnets            = [aws_subnet.public_1.id, aws_subnet.public_2.id]

  tags = {
    Name = "public-lb"
  }
}

resource "aws_lb_target_group" "public_tg" {
  name               = "public-tg"
  port               = 80
  protocol           = "HTTP"
  target_type        = "instance"
  vpc_id             = aws_vpc.vpc.id

  health_check {
    enabled = true
    path    = "/"
    port    = "80"
  }


  depends_on = [
    aws_instance.public_instance_1,
    aws_instance.public_instance_2,
  ]

}

resource "aws_lb_target_group_attachment" "public_tg_attachment" {
  for_each = {
    for idx, instance_id in [
      aws_instance.public_instance_1.id,
      aws_instance.public_instance_2.id,
    ] : idx => instance_id
  }
  target_group_arn = aws_lb_target_group.public_tg.arn
  target_id        = each.value
  port             = 80
}

resource "aws_lb_listener" "public_listener" {
  load_balancer_arn = aws_lb.public_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.public_tg.arn
  }
}


resource "aws_lb" "private_lb" {
  name               = "private-lb"
  internal           = true
  load_balancer_type = "application"
  security_groups = [aws_security_group.private-lb.id]
  subnets            = [aws_subnet.private_1.id, aws_subnet.private_2.id]

  tags = {
    Name = "private-lb"
  }
}

resource "aws_lb_target_group" "private_tg" {
  name               = "private-tg"
  port               = 80
  protocol           = "HTTP"
  target_type        = "instance"
  vpc_id             = aws_vpc.vpc.id

  health_check {
    enabled = true
    path    = "/"
    port    = "80"
  }


  depends_on = [
    aws_instance.private_instance_1,
    aws_instance.private_instance_2,
  ]

}

resource "aws_lb_target_group_attachment" "private_tg_attachment" {
  for_each = {
    for idx, instance_id in [
      aws_instance.private_instance_1.id,
      aws_instance.private_instance_2.id,
    ] : idx => instance_id
  }
  target_group_arn = aws_lb_target_group.private_tg.arn
  target_id        = each.value
  port             = 80
}

resource "aws_lb_listener" "private_listener" {
  load_balancer_arn = aws_lb.private_lb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.private_tg.arn
  }
}



