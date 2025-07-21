import discord
from discord.ext import commands
from discord import app_commands
from views.panel_buttons import PanelButtonView  # ボタンViewを読み込む

class SetupGuild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="setup", description="Botの操作部屋とロールを自動作成します（管理者限定）")
    @app_commands.checks.has_permissions(administrator=True)
    async def setup(self, interaction: discord.Interaction):
        guild = interaction.guild

        # ✅ 操作部屋の作成
        channel_name = "LastFox-指令室"
        existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
        if existing_channel:
            await interaction.response.send_message(f"⚠️ すでに『{channel_name}』が存在します。", ephemeral=True)
            return

        try:
            command_channel = await guild.create_text_channel(channel_name)
        except discord.Forbidden:
            await interaction.response.send_message("❌ チャンネル作成に必要な権限がありません。", ephemeral=True)
            return

        # ✅ 管理ロールの作成（存在しない場合）
        role_name = "LastFox管理"
        existing_role = discord.utils.get(guild.roles, name=role_name)
        if not existing_role:
            try:
                await guild.create_role(name=role_name, mentionable=True, reason="LastFoxの管理ロール")
            except discord.Forbidden:
                await interaction.followup.send("⚠️ ロール作成に必要な権限がありません。", ephemeral=True)

        # ✅ 操作ボタンの設置
        embed = discord.Embed(title="LastFox 操作パネル", description="以下のボタンから機能を選択してください。", color=0x00ccff)
        await command_channel.send(embed=embed, view=PanelButtonView(self.bot))

        await interaction.response.send_message(f"✅ 『{channel_name}』とロールの作成が完了しました！", ephemeral=True)

    # ✅ 権限エラー処理
    @setup.error
    async def setup_error(self, interaction: discord.Interaction, error):
        if isinstance(error, app_commands.errors.MissingPermissions):
            await interaction.response.send_message("❌ このコマンドは管理者のみ実行できます。", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SetupGuild(bot))
