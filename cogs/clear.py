import discord
from discord.ext import commands
from discord import app_commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="clear", description="指定した数のメッセージを削除します")
    @app_commands.describe(amount="削除するメッセージの数（最大100件）")
    async def clear(self, interaction: discord.Interaction, amount: int):
        if not interaction.channel.permissions_for(interaction.user).manage_messages:
            await interaction.response.send_message("⚠️ メッセージの管理権限がありません。", ephemeral=True)
            return

        deleted = await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(
            f"{len(deleted)}件のメッセージを削除しました。", ephemeral=True
        )

    async def cog_load(self):
        self.bot.tree.add_command(self.clear)

    async def cog_unload(self):
        self.bot.tree.remove_command(self.clear.name)

async def setup(bot):
    await bot.add_cog(ClearCog(bot))
