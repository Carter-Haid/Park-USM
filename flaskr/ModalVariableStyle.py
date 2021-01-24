from flaskr.GorhamMap import gorhammap
from flaskr.PortlandMap import portlandmap
from streetBanDetection import *

# Determining what color the number of banned lots should be:
if gorhammap() > 0:
    gorbancolor = "red"
else:
    gorbancolor = "green"

    if portlandmap() > 0:
        porbancolor = "red"
    else:
        portbancolor = "green"