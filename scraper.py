import requests as rq
from bs4 import BeautifulSoup
import smtplib

# Edit these values accordingly.
sender = 'sender@email.com'
password = 'yourPassword'
recepient = 'recepient@email.com' # make equal to sender to send yourself the email notification.
max_price = 800

# This url links to the item we want to track
URL = "https://www.lenovo.com/us/en/laptops/thinkpad/thinkpad-x/X1-Carbon-Gen-7/p/22TP2TXX17G"

#Prepare headers
headers ={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
        
    page = rq.get(URL, headers= headers)
    #print(page.status_code)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    #We can go and "inspect" the product's page and look for data items we need. I only need the title and price
    title = soup.find(itemprop="name").get_text()
    price = soup.find(itemprop="price").get_text()

    price_length = len(price)
    price = price[1:price_length] #Starts at 1 because the 0th character is '$'

    #the replace method basically deletes the comma from the price allowing the conversion to take place (str-->float)
    converted_price = float(price.replace(',',''))
    print(converted_price)

    if (converted_price < max_price):
        send_mail(converted_price)
    else:
        print("Price condition hasn't been met. Email not sent!")

    
def send_mail(price):
    server = smtplib.SMTP('smtp.office365.com', 587) # I used my outlook account, this will vary depending on what email service we use.
    server.ehlo()
    server.starttls()
    server.ehlo()
    try:
        server.login(sender,password) # sender email credentials
    except:
        print("EMAIL NOT SENT: Please double check your credentials.")
        server.quit()
        return

    subject = "Amazon Price Notification"
    body = "Hello, I am your price-tracking bot,\n\nThe Price of your tracked item has changed. Here is the link:\n https://www.amazon.com/gp/product/B07VLXMNYV?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=1AHFA1GCFN1EGN18K963"
    body += "$"+str(price)
    msg = f"{subject}\n{body}"
    
    try:
        server.sendmail(sender, recepient, msg)
        print("Email successfully sent!")
    except :
        print("EMAIL NOT SENT: Invalid sender or recipient address.")

    server.quit()

check_price()

'''

To know more about SMTP setting go to:
https://support.office.com/en-us/article/pop-and-imap-email-settings-for-outlook-8361e398-8af4-4e97-b147-6c6c4ac95353

'''