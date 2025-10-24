# セットアップ手順（日本語）

このドキュメントでは、Discord の Webhook URL を安全に設定しながら `gold_ai_system` を実行するための方法を説明します。

## 1. `.env` ファイルを使う方法

1. テンプレートをコピーします。コピー先のファイル名は **`.env`（拡張子なし）** とし、リポジトリのルートに配置してください。
   ```bash
   cp .env.example .env
   ```
2. コピーした `.env` をテキストエディタで開き、`DISCORD_WEBHOOK_URL` の行を実際の Webhook URL に書き換えます。
3. 必要に応じて `STAGE1_MODEL`（`lightgbm` または `catboost`）と `STAGE2_MODEL`（`lstm`）を設定します。
4. ファイルを保存します。

`.env` は `.gitignore` に含まれているため、GitHub へはコミットされません。安全に秘密情報を管理できます。`Files/` など別ディレクトリに置くとアプリから読み込まれないので、必ずルート直下に置いてください。

## 2. コマンドプロンプトから毎回設定する方法（Windows）

1. コマンドプロンプトを開きます。
2. 以下のコマンドを入力して Webhook URL などを設定します（URL 部分を実際の値に置き換えてください）。
   ```cmd
   set DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxx/yyy
   set STAGE1_MODEL=lightgbm
   set STAGE2_MODEL=lstm
   python -m gold_ai_system.cli --show-config
   ```
3. コマンドプロンプトを閉じると変数は消えるので、毎回再設定が必要です。

## 3. PowerShell から設定する方法（Windows）

1. PowerShell を開きます。
2. 以下のコマンドを入力します。
   ```powershell
   $env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/xxx/yyy"
   $env:STAGE1_MODEL = "catboost"
   $env:STAGE2_MODEL = "lstm"
   python -m gold_ai_system.cli --show-config
   ```
3. セッションを閉じると変数が消える点はコマンドプロンプトと同じです。

## 4. シェルから設定する方法（macOS / Linux）

1. ターミナルを開きます。
2. 以下のコマンドを入力します。
   ```bash
   export DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/xxx/yyy
   export STAGE1_MODEL=lightgbm
   export STAGE2_MODEL=lstm
   python -m gold_ai_system.cli --show-config
   ```
3. シェルを閉じると変数は消えます。毎回設定するか、`.bashrc` などに追記してください。

## 5. テンプレートスクリプトを利用する

`scripts/` ディレクトリにあるテンプレートを自分用にコピーし、Webhook URL を書き換えてから実行することもできます。

- コマンドプロンプト用テンプレート：`scripts/run_cli_cmd_template.bat`
  - 例：`copy scripts\run_cli_cmd_template.bat scripts\run_cli_cmd.bat`
- PowerShell 用テンプレート：`scripts/run_cli_powershell_template.ps1`
  - 例：`copy scripts\run_cli_powershell_template.ps1 scripts\run_cli_powershell.ps1`
- macOS / Linux 用テンプレート：`scripts/run_cli_unix_template.sh`
  - 例：`cp scripts/run_cli_unix_template.sh scripts/run_cli_unix.sh`

コピー後のファイルに記載された `YOUR_DISCORD_WEBHOOK_URL` を実際の URL に置き換えて保存してください。コピーして作成した実行用スクリプト（例：`run_cli_cmd.bat`）は `.gitignore` に含まれているため、GitHub へコミットされません。`Files/` ディレクトリもデータ専用として `.gitignore` 済みなので、ここに置いた個人用ファイルはリポジトリへ上がりません。

## 6. GitHub へコミットするファイルの目安

- コミットする：`.env.example`、`README.md`、`docs/`、`src/`、`scripts/` のテンプレートなどソースやドキュメント類。
- コミットしない：`.env` や個人用スクリプト（`run_cli_cmd.bat` など）、`Files/` に配置したロウデータや秘密情報。
- 迷った場合は `git status` の結果を確認し、秘密情報を含まないことを確かめてからコミットしてください。

## 7. GitHub Desktop でコミット／プッシュする場合

GitHub Desktop を使う場合は以下の手順でコミットとプッシュを行います。Push ボタンがグレーアウトしている、反映されないといった
ときはトラブルシューティングも併せて確認してください。

1. GitHub Desktop の左上で「Current Repository」が `gold_ai_system` になっていることを確認します。
2. 画面左の変更一覧にコミットしたいファイルが表示されているか確認し、不要なファイルはチェックを外します。
3. 左下の `Summary` と `Description` にメッセージを入力し、`Commit to <ブランチ名>` をクリックします。
4. コミット後に右上の `Push origin`（または `Publish branch`）ボタンをクリックして GitHub へ送信します。

Push が実行できない場合は次の項目を確認してください。

- **GitHub へログインしているか**：右上のプロフィールアイコンからログイン状態を確認します。
- **ブランチが GitHub 上に存在するか**：初回は `Publish branch` と表示されます。これを押さないと GitHub にブランチが作成されません。
- **リモート URL が正しいか**：メニューの `Repository > Repository Settings...` を開き、`Remote` に正しい GitHub リポジトリ URL が設定されているかを確認します。
- **コミットしていないファイルしかない**：コミットを作成していないと Push は何も送るものがありません。`Changes` タブにファイルが表示されているか確認し、まずコミットを作成してください。
- **ネットワークの問題**：インターネット接続やプロキシ設定に問題がないか確認します。エラーが表示された場合は内容をメモして解決します。

上記を確認しても改善しない場合は、GitHub Desktop の `View > Toggle Developer Tools` でコンソールログを開き、エラーメッセージを元に原因
を探ると解決のヒントになります。

## 8. 設定を確認する

環境変数を設定した状態で以下を実行すると、現在読み込まれている設定値を確認できます。

```bash
python -m gold_ai_system.cli --show-config
```

Discord Webhook URL はログ上で `********` にマスクされて表示されます。

---

何か問題があれば `README.md` や `docs/system_structure_ja.md` もあわせて参照してください。
