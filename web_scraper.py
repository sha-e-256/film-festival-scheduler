from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager
from festival import Film, Screening
from datetime import date, datetime, time, timedelta


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
        film_name_element = film_data.find_element(by=By.XPATH,
                                         value="./h3")  # . Means to search
                                                        # the child of the current node
        film_name = film_name_element.text
        film_screening_list = film_data.find_elements(by=By.XPATH,
                                                      value=".//div[@class='film-screen']")
        for film_screening in film_screening_list:
            
            film_screening_str = film_screening.text
            film_screen_str_list = film_screening_str.split('\n')

            film_start_time_str = film_screen_str_list[0]
            film_start_time = datetime.strptime(film_start_time_str, '%I:%M %p')
            
            
            film_length = 100  # Filler for now
            film_end_time = film_start_time + timedelta(minutes=film_length)
            
            film_date_str = film_screen_str_list[1]
            film_date = datetime.strptime(film_date_str, 
                                         '%a %b %d').date()  # Year defaults to 1900
            film_date_correct_year = film_date.replace(2022)  # Change year to 2022
            
            film_location = film_screen_str_list[2]

            # Make a Screening object
            curr_screening = Screening(screening_time_start=film_start_time,
                                       screening_time_end=film_end_time,
                                       screening_date=film_date_correct_year,
                                       screening_location=film_location)
            screening_list.append(curr_screening)

        # Make a Film object
        curr_film = Film(film_name=film_name, film_screenings=screening_list)
        film_list.append(curr_film)
        screening_list = []  # Empty the list of screenings 

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
    for film in film_list:
        print(film)

if __name__ == '__main__':
    main()
