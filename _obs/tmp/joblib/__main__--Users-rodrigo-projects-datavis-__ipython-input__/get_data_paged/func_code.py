# first line: 1
@memory.cache
def get_data_paged(query, page):
    url = 'https://www.setlist.fm/search?page={}&query={}'.format(page, query)
    browser.open(url.format(page))
    data = []
    for concert in browser.select('.setlistPreview'):
        month = concert.select('.month')[0].text
        day = concert.select('.day')[0].text
        year = concert.select('.year')[0].text
        datetext = "{}, {} {}".format(year, month, day)
        date = dateparser.parse(datetext)
        desc = concert.select('h2 a')[0].text
        idx = desc.find(' at ')+4
        loc = desc[idx:]
        loc_pieces = loc.split(',')
        #print(loc_pieces[-1],country)
        if loc == None:
            continue
        if len(loc_pieces)>=3:
            loc = ','.join(loc_pieces[-3:])
        lat, lng, code = get_latlng(loc)
        if lat and lng:
            data.append([loc, lat, lng, code, date, desc])
    return data
