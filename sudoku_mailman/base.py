import os
from dotenv import load_dotenv

load_dotenv()

# example constant variable
NAME = "spotify_terminal_plugin"


HOST = os.getenv('HOST_URI')