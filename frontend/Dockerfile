# ベースイメージとしてNode.js 18を使用
FROM node:18-alpine

# 必要な依存パッケージをインストール（Gitを含む）
RUN apk update && apk add --no-cache git

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要な依存関係をインストール
# RUN npm install -g npm@latest

# # package.json が存在する場合の処理
# # ホスト側のファイルをコピーして依存関係をインストール
# COPY package.json package-lock.json ./
# RUN npm install || true

# # Reactプロジェクトを作成
# RUN npx create-react-app my-app

# Viteプロジェクトを作成 npm initが含まれている(package.jsonが作成される)
#RUN npm create vite@latest my-app -- --template react --force

COPY my-app/package*.json ./

WORKDIR /workspace/my-app

# 依存関係をインストール
RUN npm install

# ソースコードをコピー
COPY my-app/ .

# ポートの公開
EXPOSE 3000

# 開発サーバーを起動
CMD ["npm", "run", "dev", "--", "--host"]