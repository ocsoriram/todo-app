# ベースイメージとしてNode.js 18を使用
FROM node:18-alpine

# 作業ディレクトリを設定
WORKDIR /workspace

# 必要な依存関係をインストール
RUN npm install -g create-react-app

# Reactプロジェクトを作成
RUN npx create-react-app my-app

# 作業ディレクトリを変更
WORKDIR /workspace/my-app

# ポートの公開
EXPOSE 3000

# 開発サーバーを起動
CMD ["npm", "start"]