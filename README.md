# Summary
The idea for this program arose out of my need for a new laptop; the laptop I wanted was out of my budget, so I decided to track its price on amazon.com until it fell inside a price range that I could afford.

When the app is run, it scrapes the item's price from amazon. It then takes this float and compares it to my set max price; if the retrieved price is below the set maximum, an email notification is sent, otherwise, nothing happens.

The app can be set up to run automatically at Startup (more below on how to set this up). Also, the email credentials are blank variables, they have to be edited for the program to work. See scraper.py -> line 5. 
## How to Run at Start up (Windows only)

To enalbe this feature, it takes several simple steps:

1) Edit the auto.bat file:
    - Copy the path to your python.exe (usually C:\Python38\python.exe), this will vary depending on where python was intalled.
	- Paste this path between the first set of quotes
	- Copy the path to the scraper.py file of this project
	- Paste it between the second set of quotes, then save and close the .bat file

2) Add the auto.bat file to Windows' Startup folder:
	- Here's a [tutorial](https://support.microsoft.com/en-us/help/4558286/windows-10-add-an-app-to-run-automatically-at-startup) on how to do this.
# Take-Aways
- SMTP: Before this tiny and simple project I was unfamiliar with the Simple Mail Transfer Protocol, and python's smtplib library. They are simple and straight-forward, contrary to my previous belief.
- Web Scraping: Widened my knowledge in HTTP requests and the use of HTML tags to collect data from websites.
- Task Automation: Learned how to automatically run a program on Windows using batch files and the Windows Starup folder.