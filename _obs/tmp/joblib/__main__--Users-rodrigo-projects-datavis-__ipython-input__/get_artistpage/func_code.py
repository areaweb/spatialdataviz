# first line: 1
@memory.cache
def get_artistpage(query, idx):
    query = query.replace(' ', '+')
    url = 'https://www.setlist.fm/search?page={}&query={}'.format(idx, query)
    browser = RoboBrowser(history=True, parser='html5lib')
    return browser
