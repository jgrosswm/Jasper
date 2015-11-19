import os
import re
import subprocess

#WORDS = ["FAN", "OFF"]

def handle(text, mic, profile):
    
    fancheck = subprocess.check_output("sudo wemo switch 'fan' status", shell=True)
    fancheck = fancheck.strip()
    
    if fancheck == "0":
    	mic.say("The fan is already off.")
    elif fancheck == "1":
	os.system("sudo wemo switch 'Fan' off")
 	mic.say("I've turned the Fan off.")


def isValid(text):
    return bool(re.search(r'\bfan off\b', text, re.IGNORECASE))

