from banDetection import *
from GorhamMap import *
from PortlandMap import *

# Color of "Parking Lots Closed: #" for Gorham Campus
if gorhammap() > 0:
    gorbancolor = "red"
else:
    gorbancolor = "green"

# Color of "Parking Lots Closed: #" for Portland Campus
if portlandmap() > 0:
    porbancolor = "red"
else:
    porbancolor = "green"

# Gorham Campus
usmgorcolor = ""
usmgorhamicon = ""
usmgorhamiconcolor = ""
gorhamopen = ""

pogobaninfo = pogo_status("University of Southern Maine")
if not pogobaninfo:
    status = "Open"
    usmgorcolor += "green"
    pogobaninfo = "No Current Ban Info"
    if gorhammap() <= 0:
        usmgorhamicon += "check_circle_outline"
        usmgorhamiconcolor += "green"
    else:
        usmgorhamicon += "warning"
        usmgorhamiconcolor += "red"
else:
    status = "Closed"
    usmgorcolor += "red"
    usmgorhamicon += "warning"
    usmgorhamiconcolor += "red"
gorhamopen += status

# Portland Campus
usmporcolor = ""
usmportlandicon = ""
usmportlandiconcolor = ""
portlandopen = ""

pogobaninfo = pogo_status("University of Southern Maine")
if not pogobaninfo:
    status = "Open"
    usmporcolor += "green"
    pogobaninfo = "No Current Ban Info"
    if portlandmap() <= 0:
        usmportlandicon += "check_circle_outline"
        usmportlandiconcolor += "green"
    else:
        usmportlandicon += "warning"
        usmportlandiconcolor += "red"
else:
    status = "Closed"
    usmporcolor += "red"
    usmportlandicon += "warning"
    usmportlandiconcolor += "red"
portlandopen += status

# Lewiston Campus Info
usmlewcolor = ""
usmlewistonicon = ""
usmlewistoniconcolor = ""
lewistonopen = ""

lewbaninfo = lac_status("University of Southern Maine")
if not lewbaninfo:
    status = "Open"
    usmlewcolor += "green"
    usmlewistonicon += "check_circle_outline"
    usmlewistoniconcolor += "green"
    lewbaninfo = "No Current Ban Info"
else:
    status = "Closed"
    usmlewcolor += "red"
    usmlewistonicon += "warning"
    usmlewistoniconcolor += "red"
lewistonopen += status

# Everything for Gorham Street Parking Ban
gorhamstreeticon = ""
gorhamstreeticoncolor = ""
gorhamstreetstatus = ""
gorcolor = ""

gorhambaninfo = gorham_status("Gorham Parking Ban")
if not gorhambaninfo:
    status = "Not In Effect"
    gorcolor += "green"
    gorhamstreeticon += "check_circle_outline"
    gorhamstreeticoncolor += "green"
    gorhambaninfo = "No Current Ban Info"
else:
    status = "In Effect"
    gorcolor += "red"
    gorhamstreeticon += "warning"
    gorhamstreeticoncolor += "red"
gorhamstreetstatus += status

# Everything for Portland Street Parking Ban
portlandstreeticon = ""
portlandstreeticoncolor = ""
portlandstreetstatus = ""
porcolor = ""

portlandbaninfo = portland_status("Portland Parking Ban")
if not portlandbaninfo:
    status = "Not In Effect"
    porcolor += "green"
    portlandstreeticon += "check_circle_outline"
    portlandstreeticoncolor += "green"
    portlandbaninfo = "No Current Ban Info"
else:
    status = "In Effect"
    porcolor += "red"
    portlandstreeticon += "warning"
    portlandstreeticoncolor += "red"
portlandstreetstatus += status

# Everything for Lewiston Street Parking Ban
lewcolor = ""
lewistonstreeticon = ""
lewistonstreeticoncolor = ""
lewistonstreetstatus = ""

lewistonbaninfo = lewiston_status("Lewiston Parking Ban")
if not lewistonbaninfo:
    status = "Not in Effect"
    lewcolor = "green"
    lewistonstreeticon = "check_circle_outline"
    lewistonstreeticoncolor = "green"
    lewistonbaninfo = "No Current Ban Info"
else:
    status = "In Effect"
    lewcolor = "red"
    lewistonstreeticon = "warning"
    lewistonstreeticoncolor = "red"
lewistonstreetstatus = status
