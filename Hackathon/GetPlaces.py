import urllib.request, json 

class GetPlaces:

    def __init__(self):
        print ("init")

    def getPlaces(self, inquiryString, startLocation, radius): # pubs or what, latlng of user, radius, 
        # fix inquiry string
        # inquiryString = str(inquiryString).replace(" ", "%20")#+ "&inputtype=textquery"
        inputPart = "type=" + inquiryString+ "&"
        fieldsPart = "fields=formatted_address"+ "&"
        startLocation = "location="+ startLocation + "&"
        radius = "radius="+radius+ "&"# in meters
        params = "fields=formatted_address&"
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?" + startLocation+ inputPart + fieldsPart +radius +params+"key=AIzaSyDXKLWHJQdqzVI1agSREbzr4AuoBKyUeuE"    

        print (url)
        # with urllib.request.urlopen(urlToRead) as url:
        #     data = json.loads(url.read().decode())
        #     print(data)
        response = urllib.request.urlopen(url)

        data = json.loads(response.read())
        # print (data)
        # print (data['formatted_address'])
        return (data)



# print(GetPlaces.getPlaces("bar", "51.7520220,-1.2577260", "50")

