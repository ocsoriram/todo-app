# ベースイメージとしてPython 3.11を使用
FROM python:3.11-slim

# Node.jsをインストールするために必要なツールを準備
RUN apt-get update && apt-get install -y curl gnupg

# Node.jsの公式リポジトリを登録し、Node.jsをインストール
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

# 作業ディレクトリを作成
WORKDIR /workspace

# requirements.txt をコンテナにコピーし、Pythonの依存関係をインストール
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ポートの公開
EXPOSE 8000
EXPOSE 3000