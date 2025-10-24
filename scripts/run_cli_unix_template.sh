#!/usr/bin/env bash
# ================================================
# gold_ai_system を macOS / Linux から起動するテンプレート
# 1. このファイルをコピーして "run_gold_ai.sh" などの名前を付ける
# 2. YOUR_DISCORD_WEBHOOK_URL を実際の URL に置き換える
# 3. `chmod +x run_gold_ai.sh` で実行権限を付与し、`./run_gold_ai.sh` で実行
# ================================================

export DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL
export STAGE1_MODEL=lightgbm
export STAGE2_MODEL=lstm

python -m gold_ai_system.cli --show-config
read -rp "Enter キーを押すと終了します" _