resource "aws_ecr_repository" "cgg-framework-react" {
  image_tag_mutability = "MUTABLE"
  name                 = "ecr-${var.name}-react"
}
