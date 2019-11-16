import googlemaps
import UserData
import postcodes
import IndiceToPostcodeConverter
import Graph
'''
	class that deals with taking the list of postcodes produced from 'RoutePostcodeConverter' and producing a google maps url link.
	ALGORITHM:
		takes the first element of the postcodes List and applies it as the start location of the directions 
'''

'''
#NOTE - USEFUL FOR DIRECTIONS
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
'''
class GoogleRoutePlanner :

	def __init__(self) :
		aKey = 'AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE'
		#self.graph = Graph.Graph()
		#self.postcodes = postcodes.Postcodes()
		gmaps = googlemaps.Client(key = aKey)

	#function that turns the list of postcodes gathered from RoutePostcodeConverter to a list of addresses
	def postcodesAddressConverter(self,postcodes) :
		#for currentPostcode in postcodes :
		listofAddresses = []
		graph = Graph.Graph(postcodes)
		print(postcodes, listofAddresses)
		for currentPostcode in postcodes :
			newLatLong = graph.convertPostCoord(currentPostcode)
			print(newLatLong)
			listofAddresses.append(newLatLong)
		return 0


	#function that constructs the address of the google maps and returns it
	def googleMapsRouteURL(self,postcodes) :
		latlLongs = postcodesAddressConverter(postcodes)
		startingLatLong = atlLongs.pop()
		return startingLatLong

#Debug
routePlanner = GoogleRoutePlanner()
listofAddresses  = ["TN21 0TQ", "TN21 0TQ"]
print(routePlanner.postcodesAddressConverter(listofAddresses))
