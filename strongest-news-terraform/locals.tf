locals {
  name           = "cgg-${local.sci_number}"
  artifacts_name = "codepipeline-cgg-${local.sci_number}"
  environment    = local.name
}
