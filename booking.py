from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

message = '''Choose your preferred time:\n
            Press 1 for 0800-0900\n
            Press 2 for 0900-1000\n
            Press 3 for 1000-1100\n
            Press 4 for 1100-1200\n
            Press 5 for 1200-1300\n
            Press 6 for 1300-1400\n
            Press 7 for 1400-1500\n
            Press 8 for 1500-1600\n
            Press 9 for 1600-1700\n
            Press 10 for 1700-1800\n
            Press 11 for 1800-1900\n
            Press 12 for 1900-2000\n
            Press 13 for 2000-2100\n
            Press 14 for 2100-2200\n'''

message2 = "Choose your preferred date (eg 03-Mar-2023): "
message3 = "Choose your preferred court 1-6: "

preferred_time = input(message)
preferred_date = input(message2)
court = input(message3)

browser = webdriver.Edge()
#Put the link you want the webdriver to access in the function. In this case, it is NTU SRC booking website
browser.get('https://sso.wis.ntu.edu.sg/webexe88/owa/sso_login1.asp?t=1&p2=https://wis.ntu.edu.sg/pls/webexe88/srce_smain_s.Notice_O&extra=&pg=') 

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'UserName'))
    )
finally:
    pass

# Change your NTU username here.
user_name = 'USERNAME'
fill_name = browser.find_element(By.NAME, 'UserName')
fill_name.send_keys(user_name)

submit_name_button = browser.find_element(By.NAME, 'bOption')
submit_name_button.click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'PIN'))
    )
finally:
    pass

# Change your NTU password here.
user_password = 'PASSWORD'
fill_password = browser.find_element(By.NAME, 'PIN')
fill_password.send_keys(user_password)

submit_password_button = browser.find_element(By.NAME, 'bOption')
submit_password_button.click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='1BB26']"))
    )
finally:
    pass

while (True):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if (current_time == "00:00"):
        break

badminton_radio = browser.find_element(By.XPATH, "//input[@value='1BB26']")
badminton_radio.click()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='1BB2BB0{court}{date}{time}']".format(court = court, date = preferred_date, time = preferred_time)))
    )
finally:
    pass

select_time = browser.find_element(By.XPATH, ("//input[@value='1BB2BB0{court}{date}{time}']".format(court = court, date = preferred_date, time = preferred_time)))
select_time.click()
    

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@value='Confirm']"))
    )
finally:
    pass

confirm = browser.find_element(By.XPATH, "//input[@value='Confirm']")
confirm.click()
