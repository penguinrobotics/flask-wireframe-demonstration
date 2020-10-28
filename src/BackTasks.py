import Configuration as config
import TeamStore as teams
from threading import Thread
import FlaskServer as fs
import time

running = False
currentThread = None

def start_background_services():
    print("Preparing Thread")
    global running
    global currentThread
    currentThread = Thread(target=do_background_services)
    currentThread.start()

def do_background_services():
    print("Threaded function initializing")
    global running
    running = True
    while fs.active:
        teams.update_online()
        teams.save_to_file()
        time.sleep(10)
        print("Backtask update")
    print("Background Thread Exiting")
    running = False
