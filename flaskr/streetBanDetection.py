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
    usmgorhamtextcolor = "green"
    usmgorhamicon = "check_circle_outline"
else:
    status = "Closed"
    usmgorhamtextcolor = "red"
    usmgorhamicon = "warning"
gorhamopen = status


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "Open"
    usmportlandtextcolor = "green"
    usmportlandicon = "check_circle_outline"
else:
    status = "Closed"
    usmportlandtextcolor = "red"
    usmportlandicon = "warning"
portlandopen = status


def lac_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lac_status("University of Southern Maine, L-A")
if not baninfo:
    status = "Open"
    usmlewistontextcolor = "green"
    usmlewistonicon = "check_circle_outline"
else:
    status = "Closed"
    usmlewistontextcolor = "red"
    usmlewistonicon = "warning"
lewistonopen = status


def gorham_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = gorham_status("Gorham Parking Ban")
if not baninfo:
    status = "Not In Effect"
    gorhamtextcolor = "green"
    gorhamicon = "check_circle_outline"
else:
    status = "In Effect"
    gorhamtextcolor = "red"
    gorhamicon = "warning"
gorhamstreetstatus = status


def portland_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = portland_status("Portland Parking Ban")
if not baninfo:
    status = "Not In Effect"
    portlandtextcolor = "green"
    portlandicon = "check_circle_outline"
else:
    status = "In Effect"
    portlandtextcolor = "red"
    portlandicon = "warning"
portlandstreetstatus = status


def lewiston_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lewiston_status("Lewiston Parking Ban")
if not baninfo:
    status = "Not In Effect"
    lewistontextcolor = "green"
    lewistonicon = "check_circle_outline"
else:
    status = "In Effect"
    lewistontextcolor = "red"
    lewistonicon = "warning"
lewistonstreetstatus = status
