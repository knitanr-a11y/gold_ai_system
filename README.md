# Gold AI System

このリポジトリは、ゴールドのFXトレードシグナルを自動で生成するシステムのソースコードです。現段階ではプロジェクトの土台と環境変数の設定方法を整備し、今後のファイル構成案をまとめています。

> **English summary**: The repository currently provides project scaffolding, environment
> configuration helpers, and documentation for Stage1 (LightGBM/CatBoost) and Stage2
> (PyTorch LSTM) model choices. Japanese setup instructions are included below.

## Project layout

```
.
├── .env.example            # Template for environment variables
├── pyproject.toml          # Python project metadata and dependencies
├── src/gold_ai_system/
│   ├── __init__.py
│   ├── cli.py              # Placeholder CLI for configuration validation
│   └── config.py           # Environment-driven settings loader
└── README.md
```

## セットアップ手順（日本語）

Webhook URL の設定方法や実行手順は `docs/setup_ja.md` に詳しく記載しています。以下は概要です。

1. `.env` を使う場合はリポジトリの **ルートディレクトリ** で `cp .env.example .env`（拡張子なし）とコピーし、`DISCORD_WEBHOOK_URL` を実際の URL に書き換えます。`Files/` ディレクトリなど別の場所に配置すると読み込まれないので注意してください。
2. `.env` を使わない場合は、コマンドプロンプトや PowerShell、ターミナルで環境変数を毎回設定します。
3. `scripts/` ディレクトリにはそれぞれの環境向けテンプレートスクリプトがあるので、コピーして URL を差し替えるだけで実行できます。
4. 設定後に `python -m gold_ai_system.cli --show-config` を実行すると、Discord Webhook URL（マスク表示）と Stage1/Stage2 のモデル指定が確認できます。

詳細は [`docs/setup_ja.md`](docs/setup_ja.md) を参照してください。

## Git へのコミットの目安

- `.env` は秘密情報を含むためコミットしません（`.gitignore` 済み）。`.env.example` はテンプレートなのでコミット対象です。
- `scripts/` 以下のテンプレートをコピーして作った自分専用スクリプト（例: `scripts/run_cli_cmd.bat`）は `.gitignore` 済みです。
- それ以外のソースコード、ドキュメント、設定ファイルは変更内容を確認したうえで通常どおりコミットしてください。
- GitHub Desktop でのコミット／プッシュ手順と Push できない場合の対処は [`docs/setup_ja.md`](docs/setup_ja.md) の「GitHub Desktop でコミット／プッシュする場合」を参照してください。

## Running the placeholder CLI

After configuring the environment variables, verify the configuration with:

```
python -m gold_ai_system.cli --show-config
```

The webhook URL is masked in the output so secrets are not exposed. The command will
be expanded later into the scheduler that polls 5-minute candles, executes inference,
and dispatches Discord notifications.

## 追加ドキュメント

- [`docs/setup_ja.md`](docs/setup_ja.md) : 環境変数の設定方法まとめ
- [`docs/system_structure_ja.md`](docs/system_structure_ja.md) : 今後作成するモジュール・ファイル構成案

## Next steps / 今後の開発項目

- Implement candle ingestion, validation, and scheduling utilities.
- Build Stage1 (LightGBM/CatBoost) classifiers for ±10/±5 USD movements using the latest 1–3 months of data plus long-term context.
- Develop Stage2 PyTorch LSTM models for refined expectation estimates with multi-scale (4h/8h/16–24h) wave features.
- Add backtesting, expectation calibration, and Discord notification workflows.