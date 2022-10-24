from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager
from festival import Film, Screening
from datetime import datetime

def main() -> int:

    film_list = []  # Create a list of Film objects
    screening_list = []  # Create a list of Screening objects
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get('https://windsorfilmfestival.com/')
    film_list_button = browser.find_element(by=By.PARTIAL_LINK_TEXT,
                                       value='Films & Tickets')
    film_list_button.click()

    # After clicking, wait 2 s (5000 ms) for the site to load
    # Locator accepts a tuple as an arguement
    film_data_list = WebDriverWait(browser, 2000).until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                                                "//div[@class='film-content']")))
    for film_data in film_data_list:
        film_name = film_data.find_element(by=By.XPATH,
                                         value="./h3")  # . Means to search
                                                        # the child of the current node
        film_screening_list = film_data.find_elements(by=By.XPATH,
                                                      value=".//div[@class='film-screen']")
        for film_screening in film_screening_list:
            film_screening_str = film_screening.text
            film_screen_str_list = film_screening_str.split('\n')
            film_time_str = film_screen_str_list[0]
            film_time = datetime.strptime(film_time_str, '%I:%M %p').time()
            film_date_str = film_screen_str_list[1]
            film_date = datetime.strptime(film_date_str, '%a %b %d').date()
            film_date_correct_year = film_date.replace(2022)
            film_location = film_screen_str_list[2]
            film_length = 120  # Filler for now
        # curr_film = Film(film_name=film_name.text, )
        # film_list.append(curr_film)

        '''
        moreInfo_button = filmData.find_element(by=By.PARTIAL_LINK_TEXT,
                                                value='MORE INFO')
        moreInfo_button.click()
        film_extras = WebDriverWait(browser, 5000).until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                                            "//div[@class='film-extras']")))
        film_extras_str = film_extras[0].text
        film_length = film_extras_str.split('\n')[-1]
        '''
    browser.quit()

if __name__ == '__main__':
    main()
