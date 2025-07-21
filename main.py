import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み（Render／ローカル両対応）
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️ dotenv モジュールは読み込まれませんでした")

TOKEN = os.getenv("DISCORD_TOKEN")

# インテント設定
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Bot初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# ✅ Botログイン完了時
@bot.event
async def on_ready():
    print(f"✅ Botログイン完了：{bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ スラッシュコマンド同期完了：{len(synced)} 件")
        for cmd in synced:
            print(f"🔧 /{cmd.name}（{cmd.description}）")
    except Exception as e:
        print(f"❌ スラッシュコマンド同期失敗: {e}")

# ✅ Cogの読み込み処理
@bot.event
async def setup_hook():
    try:
        await bot.load_extension("cogs.clear")
        print("✅ cogs.clear を読み込みました。")
    except Exception as e:
        print(f"❌ cogs.clear 読み込み失敗: {e}")

    # 追加予定のCogがあればここに書いてOK
    # await bot.load_extension("cogs.setup_notice")

# ✅ Bot起動
bot.run(TOKEN)
