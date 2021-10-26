#! python3
# seachResultOpener.py - open several search results of bing search engine

import sys
import requests
import bs4
import webbrowser
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

# get the input argument
arg = sys.argv[1]

# get the being search results
logging.info('======')
logging.info('https://www.bing.com/search?q=' + arg)
logging.info('======' + '\n')
res = requests.get('https://www.bing.com/search?q=' + arg)
logging.info('======')
logging.info(res)
logging.info(res.text)
logging.info('======' + '\n')

# parse the html text
searchSoup = bs4.BeautifulSoup(res.text)
logging.info('======')
logging.info(searchSoup)
logging.info('======' + '\n')

# get the tag with <a>
elems = searchSoup.select('h2 > a')
logging.info('======')
logging.info(elems[0].get('href'))
logging.info('======' + '\n')

# open the URL
for i in range(10):
    webbrowser.open(elems[i].get('href'))