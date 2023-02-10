import discord
from discord.ext import commands

from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.playing = False
        self.paused = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnected_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': info['formats'[0]['url']], 'title': info['title']}

    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.playing = True
            music_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

    @commands.command(name='play', aliases=['p', 'playing'], help='Plays the selected song from Youtube')
    async def play(self, ctx, *args):
        pass
