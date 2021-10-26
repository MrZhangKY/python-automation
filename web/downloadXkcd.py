#! python3
# downloadXkcd - download images from xckd site

import requests
import bs4
import logging
import os

# init logging and make directory to store images and init index to mark images
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.WARNING)
os.makedirs('xkcd', exist_ok=True)
index = 0
url = 'https://xkcd.com/'

while not url.endswith('#') and index<=10:
          # get html from xckd site and parse it
          res = requests.get(url)
          logging.info(res.text)
          xkcdSoup = bs4.BeautifulSoup(res.text)
          logging.info(xkcdSoup)

          # find url of images and download images
          imgElems = xkcdSoup.select('#comic img')
          logging.warning(imgElems)
          for img in imgElems:
                    logging.warning(img.get('src'))
                    img = requests.get(url + img.get('src'))
                    logging.warning(img)
                    # save image to ./xkcd
                    with open(os.path.join('xkcd', f'{index}.jpg'), 'wb') as f:
                              print(f'\033[31m downloading {index}.jpg \033[0m')
                              for iter in img.iter_content():
                                        f.write(iter)
                    index += 1
                    
          # get preview page URL
          url = 'https://xkcd.com/' + xkcdSoup.select('ul[class=comicNav] a[rel=prev]')[0].get('href')
          logging.error(xkcdSoup.select('ul[class=comicNav] a[rel=prev]')[0].get('href'))
          logging.error(url)