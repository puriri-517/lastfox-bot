import discord
from discord.ext import commands
import os
from views.reservation_view import ReservationView
from views.randompick_view import RandomPickView
from dotenv import load_dotenv

# .env ファイルからトークンを読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# インテント設定（必要なもののみON）
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.reactions = True
intents.members = True

# Botのインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot起動時の処理
@bot.event
async def on_ready():
    print(f"{bot.user} としてログインしました")
    bot.add_view(ReservationView(bot))  # 予約通知ボタン
    bot.add_view(RandomPickView(bot))   # ランダムピックボタン

# Cogの読み込み（必要なもののみ）
@bot.event
async def setup_hook():
    await bot.load_extension("cogs.clear")            # メッセージ削除
    # await bot.load_extension("cogs.translation")    # 翻訳（必要に応じて有効化）
    # await bot.load_extension("cogs.panda")          # パンダ応答機能（任意）
    # await bot.load_extension("cogs.everyone_call")  # @everyone呼び出し（任意）
    # await bot.load_extension("cogs.schedule")       # 通知予約（実装済みなら有効化）
    # await bot.load_extension("cogs.guild_list")     # サーバー一覧（開発者用）
    # await bot.load_extension("cogs.check_permission") # 権限確認（任意）
    # await bot.load_extension("cogs.setup_room")     # 作業部屋の自動生成（任意）

bot.setup_hook = setup_hook
bot.run(TOKEN)
