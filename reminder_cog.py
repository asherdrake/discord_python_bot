import discord
from discord.ext import commands
from threading import Thread
import time
import asyncio
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
from views import reminder_view

class reminder_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sched = AsyncIOScheduler()
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    async def start_scheduler(self):
        if (not self.sched.running):
            self.sched.start()
    
    @commands.command(name="reminder", aliases=['remind', 'setreminder'])
    async def set_reminder(self, ctx, user_date, user_time, reminder_text):
        date_components = list(map(int, user_date.split('/')))
        time_components = list(map(int,user_time.split(':')))
        exec_date = datetime(date_components[2], date_components[0], date_components[1], hour=time_components[0], minute=time_components[1], second=time_components[2])
        await ctx.send(f'Setting reminder, "{reminder_text}" to be sent to {ctx.author.mention} at {exec_date}.')
        job = self.sched.add_job(self.reminder_job, run_date=exec_date, args=[ctx, reminder_text])
        await self.start_scheduler()
        await ctx.send('Reminder set.')

    async def reminder_job(self, ctx, text):
        await ctx.send(f'{ctx.author.mention}, {text}')

    async def get_seconds(self, time):
        pass

    async def cancel_reminder(self, ctx):
        reminder_view.reminder_menu(ctx, await self.parse_jobs())

    @commands.command(name="display_reminders", aliases=['display', 'reminders'])
    async def display_reminders(self, ctx):
        await ctx.send(await self.parse_jobs())

    async def parse_jobs(self):
        jobs = self.sched.get_jobs()
        job_list = ''
        for index, job in enumerate(jobs):
            job_list += ('%d. User: ' + str(job.args[0].author) + ' - Reminder: "' + job.args[1] + '" at time "' + str(job.next_run_time) + '"\n') % (index + 1)
        return job_list

async def setup(bot):
    await bot.add_cog(reminder_cog(bot))