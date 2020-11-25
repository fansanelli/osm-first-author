#!/usr/bin/env python

###########################################################################
##                                                                       ##
## Copyrights Francesco Ansanelli 2020                                   ##
##                                                                       ##
## This program is free software: you can redistribute it and/or modify  ##
## it under the terms of the GNU General Public License as published by  ##
## the Free Software Foundation, either version 3 of the License, or     ##
## (at your option) any later version.                                   ##
##                                                                       ##
## This program is distributed in the hope that it will be useful,       ##
## but WITHOUT ANY WARRANTY; without even the implied warranty of        ##
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ##
## GNU General Public License for more details.                          ##
##                                                                       ##
## You should have received a copy of the GNU General Public License     ##
## along with this program.  If not, see <http://www.gnu.org/licenses/>. ##
##                                                                       ##
###########################################################################


import json
import urllib.request

def main():
  authors = {}
  user_in = input("Oggetti da ricercare (Es. r12345 n6543): ").split()
  for value in user_in:
    if value.startswith("r"):
      request = value.replace("r", "/relation/")
    elif value.startswith("n"):
      request = value.replace("n", "/node/")
    elif value.startswith("w"):
      request = value.replace("w", "/way/")
    else:
      print(value + " sconosciuto")
      continue
    
    response = urllib.request.urlopen("https://api.openstreetmap.org/api/0.6" + request + "/1.json")
    json_response = json.loads(response.read())
    author = json_response["elements"][0]["user"]    
    print(author + " ha creato " + value)

if __name__ == "__main__":
    main()

