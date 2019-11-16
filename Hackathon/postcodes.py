

#jdata = getPlaces("bar", "51.7520220,-1.2577260", "100")

class postcodes:  

    # a method which takes in a json object and searches through it to output the latitude and longitude of the location
    def address(json_object):
        
        l = [] 
        
        if json_object == None:
            return None
        else:
            for x in json_object['results']:
                l.append({x['geometry']['location']['lat'],x['geometry']['location']['lng']})
        return l

# address(jdata)