resource "aws_security_group" "cgg-framework" {
  description = "CGG security group"

  name = "${var.name}-security-group"
  tags = {
    "Name" = var.name
  }
  vpc_id = var.vpc_id
}

resource "aws_security_group_rule" "cgg-framework-to-out" {
  cidr_blocks = [
    "0.0.0.0/0",
  ]
  from_port         = 0
  prefix_list_ids   = []
  protocol          = "-1"
  security_group_id = aws_security_group.cgg-framework.id
  to_port           = 0
  type              = "egress"
}

resource "aws_security_group_rule" "cgg-framework-from-lb" {
  description              = "lb security group"
  from_port                = 0
  prefix_list_ids          = []
  protocol                 = "-1"
  security_group_id        = aws_security_group.cgg-framework.id
  source_security_group_id = aws_security_group.cgg-framework-lb.id
  to_port                  = 0
  type                     = "ingress"
}

resource "aws_security_group" "cgg-framework-lb" {
  description = "ELB security group"
  name        = "${var.name}-lb"
  tags = {
    "Name" = "${var.name}-lb"
  }
  vpc_id = var.vpc_id
}

resource "aws_security_group_rule" "lb-cgg-framework-from-http" {
  cidr_blocks = [
    "0.0.0.0/0",
  ]
  from_port         = 80
  prefix_list_ids   = []
  protocol          = "tcp"
  security_group_id = aws_security_group.cgg-framework-lb.id
  to_port           = 80
  type              = "ingress"
}

resource "aws_security_group_rule" "lb-cgg-framework-from-https" {
  cidr_blocks = [
    "0.0.0.0/0",
  ]
  from_port         = 443
  prefix_list_ids   = []
  protocol          = "tcp"
  security_group_id = aws_security_group.cgg-framework-lb.id
  to_port           = 443
  type              = "ingress"
}

resource "aws_security_group_rule" "lb-cgg-framework-to-out" {
  cidr_blocks = [
    "0.0.0.0/0",
  ]
  from_port         = 0
  prefix_list_ids   = []
  protocol          = "-1"
  security_group_id = aws_security_group.cgg-framework-lb.id
  to_port           = 0
  type              = "egress"
}
