import sys
import GetPlaces
# import GoogleRoutePlanner
import IndiceToPostcodeConverter
import Graph
import postcodes
import TravellingSalesman
import json


def main():
    latlong = sys.argv[1]
    jsondat = gp.getPlaces("bar", latlong, sys.argv[2])
    # jsondat = gp.getPlaces("bar", "51.7520220,-1.2577260", "50")
    # print (sys.argv[1])
    # print (jsondat)

    postCodeList, nameList = post.address(jsondat)
    latlong = {float(latlong.split(',')[0]),float(latlong.split(',')[1])}
    postCodeList = [latlong] + postCodeList
    nameList = ["home"]+ nameList
    # print (postCodeList)
    # print (post.convertCoordToPost([51.7521952, -1.2582522]))

    graphUser = Graph.Graph(postCodeList, nameList)
    incidenceGraph = graphUser.getIncidence()
    nameDict = graphUser.getNameDict()

    print(incidenceGraph)
    hopefullySomething  = TravellingSalesman.travellingSalesmanAlgorithm(graphUser)
    print(hopefullySomething)
    
    # grp = GoogleRoutePlanner.GoogleRoutePlanner()
    # grp.createAddress()



if __name__ == "__main__":    
    
    gp = GetPlaces.GetPlaces()
    post = postcodes.postcodes()
    main()
