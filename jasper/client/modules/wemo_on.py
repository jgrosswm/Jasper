import os
import re
import subprocess

#WORDS = ["FAN", "ON"]

def handle(text, mic, profile):
    
    fancheck = subprocess.check_output("sudo wemo switch 'fan' status", shell=True)
    fancheck = fancheck.strip()
    
    if fancheck == "1":
    	mic.say("The fan is already on.")
    elif fancheck == "0":
	os.system("sudo wemo switch 'Fan' on")
 	mic.say("I've turned the Fan on.")


def isValid(text):
    return bool(re.search(r'\bfan on\b', text, re.IGNORECASE))

