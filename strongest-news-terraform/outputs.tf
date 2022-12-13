output "aws_alb_frontend_url" {
  value = module.frontend.aws_alb_alb_dns_name
}

output "aws_alb_backend_url" {
  value = module.backend.aws_alb_alb_dns_name
}

data "aws_region" "current" {}
output "codecommit_address" {
  value = "codecommit::${data.aws_region.current.name}://cgg@${aws_codecommit_repository.cgg_framework.repository_name}"
}
