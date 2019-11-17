import sys
import GetPlaces
# import GoogleRoutePlanner
import IndiceToPostcodeConverter
import Graph
import postcodes
import TravellingSalesman
import json


def main():
    postcodeInput= sys.argv[1]
    latlong = post.convertPostToCoord(postcodeInput)
    print(latlong)
    latlongString = str(latlong[0])+","+str(latlong[1])
    jsondat = gp.getPlaces("bar", latlongString, sys.argv[2])
    # jsondat = gp.getPlaces("bar", "51.7520220,-1.2577260", "50")
    # print (sys.argv[1])
    # print (jsondat)

    postCodeList, nameList = post.address(jsondat)
    latlongSet = {float(latlongString.split(',')[0]),float(latlongString.split(',')[1])}
    postCodeList = [latlongSet] + postCodeList
    nameList = ["home"]+ nameList
    # print (postCodeList)
    # print (post.convertCoordToPost([51.7521952, -1.2582522]))

    graphUser = Graph.Graph(postCodeList, nameList)
    incidenceGraph = graphUser.getIncidence()
    nameDict = graphUser.getNameDict()

    print(incidenceGraph)
    directedIndices  = TravellingSalesman.travellingSalesmanAlgorithm(graphUser)
    print(directedIndices)
    pubsInOrder = []
    for x in directedIndices.replace(" ", "").split(","):
        # print(x)
        # print (nameDict[int(x)])
        pubsInOrder.append(nameDict[int(x)])


    pubsInOrder[0]= latlong
    pubsInOrder[-1]=latlong
    print(pubsInOrder)

    
    # grp.createAddress()



if __name__ == "__main__":    
    
    gp = GetPlaces.GetPlaces()
    post = postcodes.postcodes()
    main()
