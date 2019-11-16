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

    jsondat = gp.getPlaces("bar", sys.argv[1], sys.argv[2])
    # jsondat = gp.getPlaces("bar", "51.7520220,-1.2577260", "50")
    # print (sys.argv[1])
    # print (jsondat)

    parseList = post.address(jsondat)
    print (parseList)
    graphUser = Graph.Graph(parseList)
    print(graphUser.getIncidence())



if __name__ == "__main__":    
    
    gp = GetPlaces.GetPlaces()
    post = postcodes.postcodes()
    main()
