import sys 
import time 
import random 
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = '/Users/bhumisehgal/Documents/whjr/project102/From'
to_dir = '/Users/bhumisehgal/Documents/whjr/project102/To-Destination'

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")

    def on_modified(self, event):
        print(f"Someone modified {event.src_path}!")

    def on_moved(self, event):
        print(f"Someone moved {event.src_path}!")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
        print('stopped!')
        observer.stop