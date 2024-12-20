# ベースイメージ
FROM node:18-alpine

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要な依存ライブラリをインストール
COPY package.json package-lock.json ./
RUN npm install

# ソースコードをコピー
COPY . .

# ポートの公開（React開発サーバー）
EXPOSE 3000

# 開発サーバーを起動
CMD ["npm", "run", "dev"]