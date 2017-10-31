# first line: 1
@memory.cache
def get_latlng(query):
    providers = geocoder.osm, geocoder.google
    for provider in providers:
        #print(provider)
        try:  
            g=provider(query)
        except ValueError:
            continue
        if g:
            return g
    return None
