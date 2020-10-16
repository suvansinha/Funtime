import webbrowser
import time
import random

while True:
    sites = random.choice(["google.com","github.com","youtube.com","pypi.org"])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5,20)
    time.sleep(seconds)