from lxml.html import fromstring
import requests


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "USM Gorham Campus is Open"
else:
    status = "USM Gorham Campus is Closed"
print(status + str(baninfo))


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "USM Portland Campus is Open"
else:
    status = "USM Portland Campus is Closed"
print(status + str(baninfo))


def lac_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lac_status("University of Southern Maine, L-A")
if not baninfo:
    status = "USM Lewiston Campus is Open"
else:
    status = "USM Lewiston Campus is Closed"
print(status + str(baninfo))


def gorham_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = gorham_status("Gorham Parking Ban")
if not baninfo:
    status = "No Gorham Parking Ban In Effect"
else:
    status = "Gorham Parking Ban In Effect"
print(status + str(baninfo))


def portland_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = portland_status("Portland Parking Ban")
if not baninfo:
    status = "No Portland Parking Ban In Effect"
else:
    status = "Portland Parking Ban In Effect"
print(status + str(baninfo))


def lewiston_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lewiston_status("Lewiston Parking Ban")
if not baninfo:
    status = "No Lewiston Parking Ban In Effect"
else:
    status = "Lewiston Parking Ban In Effect"
print(status + str(baninfo))

