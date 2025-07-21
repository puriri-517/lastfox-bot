import discord
from discord.ext import commands
from discord import app_commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="指定した件数のメッセージを削除します")
    @app_commands.describe(amount="削除する件数（1〜100）")
    async def clear(self, interaction: discord.Interaction, amount: int):
        # まず応答を予約する
        await interaction.response.defer(ephemeral=True)

        if not interaction.channel.permissions_for(interaction.user).manage_messages:
            await interaction.followup.send("⚠️ メッセージの管理権限が必要です。")
            return

        if amount < 1 or amount > 100:
            await interaction.followup.send("⚠️ 1～100の範囲で指定してください。")
            return

        deleted = await interaction.channel.purge(limit=amount + 1)
        await interaction.followup.send(f"{len(deleted) - 1}件のメッセージを削除しました。", delete_after=5)

    async def cog_load(self):
        self.bot.tree.add_command(self.clear)

async def setup(bot):
    await bot.add_cog(ClearCog(bot))

