from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager


def main() -> int:
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get('https://windsorfilmfestival.com/')
    
    
    filmList_button = browser.find_element(by=By.PARTIAL_LINK_TEXT,
                                       value='Films & Tickets')
    filmList_button.click()

    # After clicking, wait 2 s (5000 ms) for the site to load
    # Locator accepts a tuple as an arguement
    filmData_list = WebDriverWait(browser, 2000).until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                                            "//div[@class='film-content']")))
    for filmData in filmData_list:
        filmName = filmData.find_element(by=By.XPATH,
                                     value="./h3") # . Means to search
                                                   # the child of the current node
        
        moreInfo_button = filmData.find_element(by=By.PARTIAL_LINK_TEXT,
                                               value='MORE INFO')
        moreInfo_button.click()
        film_extras = WebDriverWait(browser, 5000).until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                                            "//div[@class='film-extras']")))
        film_extras_str = film_extras[0].text
        film_length = film_extras_str.split('\n')[-1]
    browser.quit()

if __name__ == '__main__':
    main()
