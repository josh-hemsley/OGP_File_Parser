import time
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parse_text import parse_coordinates


class MyHandler(FileSystemEventHandler):
    file_cache = {}

    def on_created(self, event):
        seconds = int(time.time())
        key = (seconds, event.src_path)
        if key in self.file_cache:
            return
        self.file_cache[key] = True
        print(f"{event.src_path} was added to the folder.")
        if event.src_path.endswith('.txt'):
            print('The file is a text file, exporting coordinate data.')
            time.sleep(1)
            print('...')
            time.sleep(1)
            parse_coordinates.parse_coord_text(event.src_path)
            os.remove(event.src_path)  # Deletes the file after processing
        else:
            print(f'The file is not a .txt.')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = "C:\\TEST\\"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
