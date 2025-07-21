from discord.ext import commands

class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount: int):
        """
        指定した件数のメッセージを削除
        """
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount}件のメッセージを削除しました。", delete_after=5)

async def setup(bot):
    await bot.add_cog(ClearCog(bot))
