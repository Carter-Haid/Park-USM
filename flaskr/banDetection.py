import requests
import imaplib
import os
import json
import email
import re
import datetime
from lxml.html import fromstring


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
    tag_re = re.compile(r'<[^>]+>')
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
                removetags = tag_re.sub('', email_data)
        my_message += removetags
    return my_message


if __name__ == "__main__":
    my_inbox = get_inbox()
    with open("/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/emailtext.txt", "w") as text_file:
        text_file.write(str(my_inbox))

name = '/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/emailtext.txt'

with open(name, 'r') as file:
    text = file.readlines()

index_prohibited = 0
index_available = 0
prohibited_lots = []
available_lots = []
day = []
time = []
for each in range(len(text)):
    pattern = re.compile(r'prohibited:')
    pattern2 = re.compile(r'following\slots:')
    pattern3 = re.compile(r',\s[A-Z][a-z]{2,10}\s[0-9]{1,2}(nd|rd|th)?')
    pattern4 = re.compile(r'[0-9]{2}(:[0-9]{0,2})?\s(am|pm)')
    matches = re.search(pattern, text[each])
    matches2 = re.search(pattern2, text[each])
    matches3 = re.search(pattern3, text[each])
    matches4 = re.search(pattern4, text[each])
    if matches:
        index_prohibited = each + 1
    elif matches2:
        index_available = each + 1
    if matches3:
        x = pattern3.finditer(text[each])
        for match in x:
            day.append(match.group(0).split(',')[1])
    if matches4:
        x = pattern4.finditer(text[each])
        for match in x:
            time.append(match.group(0))

for x in range(index_prohibited, index_available - 1):
    try:
        prohibited_lots.append((text[x].split()[0]))
    except:
        pass

for x in range(index_available, len(text)):
    try:
        available_lots.append((text[x].split()[0]))
    except:
        pass

residentiallots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Gorham/Residential Lots"
commuterlots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Gorham/Commuter Lots"
stafflots = "/home/carter/PycharmProjects/campusParkingMap/flaskr/Resources/GeoJSON/Gorham/Staff Lots"

prohibited_with_filename = [x + ".json5" for x in prohibited_lots]

if len(day) == 2 and len(time) >= 2:
    print(f"\n\nStarting : {day[0]} {time[0]}")
    print(f"Ending   : {day[1]} {time[1]}")
else:
    pass

for file in os.listdir(residentiallots):
    filename = os.fsdecode(file)
    if filename in prohibited_with_filename:
        with open(residentiallots + "/" + filename, 'r') as f:
            data = json.load(f)
            data['features'][0]['properties']['lot_status'] = "closed"

        with open(residentiallots + "/" + filename, 'w') as f:
            f.write(json.dumps(data))
    else:
        pass

for file in os.listdir(stafflots):
    filename = os.fsdecode(file)
    if filename in prohibited_with_filename:
        with open(stafflots + "/" + filename, 'r') as f:
            data = json.load(f)
            data['features'][0]['properties']['lot_status'] = "closed"

        with open(stafflots + "/" + filename, 'w') as f:
            f.write(json.dumps(data))
    else:
        pass

for file in os.listdir(commuterlots):
    filename = os.fsdecode(file)
    if filename in prohibited_with_filename:
        with open(commuterlots + "/" + filename, 'r') as f:
            data = json.load(f)
            data['features'][0]['properties']['lot_status'] = "closed"

        with open(commuterlots + "/" + filename, 'w') as f:
            f.write(json.dumps(data))
    else:
        pass

currenttime = str(datetime.datetime.now())
currenttimeobject = datetime.datetime.strptime(currenttime, '%Y-%m-%d %H:%M:%S.%f')
currentyear = str(datetime.datetime.now().strftime('%Y'))
prohibited_lots = ["g2a", "g4", "g16", "g17"]
time_list = ["10:00 pm ", "07:00 am"]
date = ["February 4", "February 5"]
endtime = date[1] + " " + time_list[1] + " " + currentyear
endtimeobject = datetime.datetime.strptime(endtime, '%B %d %I:%M %p %Y')

host = 'imap.gmail.com'
username = 'campusparkingproject@gmail.com'
password = 'Park2020!'

# Logic for when the parking ban is over...
if currenttimeobject > endtimeobject:
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    typ, data = mail.search(None, 'ALL')
    for num in data[0].split():
        mail.store(num, '+FLAGS', '\\Deleted')
    mail.expunge()
    mail.close()
    mail.logout()
    for file in os.listdir(residentiallots):
        filename = os.fsdecode(file)
        if filename in prohibited_with_filename:
            with open(residentiallots + "/" + filename, 'r') as f:
                data = json.load(f)
                data['features'][0]['properties']['lot_status'] = "open"

            with open(residentiallots + "/" + filename, 'w') as f:
                f.write(json.dumps(data))
        else:
            pass

    for file in os.listdir(stafflots):
        filename = os.fsdecode(file)
        if filename in prohibited_with_filename:
            with open(stafflots + "/" + filename, 'r') as f:
                data = json.load(f)
                data['features'][0]['properties']['lot_status'] = "open"

            with open(stafflots + "/" + filename, 'w') as f:
                f.write(json.dumps(data))
        else:
            pass

    for file in os.listdir(commuterlots):
        filename = os.fsdecode(file)
        if filename in prohibited_with_filename:
            with open(commuterlots + "/" + filename, 'r') as f:
                data = json.load(f)
                data['features'][0]['properties']['lot_status'] = "open"

            with open(commuterlots + "/" + filename, 'w') as f:
                f.write(json.dumps(data))
        else:
            pass
