import requests
from bs4 import BeautifulSoup
import smtplib


def check_price():
    url='https://www.amazon.in/dp/B07HGMR1X1?pf_rd_p=74e1f885-2d10-496c-bdfd-93578cd2be03&pf_rd_r=VC5HWPFHB0GWFZD1Y6JN'
    header={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"}
    result=requests.get(url,headers=header)
    soup=BeautifulSoup(result.content,'html.parser')
    # print(soup.prettify())
    name=soup.find(id='productTitle').get_text()
    # print(name)
    print(name.strip())
    price=soup.find(id='priceblock_ourprice').get_text()
    price=float(price[2:4]+price[5:8])
    print(price)
    if price <= 11999.0:
        send_mail()
    elif price >=11999.0:
        send_mail()

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('gelotdashrath001@gmail.com','uakprhbcwikdlpwi')

    subject='price fell down'
    body='check link now https://www.amazon.in/dp/B07HGMR1X1?pf_rd_p=74e1f885-2d10-496c-bdfd-93578cd2be03&pf_rd_r=VC5HWPFHB0GWFZD1Y6JN'

    msg=f'subject {subject} body {body}'

    server.sendmail('gelotdashrath001@gmail.com','gelotdashrath9731@gmail.com',msg)
    print("email has been sent")
    server.quit()

check_price()
