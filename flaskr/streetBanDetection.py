from flaskr.GorhamMap import gorhammap
from lxml.html import fromstring
import requests


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "Open"
else:
    status = "Closed"
gorhamopen = status


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "Open"
else:
    status = "Closed"
portlandopen = status


def lac_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lac_status("University of Southern Maine, L-A")
if not baninfo:
    status = "Open"
else:
    status = "Closed"
lewistonopen = status


def gorham_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = gorham_status("Gorham Parking Ban")
if not baninfo:
    status = "Not In Effect"
else:
    status = "In Effect"
gorhamstreetstatus = status


def portland_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = portland_status("Portland Parking Ban")
if not baninfo:
    status = "Not In Effect"
else:
    status = "In Effect"
portlandstreetstatus = status


def lewiston_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lewiston_status("Lewiston Parking Ban")
if not baninfo:
    status = "Not In Effect"
else:
    status = "In Effect"
lewistonstreetstatus = status
