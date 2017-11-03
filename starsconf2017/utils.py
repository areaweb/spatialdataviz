import json

def persist_to_file(file_name='cache.dat'):
    def decorator(original_func):

        try:
            cache = json.load(open(file_name, 'r'))
        except (IOError, ValueError):
            cache = {}

        def new_func(param):
            if param not in cache:
                cache[param] = original_func(param)
                json.dump(cache, open(file_name, 'w'))
            return cache[param]

        return new_func

    return decorator

from joblib import Memory
memory = Memory(cachedir='tmp', verbose=0)

@memory.cache
def get_latlng(query):
    g=geocoder.google(query)
    if g:
        return g.latlng
    else:
        return None, None