module "frontend" {
  source = "./frontend"

  name             = "${local.name}-frontend"
  vpc_id           = local.vpc_id
  public_subnet_1a = local.public_subnet_1a
  public_subnet_1c = local.public_subnet_1c

  artifacts_name                          = "${local.artifacts_name}-frontend"
  aws_codecommit_repository_cgg_framework = aws_codecommit_repository.cgg_framework
  api_endpoint                            = module.backend.aws_alb_alb_dns_name
}

module "backend" {
  source = "./backend"

  name             = "${local.name}-backend"
  vpc_id           = local.vpc_id
  public_subnet_1a = local.public_subnet_1a
  public_subnet_1c = local.public_subnet_1c

  artifacts_name                          = "${local.artifacts_name}-backend"
  aws_rds_cluster_mysql                   = aws_rds_cluster.mysql
  aws_codecommit_repository_cgg_framework = aws_codecommit_repository.cgg_framework
}

// App Runnerのために以下のコメントアウトを外す
/*
module "frontend_apprunner" {
  source = "./frontend_apprunner"

  name               = "${local.name}-frontend-apprunner"
  ecr_repository_url = module.frontend.ecr_repository_url
}
*/
