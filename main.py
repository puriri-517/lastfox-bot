import discord
from discord.ext import commands
from discord import app_commands
import os

# .env の読み込み（ローカル実行にも対応）
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

# インテント設定（!コマンドに必要）
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

# Bot初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# Botが起動したときの処理（スラッシュコマンド同期もここで）
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

# Cogの読み込み（Bot起動時に自動）
@bot.event
async def setup_hook():
    print("🔄 setup_hook が呼び出されました")
    try:
        await bot.load_extension("cogs.clear")
        print("✅ cogs.clear を読み込みました")
    except Exception as e:
        print(f"❌ cogs.clear 読み込み失敗: {e}")

    # 他に読み込むCogがあればここに追加
    # await bot.load_extension("cogs.setup_notice")

# Bot起動
print("🚀 Bot を起動します")
bot.run(TOKEN)

