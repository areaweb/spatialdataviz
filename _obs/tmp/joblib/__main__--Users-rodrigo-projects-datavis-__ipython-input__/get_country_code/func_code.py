# first line: 1
@memory.cache
def get_country_code(txt):
    names = difflib.get_close_matches(txt, country_names)
    if names:
        return country_dict[names[0]]
    else:
        return txt
