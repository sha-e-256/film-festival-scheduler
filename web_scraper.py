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
for filmData in filmData_list:
    filmName = filmData.find_element(by=By.XPATH,
                                     value="./h3") # . Means to search 
                                                   # the child of the current node
    print(filmName.text)
browser.quit()
