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
    print (jsondat)

    postCodeList, nameList = post.address(jsondat)
    print (postCodeList)
    # print (post.convertCoordToPost([51.7521952, -1.2582522]))

    graphUser = Graph.Graph(postCodeList, nameList)
    incidenceGraph = graphUser.getIncidence()
    nameDict = graphUser.getNameDict()

    print(incidenceGraph)
    ts = TravellingSalesman.TravellingSalesman()
    
    # grp = GoogleRoutePlanner.GoogleRoutePlanner()
    # grp.createAddress()



if __name__ == "__main__":    
    
    gp = GetPlaces.GetPlaces()
    post = postcodes.postcodes()
    main()
