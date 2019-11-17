'''
set of functions that allows us to take Google maps addresses and distances and
form a graph that we can easily apply a SPT Algorithm to

Created on Sat Nov 16 12:54:10 2019

@author: lUkA-kOVaCeVIc (weird flex but okay)
'''
import numpy as np
import googlemaps
import postcodes

class Graph:

    #for a given list of postcodes, creates the incidence matrix for the distances between them
    def __init__(self, postcodeList, nameList):
        self.key = 'AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE'

        self.nameList = nameList

        self.setDestList(postcodeList, nameList)

        self.setDistanceDict(self.getDestList, self.key)

        self.setIncidence(self.getDistanceDict, self.getNameDict)

    def setIncidence(self, distanceDict, nameDict):
        n = len(self.distanceDict['rows'])
        self.incidence = np.eye(n)

        self.nameDict = dict()

        for x in range(0, n):
            elem = self.distanceDict['rows'][x]
            for y in range(0, len(elem['elements'])):
                self.incidence[x][y] = elem['elements'][y]['distance']['value']
                if x == y and elem['elements'][y]['distance']['value'] == 0:
                    self.nameDict[nameList[x]] = x

    def getIncidence(self):
        return self.incidence

    def setDestList(self, postcodeList, nameList):

        if len(postcodeList[0]) > 1:
            for x in range(0, len(postcodeList)):
                postcodeList[x] = postcodes.postcodes.convertCoordToPost(coord = postcodeList[x])

        dest = postcodeList[0].split(' ')
        destList = dest[0]+'+'+dest[1]

        for x in range(1, len(postcodeList)):
            dest = postcodeList[x].split(' ')
            destPostcode = dest[0]+'+'+dest[1]
            destList = destList+'|'+destPostcode

        self.destinations = destList

    def getDestList(self):
        return self.destinations

    def setDistanceDict(self, destList):
        gmaps = googlemaps.Client(key = self.key)
        self.distanceDict = gmaps.distance_matrix(origins = destList , destinations = destList, mode = 'walking')

    def getDistanceDict(self):
        return self.distanceDict

    def getNameDict(self):
        return self.nameDict
