import discord
from discord.ext import commands
from discord import app_commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="指定した件数のメッセージを削除します")
    @app_commands.describe(amount="削除する件数（1〜100）")
    async def clear(self, interaction: discord.Interaction, amount: int):
        if not interaction.channel.permissions_for(interaction.user).manage_messages:
            await interaction.response.send_message("⚠️ メッセージの管理権限が必要です。", ephemeral=True)
            return

        if amount < 1 or amount > 100:
            await interaction.response.send_message("⚠️ 1～100の範囲で指定してください。", ephemeral=True)
            return

        deleted = await interaction.channel.purge(limit=amount + 1)
        await interaction.response.send_message(f"{len(deleted)-1}件のメッセージを削除しました。", delete_after=5)

async def setup(bot):
    await bot.add_cog(ClearCog(bot))

