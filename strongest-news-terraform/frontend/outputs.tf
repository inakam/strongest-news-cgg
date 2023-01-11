output "aws_alb_alb_name" {
  value = aws_alb.alb.name
}

output "aws_alb_alb_dns_name" {
  value = aws_alb.alb.dns_name
}

output "ecr_repository_url" {
  value = aws_ecr_repository.cgg-framework-react.repository_url
}
