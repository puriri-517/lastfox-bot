import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み（Render用）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenv モジュールは読み込まれませんでした")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True  # 念のため明示

bot = commands.Bot(command_prefix="!", intents=intents)

# Bot起動完了時
@bot.event
async def on_ready():
    print(f"{bot.user} としてログインしました！")

# スラッシュコマンド登録とCog読み込み
@bot.event
async def setup_hook():
    # ✅ スラッシュコマンドの同期（推奨：setup_hook内）
    try:
        synced = await bot.tree.sync()
        print(f"✅ スラッシュコマンド {len(synced)} 件を同期しました。")
    except Exception as e:
        print(f"❌ スラッシュコマンド同期失敗: {e}")

    # ✅ Cogの読み込み
    await bot.load_extension("cogs.clear")

    # 👇 setup_notice.py が存在しない場合はコメントアウト
    # await bot.load_extension("cogs.setup_notice")

bot.run(TOKEN)

