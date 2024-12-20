# ベースイメージとしてNode.js 18を使用
FROM node:18-alpine

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
RUN npm create vite@latest . -- --template react

# 依存関係をインストール
RUN npm install

# ソースコードをコピー
COPY . .

# 作業ディレクトリを変更
WORKDIR /workspace/my-app

# ポートの公開
EXPOSE 3000

# 開発サーバーを起動
CMD ["npm", "run", "dev", "--", "--host"]