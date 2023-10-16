#!/usr/bin/env python3
import sys
import time
import webbrowser
import schedule
from datetime import date
from datetime import datetime
from urllib.parse import urlparse


"""
Run pip install -r requirements.txt in the command line terminal to install the necessary dependencies
Click Ctrl + C in the command-line terminal to stop any processes in the terminal. if, for some reason, the infinite loop still continues after the meeting is launched or is unintended.
"""


def is_valid_url(url):
    """This will check the command-line argument for a valid URL"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def is_valid_char(ch):
    """This will check if start variable is valid"""
    return isinstance(ch, str) and ch.lower() in ["l", "m"]


def is_valid_time(t):
    """This will check if the time variable is valid (in the format HH:MM)"""
    if isinstance(t, str):
        try:
            hr, min = t.split(":")
            if 0 <= int(hr) <= 23 and 0 <= int(min) <= 59:
                return True
        except ValueError:
            pass
    return False


while True:
    VIRTUAL_MEETING_LINK = sys.argv[1] # Use command line to paste url link or hardcode it here
    if is_valid_url(VIRTUAL_MEETING_LINK):
        break
    else:
        print("Please provide a valid meeting link URL")
        sys.exit()


def main():
    print("Welcome to your virtual meeting scheduler. Please follow the prompts.")
    try:
        start = input("Enter m for meeting or l for lunch: ")
        if is_valid_char(start):
            if start == "l":
                try:
                    lunch_minutes = int(input("Minutes: "))
                    if 30 <= lunch_minutes <= 60:
                        open_meeting_after_lunch(lunch_minutes)
                    else:
                        print("Try again with a number in range of 30 - 60")
                        sys.exit()
                except ValueError:
                    print("Not a valid number")
                    sys.exit()
            elif start == "m":
                scheduled_meeting_time = input("Enter Time (for example 19:02): ")
                if is_valid_time(scheduled_meeting_time):
                    time_timer(scheduled_meeting_time)
                else:
                    print("Time Format Error Try again in this format HH:MM")
                    sys.exit()
        else:
            print("Only Enter letter M or L to start python script : ")

    except ValueError:
        print(
            "Check if start is a proper letter character\nOnly enter a number value for minutes"
        )
        sys.exit()


def open_meeting():
    """
    This will open a link on the web browser, ideally for your virtual meetings.
    Google Meet, Teams app, Zoom app, etc.
    """
    return webbrowser.open(f"{VIRTUAL_MEETING_LINK}")


def open_meeting_after_lunch(minutes=30):
    """This function is meant to be called
    when there is a virtual meeting scheduled after a lunch break"""
    lunch_time = minutes * 60

    # How do I know my lunch break is over?
    # I will create an infinite loop that will run until the countdown timer is complete.
    # 1800 seconds equals 30 minutes, which is my default scheduled daily total lunch break.

    while lunch_time > 1:
        schedule.run_pending()
        time.sleep(1)
        lunch_time -= 1
        if lunch_time < 11:
            print(f"{lunch_time}...")
        else:
            print("Not Yet...")

    print("Lunch break over")
    open_meeting()
    sys.exit()


def get_meeting(meeting_time):
    today = date.today().weekday()
    day_of_week = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
    }

    try:
        if today in day_of_week:
            getattr(schedule.every(), day_of_week[today]).at(meeting_time).do(
                open_meeting()
            )
        else:
            print("Don't work on a weekend silly")
    except TypeError:
        print("Test your Audio and Video")
        return True
    else:
        return False


def time_timer(meeting_time):
    """This function will run until the meeting time and then open the meeting link"""

    cnt = 0
    while True:
        current_date_time = datetime.now()  # Output: 2023-10-13 11:09:49.274451
        hr, min, sec = current_date_time.strftime("%H:%M:%S").split(":")
        current_time = f"{int(hr):02}:{int(min):02}"
        schedule.run_pending()
        time.sleep(1)
        if meeting_time == current_time:
            print(f"{current_time} Meeting has started...")
            get_meeting(meeting_time)
            break
        else:
            if cnt == 600:
                print(
                    f"{current_time} Not Yet..."
                )  # Update every 10 minutes to reduce output
                cnt = 0
            cnt += 1
    sys.exit()


if __name__ == "__main__":
    main()
