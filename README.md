# Summary
The idea for this program arose out of my need for a new laptop. The laptop I wanted was out of my budget, so I decided to track its price on amazon.com until it fell inside a price range that I was willing to pay.

When the app is executed, it scrapes a given item's price from Amazon. It then takes this number and compares it to my set max price; if the retrieved price is below the set maximum, an email notification is sent, otherwise, nothing happens.

The script can be set up to run automatically on your PC at Startup (below is how to set this up). And the email credentials are simply blank variables, they have to be edited for the script to work. See scraper.py -> line 5. 
## How to Run at Startup (Windows only)

To enable this feature, it takes several simple steps:

1) Edit the auto.bat file:
    - Copy the path to your python.exe (usually C:\Python38\python.exe), this will vary depending on where python was installed.
	- Paste this path between the first set of quotes
	- Copy the path to the scraper.py file of this project
	- Paste it between the second set of quotes, then save and close the .bat file

2) Add the auto.bat file to Windows' Startup folder:
	- Here's a [tutorial](https://support.microsoft.com/en-us/help/4558286/windows-10-add-an-app-to-run-automatically-at-startup) on how to do this.
# Take-Aways
- SMTP: Before this project, I was unfamiliar with the Simple Mail Transfer Protocol and Python's smtplib library. They are simple and straightforward, contrary to my previous belief.
- Web Scraping: Widened my knowledge in HTTP requests and the use of HTML tags to collect data from websites.
- Task Automation: Learned how to automatically run a program on Windows using a batch file and the Windows Startup folder.
