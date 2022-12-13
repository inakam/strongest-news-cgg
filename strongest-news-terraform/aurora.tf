####################################################
# RDS SG
####################################################

resource "aws_security_group" "database_sg" {
  name        = "${local.name}-database-sg"
  description = "${local.name}-database"
  vpc_id      = local.vpc_id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 3306
    to_port     = 3306
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${local.name}-database-sg"
  }
}

resource "aws_db_subnet_group" "database_sg_group" {
  name        = "${local.name}-database-subnet-group"
  description = "${local.name}-database-subnet-group"
  subnet_ids = [
    # 本来的にはprivateに置くべき
    local.public_subnet_1a,
    local.public_subnet_1c
  ]
}

####################################################
# RDS Cluster
####################################################

resource "aws_rds_cluster" "mysql" {
  cluster_identifier = "${local.name}-database-cluster"

  db_subnet_group_name   = aws_db_subnet_group.database_sg_group.name
  vpc_security_group_ids = [aws_security_group.database_sg.id]

  engine         = "aurora-mysql"
  engine_mode    = "provisioned"
  engine_version = "8.0.mysql_aurora.3.02.0"
  port           = "3306"

  serverlessv2_scaling_configuration {
    min_capacity = 0.5
    max_capacity = 2.0
  }

  database_name   = "article_database"
  master_username = "user"
  master_password = "password"

  skip_final_snapshot = true

  db_cluster_parameter_group_name = aws_rds_cluster_parameter_group.aurora_mysql.name
}

####################################################
# RDS Cluster Instance
####################################################

resource "aws_rds_cluster_instance" "cluster" {
  identifier         = "${local.name}-database-cluster-instance"
  cluster_identifier = aws_rds_cluster.mysql.id

  engine         = aws_rds_cluster.mysql.engine
  engine_version = aws_rds_cluster.mysql.engine_version

  instance_class       = "db.serverless"
  publicly_accessible  = true # 実際の開発ではtrueにするべきではない
  db_subnet_group_name = aws_rds_cluster.mysql.db_subnet_group_name
}

####################################################
# RDS cluster config
####################################################

resource "aws_rds_cluster_parameter_group" "aurora_mysql" {
  name   = "${local.name}-database-cluster-parameter-group"
  family = "aurora-mysql8.0"

  parameter {
    name  = "time_zone"
    value = "Asia/Tokyo"
  }
}

#####################################################
# RDSの初期データ投入
#####################################################

resource "local_file" "mysql_config_file" {
  filename = "./.my.cnf"
  content  = <<-EOT
[client]
user = ${aws_rds_cluster.mysql.master_username}
password = ${aws_rds_cluster.mysql.master_password}
host = ${aws_rds_cluster.mysql.endpoint}
port = ${aws_rds_cluster.mysql.port}
  EOT
}

resource "null_resource" "db_setup" {
  depends_on = [
    aws_rds_cluster.mysql,
    aws_rds_cluster_instance.cluster,
  ]

  provisioner "local-exec" {
    command = <<-EOT
      mysql --defaults-extra-file=./.my.cnf ${aws_rds_cluster.mysql.database_name} < ../database/1_initial.sql
      mysql --defaults-extra-file=./.my.cnf ${aws_rds_cluster.mysql.database_name} < ../database/2_users.sql
      mysql --defaults-extra-file=./.my.cnf ${aws_rds_cluster.mysql.database_name} < ../database/3_articles.sql
      mysql --defaults-extra-file=./.my.cnf ${aws_rds_cluster.mysql.database_name} < ../database/4_comments.sql
    EOT
  }
}
