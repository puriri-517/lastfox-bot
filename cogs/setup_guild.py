import discord
from discord.ext import commands
from views.setup_button import SetupButtonView

class SetupGuild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        # 👑 管理者を1人取得（サーバー主など）
        admin_user = None
        for member in guild.members:
            if member.guild_permissions.administrator and not member.bot:
                admin_user = member
                break

        # 📩 管理者にDMを送信してみる
        if admin_user:
            try:
                await admin_user.send(
                    f"🔧 **{guild.name}** にLastFoxを導入していただきありがとうございます！\n"
                    f"セットアップを開始するには、以下のボタンを押してください。",
                    view=SetupButtonView(self.bot)
                )
                return  # 成功したらここで終わり
            except discord.Forbidden:
                print(f"⚠️ 管理者 {admin_user} にDMを送れませんでした。")

        # 🏠 サーバー内で投稿できるチャンネルを探す
        fallback_channel = None
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                fallback_channel = channel
                break

        if fallback_channel:
            try:
                await fallback_channel.send(
                    f"📢 Botのセットアップを行うには、以下のボタンから開始してください。",
                    view=SetupButtonView(self.bot)
                )
            except discord.Forbidden:
                print(f"⚠️ {guild.name} のチャンネルに送信できませんでした。")
        else:
            print(f"❌ セットアップ案内を送信できるチャンネルが見つかりませんでした。")

async def setup(bot: commands.Bot):
    await bot.add_cog(SetupGuild(bot))
