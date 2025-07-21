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

# インテント設定（!コマンドやユーザー取得に必要）
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.members = True  # 管理者DM送信に必要

# Bot初期化
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot起動時
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

# サーバーに参加したとき（管理者に案内送信）
@bot.event
async def on_guild_join(guild: discord.Guild):
    print(f"📥 新しいサーバーに参加：{guild.name} ({guild.id})")

    # 管理者と思われるメンバーを探す
    admin = None
    for member in guild.members:
        if member.guild_permissions.administrator and not member.bot:
            admin = member
            break

    if admin:
        try:
            await admin.send("✅ LastFoxを導入いただきありがとうございます！\nサーバー内で `/setup` コマンドを実行して、初期セットアップを行ってください。")
            print(f"📩 管理者 {admin} にDMを送信しました")
            return
        except discord.Forbidden:
            print("⚠️ 管理者へのDMが拒否されました")

    # fallback: 投稿可能なチャンネルを探す
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            try:
                await channel.send("✅ LastFoxを導入いただきありがとうございます！\nサーバー内で `/setup` コマンドを実行して、初期セットアップを行ってください。")
                print(f"📢 サーバー内チャンネル {channel.name} に案内を送信しました")
                break
            except Exception as e:
                print(f"⚠️ チャンネルへの案内送信に失敗しました: {e}")

# Cogの読み込み
@bot.event
async def setup_hook():
    print("🔄 setup_hook が呼び出されました")
    try:
        await bot.load_extension("cogs.clear")
        print("✅ cogs.clear を読み込みました")
    except Exception as e:
        print(f"❌ cogs.clear 読み込み失敗: {e}")

    try:
        await bot.load_extension("cogs.setup_invite")
        print("✅ cogs.setup_invite を読み込みました")
    except Exception as e:
        print(f"❌ cogs.setup_invite 読み込み失敗: {e}")

# Bot起動
print("🚀 Bot を起動します")
bot.run(TOKEN)

