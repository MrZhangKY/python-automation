#! python3
# 2048player - a automatic 2048 game plyer, is loss it will try again, maybe you can train a agent to get higher score~

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# open address of 2048 game
browser = webdriver.Edge()
browser.get(' https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element_by_tag_name('html')

# candidate actions
candidateOperation = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]

for i in range(10000):
          #get board condition
          try:
                    boardCondition = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                    board = browser.find_element_by_css_selector('.tile-container')
                    chessNum = board.text.split('\n')       #get all num
                    for chess in range(len(chessNum)):
                              chessLocation = browser.find_element_by_xpath(f"/html/body/div[1]/div[3]/div[3]/div[{chess+1}]").get_attribute("class").split()[2].split("-")[2:] #get location one by one
                              boardCondition[int(chessLocation[1])-1][int(chessLocation[0])-1] = int(chessNum[chess])
          except:
                    continue
          print(f'\033[32m {boardCondition} \033[0m')
          #get score
          score = browser.find_element_by_css_selector('.score-container')
          print(f'\033[31m score:{score.text} \033[0m')
          #play after decision making
          '''decision making'''
          operation  = candidateOperation[i%4]
          htmlElem.send_keys(operation)
          #retrain after loose
          try:
                    browser.find_element_by_class_name('retry-button').click()
          except:
                    pass