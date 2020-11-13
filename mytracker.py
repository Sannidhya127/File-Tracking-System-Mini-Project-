import time as t
from datetime import date
from datetime import time
from datetime import datetime
from watchdog.observers import Observer
import watchdog.events
from watchdog.events import PatternMatchingEventHandler

# class watchdog.events.FileModifiedEvent(src_path):


def afterData():
    pass
    # To be used later
    # initial = input()
    # if initial == "bit add --a":
    #     commitmessage = input("Please enter your commit message here: ")

    #     f = open(f"{event.src_path}.txt", "a")
    #     f.write(str(datetime.now()))
    #     f.write(f": {commitmessage}\n")
    #     print("Commit saved. You can use sds log --all to view all the commits.")
    # elif initial == "com --skp":
    #     print("Skipped staging files. Continuing")
    # else:
    #     print(
    #         f"Invalid input {initial}.\n Did you mean sds commit --d ?\nUse sds --help for refference")

    # commitalert = "Use  \033[0;31mdata commit --d to make a commit or com --skp to skip"
    # print(commitalert)
    # com = input()
    # if com == "data commit --d":


def on_created(event):
    print(f"\033[0;32m{event.src_path} has been created!")


def on_deleted(event):
    print(f"\033[0;31mDeleted {event.src_path}")


def on_modified(event):
    print(f"\033[0;36mModified {event.src_path}")


def on_moved(event):
    print(f"\033[0;34mRenamed or moved {event.src_path} to {event.dest_path}.")


if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    is_directory = False
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    path = "."   # !Current Working Directory
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    f = open(f"data.com.null.txt", "a")
    f.write(str(my_observer.start()))
    try:
        while True:
            t.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
