import math

# Sample data 
coordinates1 = {'lat': 1.346316, 'lon': 103.931746}
coordinates2 = {'lat': 1.357679, 'lon': 103.972348}

# Return distance between two points in metres
def calcDistance(lat1, lon1, lat2, lon2):
    R = 6371e3
    lat1_radians = math.radians(lat1)
    lat2_radians = math.radians(lat2)
    latDiff_radians = math.radians(lat2 - lat1)
    lonDiff_radians = math.radians(lon2 - lon1)

    a = math.sin(latDiff_radians / 2) * math.sin(latDiff_radians / 2) + math.cos(lat1_radians) * math.cos(lat2_radians) * math.sin(lonDiff_radians / 2) * math.sin(lonDiff_radians / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in metres
    return R * c

distance = calcDistance(coordinates1['lat'], coordinates1['lon'], coordinates2['lat'], coordinates2['lon'])

