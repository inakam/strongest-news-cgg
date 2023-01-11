resource "aws_apprunner_service" "apprunner" {
  service_name = var.name

  source_configuration {
    # 作成したIAMロールを指定
    authentication_configuration {
      access_role_arn = aws_iam_role.role.arn
    }
    # 事前に作成・pushしておいたECRリポジトリを指定
    image_repository {
      image_configuration {
        port = "80"
      }
      image_identifier      = "${var.ecr_repository_url}:latest"
      image_repository_type = "ECR"
    }
  }

  tags = {
    Name = "${var.name}-apprunner-service"
  }
}
