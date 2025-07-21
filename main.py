import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み（Renderやローカル実行対応）
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ .env を読み込みました")
except ImportError:
    print("⚠️ dotenv モジュールは読み込まれませんでした")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("❌ DISCORD_TOKEN が設定されていません。")
    exit(1)

# インテント設定
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True  # 管理者DM送信やロール処理に必要

# Bot 初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# 起動時イベント
@bot.event
async def on_ready():
    print("🟢 on_ready が呼ばれました")
    print(f"✅ Botログイン完了：{bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ スラッシュコマンド同期完了：{len(synced)} 件")
        for cmd in synced:
            print(f"🔧 /{cmd.name}（{cmd.description}）")
    except Exception as e:
        print(f"❌ スラッシュコマンド同期失敗: {e}")

# Cog 読み込み
@bot.event
async def setup_hook():
    print("🔄 setup_hook が呼び出されました")
    
    try:
        await bot.load_extension("cogs.clear")
        print("✅ cogs.clear を読み込みました")
    except Exception as e:
        print(f"❌ cogs.clear 読み込み失敗: {e}")
    
    try:
        await bot.load_extension("cogs.setup_invite")  # サーバー参加時のDM案内
        print("✅ cogs.setup_invite を読み込みました")
    except Exception as e:
        print(f"❌ cogs.setup_invite 読み込み失敗: {e}")
    
    try:
        await bot.load_extension("cogs.setup_guild")   # /setup コマンドで部屋とロール作成
        print("✅ cogs.setup_guild を読み込みました")
    except Exception as e:
        print(f"❌ cogs.setup_guild 読み込み失敗: {e}")

# Bot 起動
print("🚀 Bot を起動します")
bot.run(TOKEN)
