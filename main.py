import threading
import keyboard
from fisher import start_fishing, stop_fishing, running as fisher_running

fishing_thread = None

def toggle_bot():
    global fishing_thread
    if fishing_thread is not None and fishing_thread.is_alive():
        stop_fishing()
        fishing_thread.join()
        fishing_thread = None
    else:
        print("Bot starting...")
        fishing_thread = threading.Thread(target=start_fishing)
        fishing_thread.start()

print("Bot ready. Press F8 to start/stop it.")
print("Press F9 to exit the script.")


keyboard.add_hotkey("f8", toggle_bot)

keyboard.wait("f9")

if fishing_thread is not None and fishing_thread.is_alive():
    stop_fishing()
    fishing_thread.join()

print("Script stopped.")
