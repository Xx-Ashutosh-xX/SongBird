import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import shutil 
import time
from os import system



Queue = {}


class Music(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def join(self,ctx):
        '''
        To make the bot join the Voice Channel you are in
        '''
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.remove(file)


        if voice and voice.is_connected():
            await voice.move_to(channel)

        
        else:
            voice = await channel.connect()
            print(f"The bot has connected to {channel}\n")
            await ctx.send(f"Hiya!!, SongBird Joined {channel}")


    @commands.command(pass_context=True, aliases = ['dc'])
    async def leave(self,ctx):
        '''
        To make the Bot leave the Voice Channel you are in
        '''
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            print(f"The bot has left {channel}")
            await ctx.send(f"Bai Bai !!, SongBird Left {channel}")
        
        else:
            print(f"The bot has connected to {channel}\n")
            await ctx.send(f"Don't think I am in a voice channel")

    @commands.command(pass_context=True, aliases = ['p'])
    async def play(self,ctx, url: str):
        '''
        Play a Song if none is playing currently, from a Youtube/Spotify Link
        '''
        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length-1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more Queued Song(s)\n")
                    Queue.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Song Completed, Playing the next queued\n")
                    print(f"Songs still in Queue : {still_q}")
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, "song.mp3")
                    
                    time.sleep(1)
                    
                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.1

                else:
                    Queue.clear()
                    return
            else:
                Queue.clear()
                print("No Songs were queued before the ending of the last song\n")


        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
                Queue.clear()
                print("Removed old song file")
        except PermissionError:
            print("Trying to delete song file, but its being played")
            await ctx.send("ERROR: Music playing")
            return

        Queue_infile = os.path.isdir("./Queue")
        try:
            Queue_folder = "./Queue"
            if Queue_infile is True:
                print("Removed Old Queue Folder")
                shutil.rmtree(Queue_folder)
        except:
            print("No Old Queue Folder")
        
        await ctx.send("Getting everything ready now ")

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'quite': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading Audio Now\n")
                ydl.download([url])
        except:
            print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if spotify URL)")
            c_path = os.path.dirname(os.path.realpath(__file__))
            system("spotdl -f " + '"'  +c_path + '"' + " -s " + url)
            
        
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")
        
        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.1

        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: {nname[0]}")
        print(f"Playing: {nname[0]}\n")



    @commands.command(pass_context=True)
    async def pause(self,ctx):
        '''
        Pause the Current Song Playing
        '''
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            print("Music Paused")
            voice.pause()
            await ctx.send("Music Paused")
        else:
            print("Music is not playing")
            await ctx.send("Music is not playing")



    @commands.command(pass_context=True)
    async def resume(self,ctx):
        '''
        Resume if the Current Song is Paused
        '''
        voice = get(self.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_paused():
            print("Music Resumed")
            voice.resume()
            await ctx.send("Music Resumed")
        else:
            print("Music is not paused")
            await ctx.send("Music is not Paused")


    @commands.command(pass_context=True)
    async def add(self,ctx, url):
        '''
        To add a Song to the Queue, from a Youtube/Spotify Link
        '''
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is False:
            os.mkdir("Queue")
        DIR = os.path.abspath(os.path.realpath("Queue"))
        q_num = len(os.listdir(DIR))
        q_num += 1
        add_queue = True
        while add_queue:
            if q_num in Queue:
                q_num += 1
            else:
                add_queue = False
                Queue[q_num] = q_num
        
        queue_path = os.path.abspath(os.path.realpath("Queue" + f"\song{q_num}.%(ext)s"))

        ydl_opts = {
            'format': 'bestaudio/best',
            'quite': True,
            'outtmpl': queue_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        await ctx.send("Getting the Song ready now ")

        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print("Downloading Audio Now\n")
                ydl.download([url])
        except:
            print("FALLBACK: youtube-dl does not support this URL, using Spotify (This is normal if spotify URL)")
            q_path = os.path.dirname(os.path.realpath("Queue" + f'\song{q_num}'))
            system(f"spotdl -f " + '"' + q_path + '"' + " -s " + url)
        
        await ctx.send("Added song to the queue.")
        print("Song added to queue\n")




    @commands.command(pass_context=True, aliases=['next'])
    async def skip(self,ctx):
        '''
        To Skip the current song playing to the next one if it is there in the Queue
        '''

        voice = get(self.bot.voice_clients, guild=ctx.guild)

        voice.stop()

        def check_queue():
            Queue_infile = os.path.isdir("./Queue")
            if Queue_infile is True:
                DIR = os.path.abspath(os.path.realpath("Queue"))
                length = len(os.listdir(DIR))
                still_q = length-1
                try:
                    first_file = os.listdir(DIR)[0]
                except:
                    print("No more Queued Song(s)\n")
                    Queue.clear()
                    return
                main_location = os.path.dirname(os.path.realpath(__file__))
                song_path = os.path.abspath(os.path.realpath("Queue") + "\\" + first_file)
                if length != 0:
                    print("Song Skipped, Playing the next queued\n")
                    print(f"Songs still in Queue : {still_q}")
                    song_there = os.path.isfile("song.mp3")
                    if song_there:
                        os.remove("song.mp3")
                    shutil.move(song_path, main_location)
                    for file in os.listdir("./"):
                        if file.endswith(".mp3"):
                            os.rename(file, "song.mp3")

                    time.sleep(1)
                    
                    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: check_queue())
                    voice.source = discord.PCMVolumeTransformer(voice.source)
                    voice.source.volume = 0.1

                else:
                    Queue.clear()
                    return
            else:
                Queue.clear()
                print("No Songs were queued before the ending of the last song\n")

        await ctx.send("Song Skipped, Playing the next queued")
        check_queue()

def setup(bot):
    bot.add_cog(Music(bot))