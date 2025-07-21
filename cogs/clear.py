import discord
from discord.ext import commands
from discord import app_commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # ✅ スラッシュコマンド：/clearbot
    @app_commands.command(name="clearbot", description="指定した件数のメッセージを削除します")
    @app_commands.describe(amount="削除する件数（1〜100）")
    async def clearbot(self, interaction: discord.Interaction, amount: int):
        await interaction.response.defer(ephemeral=True)

        if not interaction.channel.permissions_for(interaction.user).manage_messages:
            await interaction.followup.send("⚠️ メッセージの管理権限が必要です。")
            return

        deleted = await interaction.channel.purge(limit=amount + 1)
        await interaction.followup.send(f"✅ {len(deleted) - 1}件のメッセージを削除しました。", ephemeral=True)

    # ✅ プレフィックスコマンド：!clear
    @commands.command(name="clear")
    async def clear_legacy(self, ctx: commands.Context, amount: int):
        if not ctx.channel.permissions_for(ctx.author).manage_messages:
            await ctx.send("⚠️ メッセージの管理権限が必要です。")
            return

        deleted = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"✅ {len(deleted) - 1}件のメッセージを削除しました。", delete_after=5)

# ✅ コグとしてBotに登録
asyn
