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
        actual_Postcodes = self.populateActualPostcodeList(self.postcodeList)

        
        #this is the incidence array being set 
        self.incidence = np.eye(n)


        self.nameDict = dict()

        #loops through the row index's 
        for x in range(n):
            elem = self.getDistanceDict()['rows'][x]

            #loops through the elemetns on row x
            for y in range(len(elem['elements'])):

                self.incidence[x][y] = elem['elements'][y]['distance']['value']

                #if element (a)xy is on the diagonal and the diagonal elements value is 0
                #if x == y and elem['elements'][y]['distance']['value'] == 0 :
                    
                    #assign value on row x as the pair (name of indice, postcode of indice)
            self.nameDict[x] = zip(nameList[x],actual_Postcodes[x])

    """
        function that takes a list of malformed 'postcodes', that are really a list of lat-longs
        and turns them into a list of postcodes
    """
    def populateActualPostcodeList(non_actual_postcodes) :
        postcodes = postcodes.postcodes()
        actual_Postcodes = list()
        for x in non_actual_postcodes :
            new_Real_Postcode = postcodes.convertCoordToPost(x)
            actual_Postcodes.append(new_Real_Postcode)

        return actual_Postcodes 



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
