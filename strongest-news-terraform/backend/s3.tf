data "aws_elb_service_account" "alb_log" {}

data "aws_iam_policy_document" "alb_log" {
  statement {
    actions = [
      "s3:PutObject",
    ]

    resources = [
      "arn:aws:s3:::${var.name}-alb-log/*",
    ]

    principals {
      type = "AWS"

      identifiers = [
        "arn:aws:iam::${data.aws_elb_service_account.alb_log.id}:root",
      ]
    }
  }
}

resource "aws_s3_bucket" "alb_log" {
  bucket        = "${var.name}-alb-log"
  force_destroy = true
  acl           = "private"
}

resource "aws_s3_bucket" "codebuild-artifacts" {
  bucket        = "cgg-framework-pipeline-pkg-${var.name}"
  force_destroy = true
  acl           = "private"
}

resource "aws_s3_bucket_policy" "alb_policy" {
  bucket = aws_s3_bucket.alb_log.id
  policy = data.aws_iam_policy_document.alb_log.json
}
