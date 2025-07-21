import discord
from discord import ui, Interaction

class SetupButtonView(ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    @ui.button(label="🔧 セットアップを開始する", style=discord.ButtonStyle.primary, custom_id="start_setup")
    async def start_setup(self, interaction: Interaction, button: ui.Button):
        # ✅ DMでは動作させない（Guild が必要）
        if interaction.guild is None:
            await interaction.response.send_message(
                "⚠️ この操作はサーバー内でのみ使用できます。",
                ephemeral=True
            )
            return

        member = interaction.guild.get_member(interaction.user.id)
        if not member.guild_permissions.administrator:
            await interaction.response.send_message(
                "⚠️ セットアップはサーバー管理者のみが実行できます。",
                ephemeral=True
            )
            return

        await interaction.response.send_message("✅ セットアップを開始します。", ephemeral=True)

        guild = interaction.guild

        # ✅ チャンネル作成
        channel_name = "LastFox-操作部屋"
        existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not existing_channel:
            try:
                new_channel = await guild.create_text_channel(channel_name)
                await new_channel.send("📌 こちらから操作できます。今後ボタンを追加していきます。")
            except discord.Forbidden:
                await interaction.followup.send("⚠️ チャンネル作成に必要な権限がありません。", ephemeral=True)
        else:
            await interaction.followup.send("✅ 操作部屋はすでに存在しています。", ephemeral=True)

        # ✅ ロール作成
        role_name = "LastFox管理者"
        existing_role = discord.utils.get(guild.roles, name=role_name)
        if not existing_role:
            try:
                await guild.create_role(name=role_name, permissions=discord.Permissions(administrator=True))
                await interaction.followup.send(f"✅ ロール『{role_name}』を作成しました。", ephemeral=True)
            except discord.Forbidden:
                await interaction.followup.send("⚠️ ロール作成に必要な権限がありません。", ephemeral=True)
        else:
            await interaction.followup.send(f"✅ ロール『{role_name}』はすでに存在しています。", ephemeral=True)
