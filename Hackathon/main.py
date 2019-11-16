import sys
import GetPlaces
# import GoogleRoutePlanner
import IndiceToPostcodeConverter
import Graph
import postcodes
import TravellingSalesman
import UserData
import json


def main():
    # jsondat = GetPlaces.getPlaces(sys.argv[0], sys.argv[1], sys.argv[2])

    jsondat = gp.getPlaces("bar", "51.7520220,-1.2577260", "50")
    print (jsondat)

if __name__ == "__main__":    
    gp = GetPlaces.GetPlaces()
    main()
