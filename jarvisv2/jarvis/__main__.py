import time
import random
import threading
import queue
from colorama import Fore
from AppOpener import open, close

from spotify import spotify_client
from audio import audio_recoder

print_queue = queue.Queue()

def _printer_worker():
    while True:
        message = print_queue.get()
        for char in message:
            print(char, end="", flush=True)
            time.sleep(0.05 * random.random())
        print(flush=True)
        print_queue.task_done()

threading.Thread(target=_printer_worker, daemon=True).start()

def printj(message):
    print_queue.put(Fore.CYAN + message + Fore.RESET)

printj("Good morning, sir.")
message = str(input())

def string_contains(set=(), match=None):
    string = message.lower()
    for sub in set:
        if sub in string:
            return True

    if not match == None:
        return match in string

    return False

def get_random_response(responses={}):
    return responses[random.randint(0, len(responses) - 1)]


while not string_contains(( "kill", "end", "exit", "bye", "good evening", "good night" )):
    ok = False
    if string_contains(( "music", "song" )):
        if string_contains(( "move", "transfer", "start", "play", "resume" )):
            printj("Playing your music, sir.")
            ok = False
            if string_contains(match="phone"):
                ok = spotify_client.start_playback_phone()
            elif string_contains(match="computer"):
                ok = spotify_client.start_playback_computer()
            else:
                ok = spotify_client.start_playback()

            if ok:
                printj("Enjoy your music!")
        elif string_contains(( "pause", "stop" )):
            printj("Right away, sir!")
            ok = spotify_client.stop_playback()
        elif string_contains(( "skip", "next" )):
            printj("aye")
            ok = spotify_client.next_song()
        elif string_contains(match="back"):
            printj("Right away!")
            ok = spotify_client.previous_song()

    elif string_contains(( "hello", "good morning" )):
        printj("Hello sir, thank you for visiting.")
        ok = True
    elif string_contains(( "bye", "good evening" )):
        printj("Good evening sir, have a good night.")
        ok = True
    elif string_contains(( "start", "open", "begin" )):
        if (string_contains(( "intellij",  ))):
            printj("Booting IntelliJ for you, sir!")
            open("intellij", match_closest=True, output=False)
        elif (string_contains(( "vscode", "code", "coding", "programming" ))):
            printj("Booting VSCode for you, sir!")
            open("visual studio code", match_closest=True, output=False)
        elif (string_contains(( "spotify" ))):
            printj("Opening Spotify!")
            open("spotify", match_closest=True, output=False)
        else:
            printj("Unrecognized app.")
        ok = True
        
    elif string_contains(( "close", "stop" )):
        if (string_contains(("intellij"))):
            printj("Yeah, fuck that app.")
            close("intellij", match_closest=True, output=False)
        elif (string_contains(( "vscode", "coding" ))):
            printj("Right away, sir.")
            close("visual studio code", match_closest=False, output=False)
        elif (string_contains(( "spotify" ))):
            printj("Tunes are over, sir.")
            close("spotify", match_closest=True, output=False)
        else:
            printj("Unrecognized app.")
        ok = True

    if not ok:
        printj(get_random_response(( "Unavailable, sir.", "I cannot complete your request at this time.", "Service unavailable, sir." )))

    print_queue.join()

    message = str(input())
    message = message.lower()

printj(get_random_response(( "Goodbye, sir.", "Until next time, sir.", "Aye, sir.", "So long!" )))

print_queue.join()
