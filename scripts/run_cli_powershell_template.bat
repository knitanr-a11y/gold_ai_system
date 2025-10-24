# ================================================
# gold_ai_system を PowerShell から起動するテンプレート
# 1. このファイルをコピーして "run_gold_ai.ps1" などの名前を付ける
# 2. YOUR_DISCORD_WEBHOOK_URL を実際の URL に置き換える
# 3. PowerShell で実行（実行ポリシーに注意）
# ================================================

$env:DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL"
$env:STAGE1_MODEL = "catboost"
$env:STAGE2_MODEL = "lstm"

python -m gold_ai_system.cli --show-config
Read-Host "Enter キーを押すと終了します"