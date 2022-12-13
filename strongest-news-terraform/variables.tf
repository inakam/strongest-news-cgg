provider "aws" {
  region                   = "ap-northeast-1" # 使用するリージョンが違う場合変更する
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "cgg"
}

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.12.0"
    }
  }
  backend "s3" {
    encrypt                 = true
    bucket                  = "cgg-framework-sci0xxxx.cgg.com" # 自分のSCI番号に書き換える
    region                  = "ap-northeast-1"                 # 使用するリージョンが違う場合変更する
    key                     = "terraform.tfstate"
    shared_credentials_file = "~/.aws/credentials"
    profile                 = "cgg"
  }
}

locals {
  sci_number = "sci0xxxx" # 自分のSCI番号に書き換える

  # 環境ごとの設定に変更する
  vpc_id           = "vpc-0862916a8bafd7zzz"
  public_subnet_1a = "subnet-06f8ec3f98b5f1zzz"
  public_subnet_1c = "subnet-067a18dfbc09d0zzz"
}
