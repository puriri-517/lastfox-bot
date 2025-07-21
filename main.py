import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # .envファイルからDISCORD_TOKENを読み込み

intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容の取得を許可

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"ログインしました: {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"スラッシュコマンドを {len(synced)} 件同期しました。")
    except Exception as e:
        print(f"スラッシュコマンドの同期に失敗しました: {e}")

@bot.event
async def setup_hook():
    await bot.load_extension("cogs.clear")

bot.run(os.getenv("DISCORD_TOKEN"))
