resource "aws_codecommit_repository" "cgg_framework" {
  repository_name = local.name
  description     = "CGG2022 開発演習用リポジトリ"
}
