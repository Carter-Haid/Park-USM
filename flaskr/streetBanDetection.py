from flaskr.GorhamMap import gorhammap
from flaskr.PortlandMap import portlandmap
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
    usmgorcolor = "green"
    if gorhammap() > 0:
        usmgorhamicon = "check_circle_outline"
        usmgorhamiconcolor = "green"
else:
    status = "Closed"
    usmgorcolor = "red"
    usmgorhamicon = "warning"
    usmgorhamiconcolor = "green"
gorhamopen = status


def pogo_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = pogo_status("University of Southern Maine")
if not baninfo:
    status = "Open"
    usmportcolor = "green"
    if portlandmap() > 0:
        usmportlandicon = "circle_check_outline"
        usmportlandiconcolor = "green"
else:
    status = "Closed"
    usmporcolor = "red"
    usmportlandicon = "warning"
    usmportlandiconcolor = "red"
portlandopen = status


def lac_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lac_status("University of Southern Maine, L-A")
if not baninfo:
    status = "Open"
    usmlewcolor = "green"
    usmlewistonicon = "circle_check_outline"
    usmlewistoniconcolor = "green"
else:
    status = "Closed"
    usmlewcolor = "red"
    usmlewistonicon = "warning"
    usmlewistoniconcolor = "red"
lewistonopen = status


def gorham_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = gorham_status("Gorham Parking Ban")
if not baninfo:
    status = "Not In Effect"
    gorcolor = "green"
    gorhamstreeticon = "circle_check_outline"
    gorhamstreeticoncolor = "green"
else:
    status = "In Effect"
    gorcolor = "red"
    gorhamstreeticon = "warning"
    gorhamstreeticoncolor = "red"
gorhamstreetstatus = status


def portland_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = portland_status("Portland Parking Ban")
if not baninfo:
    status = "Not In Effect"
    portcolor = "green"
    portlandstreeticon = "circle_check_outline"
    portlandstreeticoncolor = "green"
else:
    status = "In Effect"
    porcolor = "red"
    portlandstreeticon = "warning"
    portlandstreeticoncolor = "green"
portlandstreetstatus = status


def lewiston_status(location):
    res = requests.get("https://www.wmtw.com/weather/closings", headers={'user-agent': 'Mozilla 5.0'})
    html = fromstring(res.text)
    weatherstatus = html.xpath("//*[contains(text(),'{}')]/following-sibling::div[contains(@class,'status')]/ul/li/text()".format(location))
    return weatherstatus


baninfo = lewiston_status("Lewiston Parking Ban")
if not baninfo:
    status = "Not In Effect"
    lewcolor = "green"
    lewistonstreeticon = "circle_check_outline"
    lewistonstreeticoncolor = "green"
else:
    status = "In Effect"
    lewcolor = "red"
    lewistonstreeticon = "warning"
    lewistonstreeticoncolor = "red"
lewistonstreetstatus = status
