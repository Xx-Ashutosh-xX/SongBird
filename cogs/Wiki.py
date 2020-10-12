import discord
from discord.ext import commands
import wikipedia as wiki

def sendWiki(text):
    '''
    makes a 3 sentence summary from the term provided
    '''
    try:
        sh = wiki.summary(text, sentences = 3)
    except:
       sh = 'Search term is to board to summarize'
    return sh


class Wiki(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(pass_context = True, aliases=['W'])
    async def wiki(self,ctx,st: str):
        '''
        send a small summery made from wiki to the current channel
        '''
        result = sendWiki(st)
        embed = discord.Embed(
        title = st,
        description = result,
        colour = 0xce65dc
        )
        await ctx.send(embed = embed)
        await ctx.message.delete()

    
def setup(bot):
    bot.add_cog(Wiki(bot))
