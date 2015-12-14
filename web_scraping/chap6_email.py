__author__ = 'charlesw'


import smtplib
import requests
import requests.packages.urllib3.util.ssl_

from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib import urlopen
import time

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "christmas_alerts@pythonscraping.com"
    msg['To'] = "charles.wu@melbourneit.com.au"
    s = smtplib.SMTP('smtp.mit')
   #python 3
   #  s.send_message(msg)
    s.sendmail("christmas_alerts@pythonscraping.com","charles.wu@melbourneit.com.au",msg.as_string())
    s.quit()




sendMail("It's Christmas!","According xxx, it is Christmas!")