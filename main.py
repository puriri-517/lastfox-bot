import discord
from discord.ext import commands
from discord import app_commands
import os

# .env から読み込む（Renderなどでエラー回避）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("dotenvモジュールは読み込まれませんでした")

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  # スラッシュコマンドの同期
    print(f"{bot.user} としてログインしました")

# Cogを読み込む
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.clear")

bot.run(TOKEN)
