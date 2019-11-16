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
	def PostcodesAddressesConverter(postcodes) :
		#for currentPostcode in postcodes :
		listofAddresses = []
		graph = Graph.Graph(postcodes)
		for currentPostcode in postcodes :
			newLatLong = graph.convertPostCoord(currentPostcode)
			listofAddresses.append(newLatLong)
		return listofAddresses


	#function that constructs the address of the google maps and returns it
	def googleMapsRouteURL() :
		#startingList = "http://maps.google.com/dir/?api=1"
		listofAddresses = PostcodesAddressesConverter(postcodes)
		startPoint = listofAddresses.pop()
		destination = listofAddresses.
		modeOfTravel = "travelmodewalking"
		#return graph.convertPostCoord(startingDestination)

		#might not need list of routes 
		#gmaps.directions(startingDestination, "walking", listofAddresses, units="metric", transit_routing_preference="less_walking")

googleRoute = GoogleRoutePlanner()
listofAddresses = ['TN21 0TQ','TN21 9NS','TN21 7YQ', 'TN21 5TY']
googleRoute.googleMapsRouteURL(listofAddresses)