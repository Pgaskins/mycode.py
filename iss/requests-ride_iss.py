#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests
from flask import Flask
## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

app = Flask(__name__)

app@.route("/")

def main(name):
    """runtime code"""

    ## Call the webservice
    groundctrl = requests.get(MAJORTOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmetson = groundctrl.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    people = helmetson['people']
    print(people)

    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode("utf-8"))

    # display people in space
    print("People in space: " + str(helmetson["number"]))
    
    for astronaut in helmetson["people"]:
        print(astronaut["name"] + " on the " + astronaut["craft"])

if __name__ == "__main__":
    app.run(host+"0.0.0.0", port=2224)

