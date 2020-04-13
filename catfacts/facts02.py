#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
## print the value associated with text"
    for catfact in r.json()["all"]:
        print(catfact.get("user").get("name"))  # the .get() method returns NONE if key not found
 #   for catfact in r.json()["user"]:
  #      print(catfact.get("name"))
main()