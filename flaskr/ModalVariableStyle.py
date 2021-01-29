from streetBanDetection import *


# Color of "Parking Lots Closed: #" for Gorham Campus
def gorbancolorfunction():
    if gorhammap() > 0:
        gorbancolor = "red"
    else:
        gorbancolor = "green"
    return gorbancolor


# Color of "Parking Lots Closed: #" for Portland Campus
def porbancolorfunction():
    if portlandmap() > 0:
        porbancolor = "red"
    else:
        porbancolor = "green"
    return porbancolor


# Gorham Campus
def gorhamcampus():
    baninfo = pogo_status("University of Southern Maine")
    if not baninfo:
        status = "Open"
        usmgorcolor = "green"
        if gorhammap() <= 0:
            usmgorhamicon = "check_circle_outline"
            usmgorhamiconcolor = "green"
        else:
            usmgorhamicon = "warning"
            usmgorhamiconcolor = "red"
    else:
        status = "Closed"
        usmgorcolor = "red"
        usmgorhamicon = "warning"
        usmgorhamiconcolor = "green"
    gorhamopen = status
    return usmgorcolor, usmgorhamicon, usmgorhamiconcolor, gorhamopen


# Portland Campus
def portlandcampus():
    baninfo = pogo_status("University of Southern Maine")
    if not baninfo:
        status = "Open"
        usmporcolor = "green"
        if portlandmap() <= 0:
            usmportlandicon = "check_circle_outline"
            usmportlandiconcolor = "green"
        else:
            usmportlandicon = "warning"
            usmportlandiconcolor = "red"
    else:
        status = "Closed"
        usmporcolor = "red"
        usmportlandicon = "warning"
        usmportlandiconcolor = "red"
    portlandopen = status
    return usmporcolor, usmportlandicon, usmportlandiconcolor, portlandopen


# Lewiston Campus Info
def lewistoncampus():
    baninfo = lac_status("University of Southern Maine, L-A")
    if not baninfo:
        status = "Open"
        usmlewcolor = "green"
        usmlewistonicon = "check_circle_outline"
        usmlewistoniconcolor = "green"
    else:
        status = "Closed"
        usmlewcolor = "red"
        usmlewistonicon = "warning"
        usmlewistoniconcolor = "red"
    lewistonopen = status
    return usmlewcolor, usmlewistonicon, usmlewistoniconcolor, lewistonopen


# Everything for Gorham Street Parking Ban
def gorstreetbancolor():
    baninfo = gorham_status("Gorham Parking Ban")
    if not baninfo:
        status = "Not In Effect"
        gorcolor = "green"
        gorhamstreeticon = "check_circle_outline"
        gorhamstreeticoncolor = "green"
    else:
        status = "In Effect"
        gorcolor = "red"
        gorhamstreeticon = "warning"
        gorhamstreeticoncolor = "red"
    gorhamstreetstatus = status
    return gorhamstreeticon, gorhamstreeticoncolor, gorhamstreetstatus, gorcolor


# Everything for Portland Street Parking Ban
def porstreetbancolor():
    baninfo = portland_status("Portland Parking Ban")
    if not baninfo:
        status = "Not In Effect"
        porcolor = "green"
        portlandstreeticon = "check_circle_outline"
        portlandstreeticoncolor = "green"
    else:
        status = "In Effect"
        porcolor = "red"
        portlandstreeticon = "warning"
        portlandstreeticoncolor = "green"
    portlandstreetstatus = status
    return portlandstreeticon, portlandstreeticoncolor, portlandstreetstatus, porcolor


# Everything for Lewiston Street Parking Ban
def lewstreetbancolor():
    baninfo = lewiston_status("Lewiston Parking Ban")
    if not baninfo:
        status = "Not in Effect"
        lewcolor = "green"
        lewistonstreeticon = "check_circle_outline"
        lewistonstreeticoncolor = "green"
    else:
        status = "In Effect"
        lewcolor = "red"
        lewistonstreeticon = "warning"
        lewistonstreeticoncolor = "red"
    lewistonstreetstatus = status
    return lewcolor, lewistonstreeticon, lewistonstreeticoncolor, lewistonstreetstatus
