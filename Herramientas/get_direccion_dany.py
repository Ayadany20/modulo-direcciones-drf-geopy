from geopy.geocoders import Nominatim

def get_direccion_danycore(lat: str, lon: str):
    geolocator = Nominatim(user_agent="dany")
    location = geolocator.reverse(f"{lat}, {lon}")
    return location.address


