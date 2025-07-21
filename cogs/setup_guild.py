import discord
from discord.ext import commands
from discord import app_commands
from views.panel_buttons import PanelButtonView

class SetupGuild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setup", description="操作部屋とロールを作成します（管理者のみ）")
    @app_commands.checks.has_permissions(administrator=True)
    async def setup(self, interaction: discord.Interaction):
        guild = interaction.guild
        channel_name = "LastFox-指令室"
        role_name = "LastFox管理"

        # ✅ チャンネル作成
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not channel:
            try:
                channel = await guild.create_text_channel(channel_name)
            except discord.Forbidden:
                await interaction.response.send_message("❌ チャンネル作成に必要な権限がありません。", ephemeral=True)
                return

        # ✅ ロール作成
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            try:
                await guild.create_role(name=role_name)
            except discord.Forbidden:
                await interaction.response.send_message("⚠️ ロール作成に必要な権限がありません。", ephemeral=True)
                return

        # ✅ 操作パネル送信
        embed = discord.Embed(title="LastFox 操作パネル", description="以下のボタンから機能を選択してください。", color=0x00ccff)
        await channel.send(embed=embed, view=PanelButtonView(self.bot))

        await interaction.response.send_message(f"✅ {channel.mention} とロールを作成しました。", ephemeral=True)

# 👇 関数名を setup → setup_guild_cog に変更
async def setup_guild_cog(bot: commands.Bot):
    await bot.add_cog(SetupGuild(bot))
