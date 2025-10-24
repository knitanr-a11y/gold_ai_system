# システム構成とファイル計画（日本語）

以下は `gold_ai_system` で今後作成予定の主なモジュールとファイル名です。実装段階で必要に応じて細分化していきます。

## 1. コアディレクトリ構成（予定）

```
.env.example               # 環境変数テンプレート（ルート直下）
.env                       # 実際に使用する設定ファイル（Git には含めない／ルート直下に配置）
src/gold_ai_system/
├── __init__.py
├── cli.py                  # エントリーポイント（既存）
├── config.py               # 設定ロード（既存）
├── scheduler/              # 定期実行関連
│   ├── __init__.py
│   ├── jobs.py             # 5分ごとのポーリング、日次集計、週次再学習などのタスク定義
│   └── runner.py           # APScheduler 等を使った実行管理
├── data/                   # データ取得・検証・前処理
│   ├── __init__.py
│   ├── loaders.py          # M5/H1 CSV の読み込み、欠損チェック
│   ├── validators.py       # 足の連続性チェック、補完ロジック
│   └── features.py         # テクニカル指標や波形特徴量の生成
├── models/                 # 学習・推論処理
│   ├── __init__.py
│   ├── stage1.py           # LightGBM / CatBoost による粗い判定
│   ├── stage2.py           # PyTorch LSTM による期待値推定
│   ├── training.py         # 学習パイプライン（週次再学習）
│   └── calibration.py      # バックテストに基づく期待値補正
├── signals/                # シリーズ管理と通知判定
│   ├── __init__.py
│   ├── expectation.py      # 期待値計算、損切り 5 ドル時の減点ロジック
│   ├── series.py           # シリーズ状態管理（開始・更新・終了）
│   ├── notifier.py         # Discord Webhook への通知
│   └── history.py          # トレード履歴の保存と集計
└── backtest/
    ├── __init__.py
    └── runner.py           # 過去データでの検証ツール
```

## 2. データ保存先（予定）

- `data/storage/`
  - `models/` : 学習済みモデルファイル（Stage1/Stage2 別、日付別に保存）
  - `calibration/` : 期待値補正テーブル
  - `trades/` : 実トレード履歴 CSV
  - `reports/` : 日次・月次集計結果
  - （参考）リポジトリ外の `Files/` ディレクトリはローカルのローソク足 CSV 置き場として利用し、Git には含めない運用とします。

必要になったタイミングで `data/storage` 以下のサブディレクトリを作成していきます。

## 3. スクリプト

- `scripts/run_cli_cmd_template.bat` : コマンドプロンプト用起動テンプレート
- `scripts/run_cli_powershell_template.ps1` : PowerShell 用起動テンプレート
- `scripts/run_cli_unix_template.sh` : macOS / Linux 用起動テンプレート
- （今後）`scripts/retrain_models.py` や `scripts/backtest.py` などの CLI を追加予定

## 4. ドキュメント

- `docs/setup_ja.md` : 環境変数の設定方法
- `docs/system_structure_ja.md` : 本ドキュメント（ファイル構成計画）
- 今後、仕様や API をまとめた `docs/spec_ja.md` などを追加予定

## 5. 命名ルールメモ

- Python ファイル：スネークケース (`series_manager.py` など)
- クラス名：パスカルケース (`SeriesManager`)
- 関数名／変数名：スネークケース (`load_candles`, `calc_expectation`)

---

上記の構成は初期案です。開発の進捗に合わせて柔軟に調整していきましょう。
