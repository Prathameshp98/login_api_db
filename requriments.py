try:
    import os
    from tkinter import*
    from tkinter import messagebox
    from PIL import ImageTk,Image
    import psycopg2
except:
    import subprocess
    subprocess.call([sys.executable, "python", "-m", "pip", "--upgrade","pip"])
    subprocess.call([sys.executable, "-m", "pip", "install", "pillow"])
    subprocess.call([sys.executable, "-m", "pip", "install", "pillow"])
