# first line: 1
@memory.cache
def geocode(query):
    return geocoder.google(query)
