import os
import re
import subprocess

WORDS = ["FAN"]

def handle(text, mic, profile):
    
    fancheck = subprocess.check_output("sudo wemo switch 'fan' status", shell=True)
    fancheck = fancheck.strip()
    
    if fancheck == "1":
    	mic.say("I'll turn the fan off.")
        os.system("sudo wemo switch 'Fan' off")
    elif fancheck == "0":
	mic.say("I'll turn the fan on.")
        os.system("sudo wemo switch 'Fan' on")
 	


def isValid(text):
    return bool(re.search(r'\bfan\b', text, re.IGNORECASE))

