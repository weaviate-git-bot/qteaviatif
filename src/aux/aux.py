
import sys


def print_progress_bar(thread_id, progress, intro = 'Thread', message = '', print_lock = None):
    progress_bar_length = 30
    progress_fraction = progress / 100.0
    filled_length = int(progress_bar_length * progress_fraction)
    progress_bar = '=' * filled_length + ' ' * (progress_bar_length - filled_length)

    message_txt = '\t - ' + message if message else ''    
    thread_id_txt = str(thread_id)
    if thread_id < 10:
        thread_id_txt = '0' + thread_id_txt
        
    # Move cursor up if thread_id > 0
    if thread_id > 0:
        sys.stdout.write(f"\033[{thread_id}A")

    sys.stdout.write("\033[2K")  # Clear current line

    # Print the progress bar
    print(f"{intro} ({thread_id_txt}): [{progress_bar}] {progress}% {message_txt}\r", end="", flush=True)
        
    # Move cursor down to the initial position
    if thread_id > 0:
        sys.stdout.write(f"\033[{thread_id}B")


def print_thread_message(thread_id, intro = 'Thread', message = ''):
    # Move cursor up if thread_id > 0
    if thread_id > 0:
        sys.stdout.write(f"\033[{thread_id}A")
    
    thread_id_txt = str(thread_id)
    if thread_id < 10:
        thread_id_txt = '0' + thread_id_txt

    # Print the progress bar
    print(f"{intro} ({thread_id_txt}): {message}\r", end="", flush=True)
    
    # Move cursor down to the initial position
    if thread_id > 0:
        sys.stdout.write(f"\033[{thread_id}B")


def print_progress(progress_list):
    for process_id, progress in enumerate(progress_list):
        progress_bar_length = 30
        progress_fraction = progress / 100.0
        filled_length = int(progress_bar_length * progress_fraction)
        progress_bar = '=' * filled_length + ' ' * (progress_bar_length - filled_length)
        print(f"Process {process_id}: [{progress_bar}] {progress}%")
    # Move cursor up by the number of lines equal most to least important keywords
    sys.stdout.write(f"\033[{len(progress_list)}A")