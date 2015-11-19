import re
import wikipedia

# Written by Naoto Ida 

WORDS = ["WIKI", "WIKIPEDIA"]

PRIORITY = 1

def handle(text, mic, profile):

       	mic.say("Okay, what would you like me to look up?")

        def sayDefinition(text):
            mic.say(wikipedia.summary(text, sentences=2))

        sayDefinition(mic.activeListen())


def isValid(text):
        return bool(re.search(r'\bwiki|wikipedia\b', text, re.IGNORECASE))
