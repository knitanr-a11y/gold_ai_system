@echo off
REM ================================================
REM gold_ai_system をコマンドプロンプトから起動するテンプレート
REM 1. このファイルをコピーして "run_gold_ai.bat" などの名前を付ける
REM 2. YOUR_DISCORD_WEBHOOK_URL を実際の URL に置き換える
REM 3. ダブルクリックまたはコマンドラインから実行
REM ================================================

set DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/YOUR_DISCORD_WEBHOOK_URL
set STAGE1_MODEL=lightgbm
set STAGE2_MODEL=lstm

python -m gold_ai_system.cli --show-config
pause