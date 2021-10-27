#! python3
# 2048player - a automatic 2048 game plyer, is loss it will try again, maybe you can train a agent to get higher score~

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open address of 2048 game
browser = webdriver.Edge()
browser.get(' https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

# automatively play
candidateOperation = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]
for i in range(10000):
          htmlElem.send_keys(candidateOperation[i%4])
          score = browser.find_element_by_css_selector('.score-container')
          print(f'\033[31m score:{score.text} \033[0m')
          try:
                    browser.find_element_by_class_name('retry-button').click()
          except:
                    pass