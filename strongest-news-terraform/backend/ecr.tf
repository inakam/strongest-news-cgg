resource "aws_ecr_repository" "cgg-framework-fastapi" {
  image_tag_mutability = "MUTABLE"
  name                 = "ecr-${var.name}-fastapi"
}
