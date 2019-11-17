import googlemaps
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


	#adds the origin and destination to the address
	def addOriginDestination(self,names, address):
		origin = names[0]
		origin = list(origin)
		origin = origin[0].split()
		lat_address = str(origin[0])
		long_address = str(origin[1])
		address = address + lat_address + "," + long_address + "&" + "destination=" + lat_address + "," + long_address + "&" + "travelmode=walking&waypoints="
		#address=""
		return address

	#adds waypoints to the address
	def addWaypoints(self,names,address) :
		#remove first and last elements (start and finish)
		names.pop()
		del names[0]

		for currentName in names :
			currentName = list(currentName)
			currentName = str(currentName)
			currentName = currentName.replace(" ", "+")
			currentName = currentName.replace("[", "")
			currentName = currentName.replace("]", "")
			address = address + "|" + currentName
		return address

	#function that will return the completed address with full route on Google
	""" 
	def createAddress(self, postcodes) :
		latitudes = postcodesAddressConverter(postcodes)
		startOfAddress = addOriginDestination(latitudes, "https://www.google.com/maps/dir/?api=1&origin=")
		return addWaypoints(latitudes,startOfAddress)
	"""

googleRoute = GoogleRoutePlanner() 
postcodes = [{"home"},{"The Bear Inn"},{"The Crown Inn"},{"The Mitre"},{"Clowns Wine Bar"},{"The Hobbit Inn"},{"Wild Lime"},{"The Shooting Star"},{"home"}]
#latitudes = googleRoute.postcodesAddressConverter(postcodes)
startOfAddress = googleRoute.addOriginDestination(postcodes, "https://www.google.com/maps/dir/?api=1&origin=")
print(googleRoute.addWaypoints(postcodes,startOfAddress))








