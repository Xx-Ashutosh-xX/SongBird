import discord
from discord.ext import commands



class Help(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot




    @commands.command(pass_context=True, aliases=['h'])
    async def help(self,ctx):
        '''
        Sends a embeded message specifing all the commands currently there
        '''

        embed = discord.Embed(
            colour=discord.Colour.red(),
            title="--SongBird--",
            description="Bot Prefix is - (dash)\n This is a Simple Discord Bot to send Memes & Play Songs\n "
        )
        embed.set_author(name="Made by : Ashutosh", icon_url="https://avatarfiles.alphacoders.com/172/172111.png")
        embed.set_image(url="https://cache.desktopnexus.com/cropped-wallpapers/1336/1336889-1536x864-[DesktopNexus.com].jpg?st=lCApU1D3y09NKbcboq_Pdg&e=1602395457")
        embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/172/172111.png")
        
        embed.add_field(name="join", value="Makes the Bot Join the Voice Channel You are in.", inline=True)
        embed.add_field(name="leave", value="Gives the Latency of the Bot", inline=True)
        embed.add_field(name="play", value="The makes the bot play the song", inline=True)
        embed.add_field(name="pause", value="Pauses the current song being played", inline=True)
        embed.add_field(name="resume", value="Resumes if the song is paused", inline=True)
        embed.add_field(name="add", value="Adds a new song to the Queue", inline=True)
        embed.add_field(name="next", value="Skips the current song being played", inline=True)

        embed.add_field(name="ping", value="Gives the Latency of the Bot", inline=True)
        embed.add_field(name="clear", value="Purges/Clears the given amount of messages", inline=True)

        embed.add_field(name="wiki", value="Posts a Summary of the text provided", inline=True)
        embed.add_field(name="meme", value="Posts a meme from r/memes", inline=True)
        embed.add_field(name="dank", value="Posts a meme from r/Dankmemes", inline=True)
        

        embed.set_footer(text="Made with LOVE")

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Help(bot))