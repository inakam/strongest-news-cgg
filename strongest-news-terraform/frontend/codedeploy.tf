resource "aws_codedeploy_app" "cgg-framework" {
  compute_platform = "ECS"
  name             = "codedeploy-${var.name}-app"
}

resource "aws_iam_role" "cgg-framework-pipeline" {
  name = "${var.name}-pipeline-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": ["codedeploy.amazonaws.com","ecs.amazonaws.com","ecs-tasks.amazonaws.com","s3.amazonaws.com","ec2.amazonaws.com"]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "AWSCodeDeployRole" {
  policy_arn = "arn:aws:iam::aws:policy/AWSCodeDeployFullAccess"
  role       = aws_iam_role.cgg-framework-pipeline.name
}

resource "aws_iam_role_policy_attachment" "AWSECSRole" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonECS_FullAccess"
  role       = aws_iam_role.cgg-framework-pipeline.name
}

resource "aws_iam_role_policy_attachment" "AWSS3Role" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
  role       = aws_iam_role.cgg-framework-pipeline.name
}

resource "aws_iam_role_policy_attachment" "AWSCodeDeployForECSRole" {
  policy_arn = "arn:aws:iam::aws:policy/AWSCodeDeployRoleForECS"
  role       = aws_iam_role.cgg-framework-pipeline.name
}

resource "aws_iam_instance_profile" "cgg-framework-pipeline" {
  name = "${var.name}-pipeline-role"
  role = aws_iam_role.cgg-framework-pipeline.name
}

resource "aws_codedeploy_deployment_group" "cgg-framework" {
  app_name               = aws_codedeploy_app.cgg-framework.name
  autoscaling_groups     = []
  deployment_config_name = "CodeDeployDefault.ECSAllAtOnce"
  deployment_group_name  = "codedeploy-deployment-group-${var.name}"
  service_role_arn       = aws_iam_role.cgg-framework-pipeline.arn

  auto_rollback_configuration {
    enabled = true
    events = [
      "DEPLOYMENT_FAILURE",
    ]
  }

  blue_green_deployment_config {
    deployment_ready_option {
      action_on_timeout    = "CONTINUE_DEPLOYMENT"
      wait_time_in_minutes = 0
    }

    terminate_blue_instances_on_deployment_success {
      action                           = "TERMINATE"
      termination_wait_time_in_minutes = 0
    }
  }

  deployment_style {
    deployment_option = "WITH_TRAFFIC_CONTROL"
    deployment_type   = "BLUE_GREEN"
  }

  ecs_service {
    cluster_name = aws_ecs_cluster.cgg-framework-cluster.name
    service_name = aws_ecs_service.cgg-framework-service.name
  }

  load_balancer_info {
    target_group_pair_info {
      prod_traffic_route {
        listener_arns = [
          aws_alb_listener.alb.arn
        ]
      }

      target_group {
        name = aws_alb_target_group.blue.name
      }
      target_group {
        name = aws_alb_target_group.green.name
      }
    }
  }

  depends_on = [
    aws_alb.alb
  ]
}
