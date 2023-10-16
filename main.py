
from twitchio.ext import commands
import os
import datetime
import json

class Bot(commands.Bot):

    def __init__(self):
        # get token from https://twitchtokengenerator.com/
        super().__init__(token='YOURTOKEN', prefix='!', initial_channels=['YOURCHANNEL'])
        self.k4 = kayfourhour()

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


#wrote literally every function with chatgpt i love technology
class kayfourhour:
    def __init__(self):
        self.records = self.get_user_home_directory() #replace with path manually if you get an error. usually is "C:\Users\user\speedrunigt\records" (include apostrophes)
        self.completed_runs = {}
        return

    def get_user_home_directory(self):
        try:
            username = os.getlogin()
            records = f"C:\\Users\\{username}\\speedrunigt\\records"
            return records
        except Exception as e:
            print("cannot find path to your speedrunigt records. Please put them in manually.")
            return
        
    def get_last_4hrs(self):
        """return list of the names of files created in only the last 4 hours"""
        current_time = datetime.datetime.now()
        four_hours_ago = current_time - datetime.timedelta(hours=4)
        recent_files = []
        
        for root, dirs, files in os.walk(self.records):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
                
                if file_creation_time >= four_hours_ago:
                    recent_files.append(f"{self.records}\\{filename}")

        return recent_files
    
    def get_rta(self, rta: int) -> str:
        seconds = rta // 1000
        milliseconds = rta % 1000
        minutes, seconds = divmod(seconds, 60)
        formatted_time = f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        return formatted_time

    def sec_to_hour(self, seconds):
        return seconds/3600
    
    def time_since_now(self, file):
        current_time = datetime.datetime.now()
        file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file))
        difference = current_time - file_creation_time
        return round(self.sec_to_hour(difference.total_seconds()), 2)

    def check_completions(self):
        recent_files = self.get_last_4hrs()
        for file in recent_files:
            with open(file, "r", encoding='cp1251') as j:
                try:
                    data = json.load(j)
                except:
                    print("if you get here there is most likely an encoding issue. try just deleting the encoding specification entirely (in the with open thing just above this)")
                if data["is_completed"]:
                    self.completed_runs[file] = {"rta": self.get_rta(data["final_rta"]), "created_hours_ago": self.time_since_now(file)} #{filename: {rta: 3, modified: 2 hours ago}, filename2: {rta: 5, modified: 8 hours ago}}
        self.delete_old()
        return self.completed_runs
    
    def delete_old(self):
        """get rid of files in the completed runs dict that are older than 4 hours"""
        files = []
        for key in self.completed_runs:
            files.append(key)
        for file in files:
            if self.completed_runs[file]["created_hours_ago"] > 4.00:
                del self.completed_runs[file]
    
    def find_oldest_run(self, runs):
        oldtime = 0
        for run in runs:
            time = runs[run]["created_hours_ago"]
            if time > oldtime:
                oldtime = time
        return round(4-oldtime, 2) #4 minus time since first run is gonna be the time remaining

    def get_command(self):
        runs = self.check_completions()
        msg = f"time left: {self.find_oldest_run(runs)} hours. "
        i = 1
        for run in runs:
            rta = runs[run]["rta"]
            msg += f"Run {i}: {rta}. "
            i += 1
        return msg


bot = Bot()
bot.run()