<h1 align='center'>クラウド・ゴールデン・ジム #4</h1>
<h2 align='center'>直希評判記 暴れん坊コンテナ</h2>

<p align="center">
  <img src="https://user-images.githubusercontent.com/23179726/206911937-9a561de8-4f79-4d24-848d-d63ed637f704.png" alt="暴れん坊コンテナ" width="600px">
</p>

```
出演：inakam、Penpen7
対象：Dockerによるコンテナ開発を検討している/行なっている方
技術：Docker/EC2/ECS/Fargate
番組詳細：
平社員から八代将軍となった直希は、入社の行列に命懸けで訴え出た少女の願いを聞き、
開発工数を吊り上げようと非効率な開発環境を構築した罪で捕われた中村屋の無実を晴らすべく立ち上がる。
若き直希が、理想の開発環境を実現すべく、単身身を投じてレガシーシステムを暴き断罪する
『暴れん坊コンテナ』始動編！
```

# 🎁 コンテナのビルドと起動

## コンテナのビルド

```bash
docker-compose build
```

## コンテナの起動

```bash
docker-compose up
```

以下を開くとそれぞれ表示されます。

- React(Frontend) : <a href="http://localhost" target="_blank">http://localhost</a>

- FastAPI(Backend) : <a href="http://localhost:5000" target="_blank">http://localhost:5000</a>

- SwaggerUI : <a href="http://localhost:5000/docs" target="_blank">http://localhost:5000/docs</a>

### DB 内部を直接見たい場合

- MySQL8.0 のクライアントをインストールした後で以下を実行
  ```bash
  mysql -h 127.0.0.1 -u user -p password
  ```

## FastAPI テスト実行

- 以下を実行するとテスト用のコンテナが立ち上がり、テストが実行されます
  ```bash
  docker-compose run test pytest app/tests
  ```

# 📝 ハイレベルアーキテクチャ

## 💻 ローカル環境

<p align="center">
  <img src="https://user-images.githubusercontent.com/23179726/206913294-e1b7e76c-305c-4558-a548-6f3d0544b9d9.png" alt="ローカル環境" width="800px">
</p>

## 🌩 AWS 環境

<p align="center">
  <img src="https://user-images.githubusercontent.com/23179726/206988069-e8a94ccf-ffec-47c6-91df-eea3687758f5.png" alt="AWS環境" width="800px">
</p>

# 🤗 AWS EC2 上に立ち上げる

1. AWS で EC2 のインスタンス（Amazon Linux 2）を立ち上げる
1. EC2 インスタンスへ ssh 接続でログインする（`ssh ec2-user@[ipアドレス]`）
1. `git clone [このリポジトリ]`
1. `sudo sh ./ec2_docker_install_script.sh`を実行し、docker をインストール
1. `exit`で一度 ssh 接続を解除し、もう一度 ssh 接続をする
1. リポジトリのディレクトリで`docker-compose up`を実行
1. インスタンスのグローバル IP へアクセスし、表示されたら成功

# 🚀 AWS 環境で CodePipeline による ECS デプロイ

1. `aws configure --profile cgg`を実行し、AWS の認証情報を登録
1. このリポジトリを`git clone`
1. strongest-news-terraform/variables.tf の内容を修正
   - `sci_number` や `vpc_id` などを書き換える
1. AWS のコンソールで Terraform の state 用のバケットを作成
   - `nifty-cgg-framework-sci0xxxx.nifty.com`のような名前にして S3 バケット作成
1. MySQL 8.0 のクライアントをインストール
   - Terraform 実行時に null_resource を使って初期データを Aurora に流し込むために使用します
   - Amazon Linux 2 の場合
     ```bash
     $ sudo yum localinstall -y http://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
     $ sudo yum install -y mysql-community-client
     ```
1. strongest-news-terraform フォルダの内容を実行
   1. `cd ./strongest-news-terraform`
   1. `terraform init` で初期化
   1. `terraform apply` で環境を構築
      - ここで出力された codecommit_address をメモ
1. 構築された AWSCodecommit にアプリケーションをデプロイ
   1. 必要であれば、`pip install git-remote-codecommit`を行い、git で codecommit を操作できるようにする
   1. `git remote codecommit [ここをcodecommit_addressにする]`を実行し、codecommit へプッシュできるようにする
   1. `git checkout main && git push codecommit HEAD`
1. CodePipeline のパイプラインを実行
