import discord
from discord.ext import commands


class Misc(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        '''
        Send a messsage giving the latency of the Bot
        '''
        await ctx.send("Pong! = " + str(round(self.bot.latency*1000)) + "ms")

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=(amount+1))

def setup(bot):
    bot.add_cog(Misc(bot))