import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://windsorfilmfestival.com/')
filmList_button = browser.find_element(by=By.PARTIAL_LINK_TEXT,
                                       value='Films & Tickets')
filmList_button.click()
# After clicking, wait 1 s (1000 ms) for the site to load
# WebDriverWait(browser, 1000).until(expected_conditions.presence_of_element_located(by=By.CLASS_NAME, 
#                                                                                   value='festival-schedule-films-list'))
print('found')
'''
try:
    filmNames = browser.find_elements(by=By.XPATH, 
                                      value="//div[@class='festival-schedule-films-list-item']")
    print(*fileNames)
except :
    print('Unable to locate element')
'''
# browser.quit()

# Check if file exists in directory 
wiffSite_filename = 'wiffSite_data.txt'
fileExists_flag = os.path.exists(wiffSite_filename)

if fileExists_flag:
    pass 