FROM python:3.9

# 依存Pythonライブラリ一覧コピー
COPY requirements.txt ./
# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt
# 80番ポートを開く
EXPOSE 80
# FastAPIを実行（ホットリロードモードで起動する）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]