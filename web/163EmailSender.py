#! python3
#163MailSender - receive for arguments
# - email address of sender
# - password of sender
# - email address of receiver
# - content of email

import sys
from selenium import webdriver
import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.DEBUG)

# get input arguments
# logging.info(sys.argv)
addrOfSender, pwdOfSender, addrOfReceiver, contOfEmail = sys.argv[1:]

# open mail address of 163Mail
'''for the user who finds errors'''
#options = webdriver.EdgeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--ignore-ssl-errors')
#options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
#browser = webdriver.Edge(options=options)
browser = webdriver.Edge()
browser.get('https://mail.163.com/')

# sign in the email
iframe = browser.find_elements_by_tag_name("iframe")[0]
browser.switch_to.frame(iframe)
emailElem = browser.find_element_by_name('email')           #fill in emailAddress
emailElem.send_keys(addrOfSender)
passwordElem = browser.find_element_by_name('password')     #fill in password
passwordElem.send_keys(pwdOfSender)
loginButton = browser.find_element_by_id('dologin')         #login in
loginButton.click()

# write email
browser.switch_to.default_content()
write_elem = browser.find_element_by_css_selector('.js-component-component ra0 mD0')
logging.info(write_elem)
print(f'\033[31m{write_elem}\033[0m')
write_elem.click()