import discord
from discord.ext import commands

SETUP_MESSAGE = (
    "**📦 LastFox Bot セットアップのご案内**\n"
    "このBotを使用するには、まず `/setup` コマンドをサーバー内で実行してください。\n"
    "`LastFox` という名前のロールを作成し、使用を許可したいメンバーに付与してください。\n\n"
    "不明点があればお気軽にお問い合わせください！"
)

class SetupNotice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        # 優先：system_channel に送信
        if guild.system_channel and guild.system_channel.permissions_for(guild.me).send_messages:
            try:
                await guild.system_channel.send(SETUP_MESSAGE)
                return
            except discord.Forbidden:
                pass  # 送れなければ次へ

        # 次善策：最初に読み取れるチャンネルを探す
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                try:
                    await channel.send(SETUP_MESSAGE)
                    return
                except discord.Forbidden:
                    continue  # 他のチャンネルを試す

        # 最後に：ログ出力
        print(f"⚠️ {guild.name} に案内メッセージを送れませんでした。")

async def setup(bot):
    await bot.add_cog(SetupNotice(bot))
