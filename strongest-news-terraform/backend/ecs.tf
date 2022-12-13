resource "aws_ecs_cluster" "cgg-framework-cluster" {
  name = "${var.name}-cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_iam_role" "ecs_execution_role" {
  name               = "ecs-tasks-execution-role-${var.name}"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "ecs_execution_role_attach" {
  role       = aws_iam_role.ecs_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_ecs_service" "cgg-framework-service" {
  cluster                            = aws_ecs_cluster.cgg-framework-cluster.arn
  deployment_maximum_percent         = 200
  deployment_minimum_healthy_percent = 100
  desired_count                      = 1
  enable_ecs_managed_tags            = false
  health_check_grace_period_seconds  = 0
  launch_type                        = "FARGATE"
  name                               = "${var.name}-service"
  scheduling_strategy                = "REPLICA"
  task_definition                    = aws_ecs_task_definition.cgg-framework.arn
  deployment_controller {
    type = "CODE_DEPLOY"
  }

  network_configuration {
    subnets          = [var.public_subnet_1a, var.public_subnet_1c]
    security_groups  = [aws_security_group.cgg-framework.id]
    assign_public_ip = true
  }

  load_balancer {
    container_name   = "fast-api"
    container_port   = 80
    target_group_arn = aws_alb_target_group.blue.arn
  }

  depends_on = [
    aws_alb.alb
  ]

  lifecycle {
    ignore_changes = [load_balancer, task_definition]
  }
}

resource "aws_ecs_task_definition" "cgg-framework" {
  family                   = var.name
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 512
  memory                   = 1024
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn
  container_definitions = templatefile("${path.module}/task-definitions/taskdef.json", {
    ecr_name_fastapi  = aws_ecr_repository.cgg-framework-fastapi.name
    name              = var.name
    region            = data.aws_region.current.name
    aws_account_id    = data.aws_caller_identity.current.account_id
    database_user     = var.aws_rds_cluster_mysql.master_username
    database_password = var.aws_rds_cluster_mysql.master_password
    database_db_name  = var.aws_rds_cluster_mysql.database_name
    database_host     = "${var.aws_rds_cluster_mysql.endpoint}:${var.aws_rds_cluster_mysql.port}"
  })
}

resource "aws_cloudwatch_log_group" "ecs-fastapi" {
  name = "ecs-fastapi-${var.name}"
  tags = {
    Application = "fastapi"
  }
}

# Application Auto Scaling
resource "aws_appautoscaling_target" "appautoscaling_target" {
  service_namespace  = "ecs"
  resource_id        = "service/${aws_ecs_cluster.cgg-framework-cluster.name}/${aws_ecs_service.cgg-framework-service.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  min_capacity       = 1
  max_capacity       = 4
}

resource "aws_appautoscaling_policy" "appautoscaling_policy" {
  name               = aws_ecs_service.cgg-framework-service.name
  service_namespace  = "ecs"
  resource_id        = "service/${aws_ecs_cluster.cgg-framework-cluster.name}/${aws_ecs_service.cgg-framework-service.name}"
  scalable_dimension = "ecs:service:DesiredCount"
  policy_type        = "TargetTrackingScaling"

  target_tracking_scaling_policy_configuration {
    predefined_metric_specification {
      predefined_metric_type = "ECSServiceAverageCPUUtilization"
    }

    target_value       = 50
    scale_out_cooldown = 100
    scale_in_cooldown  = 300
  }

  depends_on = [aws_appautoscaling_target.appautoscaling_target]
}
