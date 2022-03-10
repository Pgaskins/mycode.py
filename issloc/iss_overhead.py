#!/usr/bin/python3
"""Alta3 Research | <your name here>
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests

#URL = "http://api.open-notify.org/iss-pass.json?lat=47.6&lon=-122.3 "
latinput = input("What is you lat:?")
loninput = input("What is your lon:?")
URLIN = "http://api.open-notify.org/iss-pass.json?lat={latinput}&lon=-{loninput}"

def main():
    
    issresp = requests.get(URLIN)

    ## Decode the response
    iss_data = issresp.json()

    ## loop across response
    for lat_lon in iss_dat:
        
        print(f'{lat_lon}')
    
    issresp = requests.get(iss_data)
    

if __name__ == "__main__":
    main()

