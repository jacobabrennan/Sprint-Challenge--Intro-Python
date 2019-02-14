import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, latitude, and longitude.


class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.lat = float(latitude)
        self.lon = float(longitude)

    def __str__(self):
        return F'({self.name}, {self.lat}, {self.lon})'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other
# examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
    with open('cities.csv', newline='') as cities_file:
        city_reader = csv.reader(cities_file)
        # Skip first line, which is a header
        next(city_reader)
        for city_data in city_reader:
            new_city = City(city_data[0], city_data[3], city_data[4])
            cities.append(new_city)
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the
# `cityreader` function. This function should output all the cities that fall
# within the coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint:
# normalize the input data so that it's always one or the other, then search
# for cities. In the example below, inputting 32, -120 first and then 45, -100
# should not change the results of what the `cityreader_stretch` function
# returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# Get latitude and longitude values from the user
corner1 = input("Enter lat1,lon1: ").split(',')
# Ensure that user provided exactly two coordinates
if(len(corner1) != 2):
    raise Exception('The coordinates were not in the correct format.')
# Attempt to convert to floating point numbers
try:
    corner1 = [float(item) for item in corner1]
except ValueError:
    raise Exception('The coordinates were not in the correct format.')

# Do it again for the second corner
corner2 = input("Enter lat2,lon2: ").split(',')
# Ensure that user provided exactly two coordinates
if(len(corner2) != 2):
    raise Exception('The coordinates were not in the correct format.')
try:
    corner2 = [float(item) for item in corner2]
# Attempt to convert to floating point numbers
except ValueError:
    raise Exception('The coordinates were not in the correct format.')


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # Ensure that the lat and lon valuse are all floats
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)
    lat_low = min(lat1, lat2)
    lat_high = max(lat1, lat2)
    lon_low = min(lon1, lon2)
    lon_high = max(lon1, lon2)
    # Go through each city and check to see if it falls within
    # the specified coordinates.
    within = []
    for city in cities:
        if(city.lat > lat_high or city.lon > lon_high):
            continue
        if(city.lat < lat_low or city.lon < lon_low):
            continue
        within.append(city)

    return within

print(cityreader_stretch(
    corner1[0], corner1[1],
    corner2[0], corner2[1],
    cities,
))
