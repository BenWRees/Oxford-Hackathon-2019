import googlemaps
import UserData
import postcodes
import IndiceToPostcodeConverter
import Graph
'''
	class that deals with taking the list of postcodes produced from 'RoutePostcodeConverter' and producing a google maps url link.
'''

class GoogleRoutePlanner :
	def __init__(self) :
		aKey = 'AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE'
		#self.graph = Graph.Grapyu
		#self.postcodes = postcodes.Postcodes()
		gmaps = googlemaps.Client(key = aKey)

	#function that turns the list of postcodes gathered from RoutePostcodeConverter to a list of addresses
	def postcodesAddressConverter(self,postcodes) :
		#for currentPostcode in postcodes :
		listofAddresses = []
		graph = Graph.Graph(postcodes)
		for currentPostcode in postcodes :
			newLatLong = graph.convertPostCoord(currentPostcode)
			listofAddresses.append(newLatLong)
		return listofAddresses

	#adds the origin and destination to the address
	def addOriginDestination(self,latitudes,address):
		latLong = latitudes[0]
		latString = str(latLong[0])
		longString = str(latLong[1])
		address = address +latString + "," + longString + "&" + "destination=" +latString + "," + longString + "&" + "travelmode=walking&waypoints="
		return address

	#adds waypoints to the address
	def addWaypoints(self,latitudes,address) :
		#remove first and last elements (start and finish)
		latitudes.pop()
		del latitudes[0]

		for currentLatitude in latitudes :
			latString = str(currentLatitude[0])
			longString = str(currentLatitude[1])
			address = address + "|" + latString + "," + longString
		return address

	#function that will return the completed address with full route on Google 
	def createAddress(self, postcodes) :
		latitudes = routePlanner.postcodesAddressConverter(postcodes)
		startOfAddress = routePlanner.addOriginDestination(latitudes, "https://www.google.com/maps/dir/?api=1&origin=")
		return routePlanner.addWaypoints(latitudes,startOfAddress)


routePlanner = GoogleRoutePlanner()
addresses = ["TN21 0TQ", "SO17 1AW", "RM11 2EH", "GL2 9DW", "TN21 0TQ"]
print(routePlanner.createAddress(addresses))





