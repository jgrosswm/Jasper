import os
import re
import subprocess

WORDS = ["DIM"]

def handle(text, mic, profile):
    
#    fancheck = subprocess.check_output("sudo wemo switch 'fan' status", shell=True)
#    fancheck = fancheck.strip()
    mic.say("Let me dim the lights for you.")
    os.system("wemo light 'Lightbulb 03' on 45")
    os.system("wemo light 'Lightbulb 01' on 45")
    
#    if fancheck == "1":
#    	mic.say("I'll turn the fan off.")
#        os.system("sudo wemo switch 'Fan' off")
#    elif fancheck == "0":
#	mic.say("I'll turn the fan on.")
#        os.system("sudo wemo switch 'Fan' on")
 	


def isValid(text):
    return bool(re.search(r'\bdim\b', text, re.IGNORECASE))

