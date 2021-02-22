import imaplib
import email
import re
from lxml.html import fromstring
import requests


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    pogoweatherstatus = html.xpath(
        "//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return pogoweatherstatus


def lac_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    lacweatherstatus = html.xpath(
        "//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return lacweatherstatus


def gorham_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    gorhamweatherstatus = html.xpath(
        "//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return gorhamweatherstatus


def portland_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    portlandweatherstatus = html.xpath(
        "//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return portlandweatherstatus


def lewiston_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    lewistonweatherstatus = html.xpath(
        "//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return lewistonweatherstatus


host = 'imap.gmail.com'
username = 'campusparkingproject@gmail.com'
password = 'Park2020!'


def get_inbox():
    TAG_RE = re.compile(r'<[^>]+>')
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, '(FROM "email@blackboard.com")')
    my_message = ""
    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for part in email_message.walk():
            if part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data = html_body.decode()
                removetags = TAG_RE.sub('', email_data)
        my_message += removetags
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    with open("", "w") as text_file:
        text_file.write(str(my_inbox))
    print(my_inbox)
