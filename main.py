import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み（ローカル実行にも対応）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv モジュールは読み込まれませんでした")

TOKEN = os.getenv("DISCORD_TOKEN")

# インテント設定（!コマンドに必要）
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Bot初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# Botが起動したときの処理（スラッシュコマンド同期もここで）
@bot.event
async def on_ready():
    print(f"{bot.user} としてログインしました！")
    try:
        synced = await bot.tree.sync()
        print(f"✅ スラッシュコマンド {len(synced)} 件を同期しました。")
    except Exception as e:
        print(f"❌ スラッシュコマンド同期失敗: {e}")

# Cogの読み込み（Bot起動時に自動）
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.clear")
    
    # 他に読み込むCogがあればここに追加
    # await bot.load_extension("cogs.setup_notice")
    # await bot.load_extension("cogs.translation") など

# Bot起動
bot.run(TOKEN)
