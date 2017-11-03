# first line: 1
@memory.cache
def get_latlng(query):
    g=geocoder.google(query)
    if g:
        return g.latlng
    else:
        return None, None
