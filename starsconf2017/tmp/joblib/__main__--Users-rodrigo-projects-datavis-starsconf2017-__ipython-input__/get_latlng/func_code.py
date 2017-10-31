# first line: 1
@memory.cache
def get_latlng(query):
    try:
        g=geocoder.google(query)
        if g:
            country = g.geojson['features'][0]['properties']['country']
            code=countries.get(country).alpha3
            print(query, g.latlng, code)
            return g.latlng+[code]
        else:
            return None, None, None
    except:
        return None, None, None
