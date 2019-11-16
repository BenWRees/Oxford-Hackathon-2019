import sys
import GetPlaces
import GoogleRoutePlanner
import IndiceToPostcodeConverter
import Graph
import postcodes
import TravellingSalesman
import UserData
import json


def main():
    jsondat = getPlaces(sys.argv[0], sys.argv[1], sys.argv[2])

if __name__ == "__main__":    
    main()