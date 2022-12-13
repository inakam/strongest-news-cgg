resource "aws_alb" "alb" {
  name                       = var.name
  security_groups            = [aws_security_group.cgg-framework-lb.id]
  subnets                    = [var.public_subnet_1a, var.public_subnet_1c]
  internal                   = false
  enable_deletion_protection = false

  access_logs {
    bucket  = aws_s3_bucket.alb_log.bucket
    enabled = true
  }
}

resource "aws_alb_listener" "alb" {
  load_balancer_arn = aws_alb.alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_alb_target_group.blue.arn
    type             = "forward"
  }

  lifecycle {
    ignore_changes = [default_action]
  }
}

resource "aws_alb_target_group" "blue" {
  name        = "${var.name}-tg-b"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.vpc_id

  health_check {
    interval            = 30
    path                = "/"
    protocol            = "HTTP"
    timeout             = 5
    unhealthy_threshold = 2
    matcher             = 200
  }
}

resource "aws_alb_target_group" "green" {
  name        = "${var.name}-tg-g"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = var.vpc_id

  health_check {
    interval            = 30
    path                = "/"
    protocol            = "HTTP"
    timeout             = 5
    unhealthy_threshold = 2
    matcher             = 200
  }
}
