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
	def postcodesAddressConverter(self.postcodes,namesList) :
		#for currentPostcode in postcodes :
		listofAddresses = []
		graph = Graph.Graph(postcodes,namesList)
		for currentPostcode in postcodes :
			newLatLong = graph.convertPostToCoord(currentPostcode)
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
	""" 
	def createAddress(self, postcodes) :
		latitudes = postcodesAddressConverter(postcodes)
		startOfAddress = addOriginDestination(latitudes, "https://www.google.com/maps/dir/?api=1&origin=")
		return addWaypoints(latitudes,startOfAddress)
	"""

googleRoute = GoogleRoutePlanner() 
postcodes = ["TN21 0TQ","RG1 6PF","RM11 2EH","S017 1AW","SO16 4UF","SO18 2NU","SO17 3RE","HS7 5PG","GL5 1JY","L22 7RA","OX14 5JZ","RG19 8BT","TN32 5BP"]
latitudes = googleRoute.postcodesAddressConverter(postcodes)
startOfAddress = googleRoute.addOriginDestination(latitudes, "https://www.google.com/maps/dir/?api=1&origin=")
print(googleRoute.ddWaypoints(latitudes,startOfAddress))








