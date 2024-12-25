# ベースイメージ
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要な依存ライブラリをインストール
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install autopep8
#キャッシュを残さない場合、以下でdockerイメージのサイズを小さくできる
#RUN pip install --no-cache-dir -r requirements.txt


#依存関係の処理結果を先に実行し、コードファイルの実行をdockerfileの後方に置くことで、キャッシュの効率を最大化する
COPY . .

# コンテナ内で使用するポートを指定（明示的なドキュメント目的）
EXPOSE 8000

# FastAPIサーバーを起動
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]