# CatsAndChocolateServer

## 開発環境構築

1. docker をインストール
2. VSCode に devContainer をインストールする
3. プロジェクトルートに.env ファイルを作成、 OpenAI の APIKey を書く

```env
OPENAI_API_KEY=<API Key>
```

4. VSCode でプロジェクトを開き、devContainer が構築されるまで待つ
5. [実行とデバッグ]ビューから[Python Django]を選択、実行することで http://localhost:8000 でサーバが起動する
