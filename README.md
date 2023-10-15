<h1>cs50x</h1>
<p>Coming Soon</p>
<br>
</h1>cs50p</h1>
<p>
  This Python script is designed for users' efficiency, speed, and time management and serves the purpose of scheduling and launching virtual meetings.
  It leverages the capabilities of the schedule library to facilitate event scheduling. See https://pypi.org/project/schedule/.
  The script also validates the user input, and then the user will make a decision to schedule a meeting outright or simulate a lunch break followed by a meeting.
  In summary, this script is a valuable tool for users who want to streamline their virtual meeting routines. It combines the power of automation with some minor command-line interface interaction.
</p> 
```
Video Demo: <https://www.youtube.com/watch?v=OI5n7S5u3Sw>
```
  It is like your personal little CLI script just for opening virtual meetings.
  
  1. Open your terminal and follow the prompts to schedule and launch virtual meetings.
  2. Browser Pop-Up Blockers: Be aware that some web browsers might block pop-ups, which could prevent the virtual meeting link from opening.
  3. On the first attempt, you may need to adjust your browser settings for this to work correctly.
  4. Please be advised to adjust your Google Meet, Teams app, Zoom app, etc. to turn off video and set the mic to off when joining meetings.
``` 
  git clone https://github.com/shaqduggan/cs50.git
  pip install -r requirements.txt
  python project.py
  IndexError: list index out of range
  python project.py "copy and paste valid url link here"
  Please provide a valid meeting link URL
  python project.py "https://www.youtube.com/watch?v=OI5n7S5u3Sw"
  Welcome to your virtual meeting scheduler. Please follow the prompts.
  Enter m for meeting or l for lunch:
```
<h1>Design Choice</h1>
<p>
  If the user chooses M for meeting to schedule a virtual meeting outright, I chose to run an infinite loop that will print "not yet..." every 10 minutes until the meeting time condition is met in the time_timer() method.
  In situations where a meeting time has been scheduled for the far future, this will result in an excessive amount of output on the system. This could be inefficient and cause excessive output in memory.
  However, the time_timer() method is intended to be used for a meeting time that will likely be within an 8-hour workday. I'll keep this strategy.
  Click Ctrl + C in the command-line terminal to stop any processes in the terminal. if, for some reason, the infinite loop still continues after the meeting is launched or is unintended.
  If the user chooses L for lunch to schedule a virtual meeting directly after lunch, I chose to run a loop with the constraints of a range of 30 to 60 minutes.
  This will simulate a standard lunch in a business setting and will execute a "not yet..." message every second until lunch ends, and it will start a countdown at 10 seconds in the open_meeting_after_lunch() method.
  Due to the fact that the open_meeting_after_lunch() method should only be run for a maximum of an hour, I chose to continue the message execution for at least 1800 seconds and at most 3600 seconds, or an hour. I'll keep this strategy.
</p>
