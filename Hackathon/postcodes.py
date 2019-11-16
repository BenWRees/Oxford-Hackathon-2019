

#jdata = getPlaces("bar", "51.7520220,-1.2577260", "100")
from geopy.geocoders import Nominatim

class postcodes:

    def __init__(self):
        super().__init__()

    # a method which takes in a json object and searches through it to output the latitude and longitude of the location
    def address(self, json_object):

        l = []

        if json_object == None:
            return None
        else:
            for x in json_object['results']:
                l.append({x['geometry']['location']['lat'],x['geometry']['location']['lng']})
        return l

    #takes postcode as argument, returns coordinates
    def convertPostToCoord(self, postcode):
        geolocator = Nominatim(user_agent='postcodeConverter')
        location = geolocator.geocode(postcode)
        return location.latitude, location.longitude

    def convertCoordToPost(self, coord):
        geolocator = Nominatim(user_agent="coordConverter")
        location = geolocator.reverse(coord[0], coord[1])
        return location

# address(jdata)
