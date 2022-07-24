#! python3
# prettyprintstopwatch.py - Take the stopwatch program from CH 17 and format
# it to print neatly to the console

import time
import pyperclip


def pretty_print_stopwatch():
    """
    User presses "enter" to reset the stop watch, or "Ctrl- C" to end the program. Store the
    current lap time as "lap_time" and the total lap times as "total_time". Format the printed
    output and store it as "formatted_times". Append "formatted_times" to a list, then join
    the list as a string and copy it to the clipboard.
    """
    print(
        'Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.'
    )
    input()  # press Enter to begin
    print("Started.")
    start_time = time.time()  # get the first lap's start time
    last_time = start_time
    lap_num = 1
    total_times = []
    try:
        while True:
            input()
            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)
            formatted_times = (
                f"Lap # {lap_num}: "
                + f"{total_time} ".rjust(7)
                + "("
                + f"{lap_time})".rjust(7)
            )
            print(formatted_times, end="")
            total_laps.append(f"{formatted_times}\n")
            lap_num += 1
            last_time = time.time()  # reset the last lap time
    except KeyboardInterrupt:
        pyperclip.copy("".join(total_times))
        print("\nDone.")


if __name__ == "__main__":
    pretty_print_stopwatch()
