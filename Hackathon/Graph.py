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

        if len(nameList) > 10:
            postcodeList = postcodeList[:10]
            nameList = nameList[:10]

        self.key = 'AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE'
        self.nameList = nameList
        self.postcodeList = postcodeList

        print(postcodeList)

        self.setDestList(postcodeList, nameList)
        self.setDistanceDict(self.getDestList())
        self.setIncidence(self.getDistanceDict(), self.nameList)

    def setIncidence(self, distanceDict, nameList):
        n = len(self.distanceDict['rows'])
        self.incidence = np.eye(n)

        self.nameDict = dict()

        for x in range(0, n):
            elem = self.getDistanceDict()['rows'][x]
            for y in range(0, len(elem['elements'])):
                self.incidence[x][y] = elem['elements'][y]['distance']['value']
                if x == y and elem['elements'][y]['distance']['value'] == 0:
                    self.nameDict[x] = nameList[x] + ',' + str(self.postcodeList[x])
                    
    def getIncidence(self):
        return self.incidence

    def setDestList(self, postcodeList, nameList):

        #determines if postcode or coordinates
        if type(postcodeList[0]) == type(set()):

            destList = str(list(postcodeList[0])[0])+', '+str(list(postcodeList[0])[1])

            for x in range(1, len(postcodeList)):
                destList = destList+'|'+str(list(postcodeList[x])[0])+', '+str(list(postcodeList[x])[1])

        else:

            #dest = postcodeList[0].split(' ')
            #destList = dest[0]+'+'+dest[1]

            destList = postcodeList[0].replace(' ','')

            for x in range(1, len(postcodeList)):
                #dest = postcodeList[x].split(' ')
                #destPostcode = dest[0]+'+'+dest[1]

                destPostcode = postcodeList[x].replace(' ','')
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
