
from twitchio.ext import commands
import k4hr

class Bot(commands.Bot):

    def __init__(self):
        # get token from https://twitchtokengenerator.com/
        super().__init__(token='YOURTOKEN', prefix='!', initial_channels=['YOURCHANNEL'])
        self.k4 = k4hr.kayfourhour()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command(name="k4att") #change to whatever you want the command to be
    async def k4att(self, ctx: commands.Context):
        await ctx.send(self.k4.get_command())
        return

    async def event_command_error(self, context: commands.Context, error: Exception):
        if isinstance(error, commands.CommandNotFound):
            return
        print(error)

bot = Bot()
bot.run()