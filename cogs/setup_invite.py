import discord
from discord.ext import commands

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

        # 📩 管理者にDMを送信
        if admin_user:
            try:
                await admin_user.send(
                    f"👋 **{guild.name}** に LastFox を導入していただきありがとうございます！\n"
                    f"サーバー内で `/setup` コマンドを実行すると、操作部屋と管理ロールを自動で作成します。"
                )
                return  # DM送信成功で終了
            except discord.Forbidden:
                print(f"⚠️ 管理者 {admin_user} にDMを送れませんでした。")

        # 🏠 チャンネルへの案内
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                try:
                    await channel.send(
                        "👋 LastFoxを導入ありがとうございます！\n"
                        "サーバー内で `/setup` コマンドを実行すると、操作部屋と管理ロールを自動で作成します。"
                    )
                    print(f"📢 {guild.name} のチャンネル {channel.name} に案内を送信しました。")
                    return
                except discord.Forbidden:
                    print(f"⚠️ {guild.name} のチャンネル {channel.name} に送信できませんでした。")

        print(f"❌ {guild.name} に案内を送信できるチャンネルが見つかりませんでした。")

async def setup(bot: commands.Bot):
    await bot.add_cog(SetupGuild(bot))
