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
# After clicking, wait 5 s (5000 ms) for the site to load
# Locator accepts a tuple as an arguement
filmData_list = WebDriverWait(browser, 5000).until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH, 
                                                                                   "//div[@class='film-content']")))
print(len(filmData_list))
'''
for filmData in filmData_list:
    filmName = filmData.find_element(by=By.XPATH,
                                     value=".//div[@class='film-content']")
    print(filmName.text)
'''
# browser.quit()

# Check if file exists in directory 
wiffSite_filename = 'wiffSite_data.txt'
fileExists_flag = os.path.exists(wiffSite_filename)

if fileExists_flag:
    pass 