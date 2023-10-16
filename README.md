# k4hrbot
a chat bot for anyone playing k4hr.

if a chatter wants to know the state of your run they can type !k4att and see this output:

![image](https://github.com/shnenanigans/k4hrbot/assets/83895136/238d75c8-b82e-4952-80ad-e4af9694f5fc)

The bot must be hosted locally because it reads off your speedrunigt files.

To get the bot working, you need twitchio and python.

download python: https://www.python.org/downloads/

once you have python, you need 'pip' in order to load the twitchio module.

in your command prompt, type `python --version` to see if python is installed properly.

then, paste in `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py` and press enter.

now do `python get-pip.py`

if all goes smoothly, you have pip installed successfully. check https://phoenixnap.com/kb/install-pip-windows if you have problems.

once done, you need twitchio.

type `py -m pip install -U twitchio` into command prompt.

Now you have setup all the hard parts. all you need now is to make your account a twitch bot.

now open main.py in a text or code editor (notepad is fine)

generate your twitch token from https://twitchtokengenerator.com/

paste it into 'YOURTOKEN'. apostrophes should be included.

next, put your channel name into 'YOURCHANNEL' (apostrophes included again)

you also have the option of changing the command name to whatever you want in (name="k4att")

![image](https://github.com/shnenanigans/k4hrbot/assets/83895136/21d5f626-ccfd-40a4-8844-a3d3059c6524)

all you have to do now is run main.py. if double clicking it doesnt work, make a new file called run.txt and write `python main.py` into it. change the .txt to .bat to make it a batch file and double click it to run the bot.

voila! should work 
