import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
base_url = 'https://twitter.com/search?q='
query = 'starsconf'
url = base_url + query

browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for _ in range(55):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)

    tweets = browser.find_elements_by_class_name('tweet-text')

    for tweet in tweets:
        if query in tweet.text:
            print(tweet.text)
