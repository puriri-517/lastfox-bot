# ✅ 完全版 main.py
import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み
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
intents.members = True

# Bot 初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# 起動時イベント
@bot.event
async def on_ready():
    print("🟢 on_ready が呼ばれました")
    print(f"✅ Botログイン完了：{bot.user}")
    try:
        # サーバーIDを指定してそのサーバーのみにコマンドを同期
        guild = discord.Object(id=1388577649328390196)  # ←ここに対象のサーバーIDを指定
        synced = await bot.tree.sync(guild=guild)
        print(f"✅ スラッシュコマンド（ギルド限定）同期完了：{len(synced)} 件")
        for cmd in synced:
            print(f"🔧 /{cmd.name}（{cmd.description}）")
    except Exception as e:
        print(f"❌ スラッシュコマンド同期失敗: {e}")

# Cog 読み込み
@bot.event
async def setup_hook():
    print("🔄 setup_hook が呼び出されました")

    for cog_path in [
        "cogs.clear",
        "cogs.setup_invite",
        "cogs.setup_guild",
    ]:
        try:
            await bot.load_extension(cog_path)
            print(f"✅ {cog_path} を読み込みました")
        except Exception as e:
            print(f"❌ {cog_path} 読み込み失敗: {e}")

# Bot 起動
print("🚀 Bot を起動します")
bot.run(TOKEN)
