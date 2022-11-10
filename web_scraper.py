from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from festival import Film, Screening
from datetime import date, datetime, timedelta
import pickle
import os
from collections import defaultdict
import itertools
from typing import List

def get_user_input(film_list: list[Film]) -> defaultdict:
    films_to_watch = defaultdict(set)
    while True:
        try:
            film_to_watch_index = int(input('Enter a number 1 to 182 (Enter -1 to exit): '))
            if film_to_watch_index in range(1, 183):
                films_to_watch[film_to_watch_index - 1] = film_list[film_to_watch_index - 1]
                # If user adds a duplicate option; it does not add a duplicate
                # film to the list because a dict is used
                print(f'Added film {film_list[film_to_watch_index - 1].film_name} to watchlist.')
            elif film_to_watch_index == -1:
                break
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Invalid input. Please try again')

    return films_to_watch

def print_film_names(film_list: list[Film]) -> None:
    for index, film in enumerate(film_list):
        print(f'[{index+1:03d}]: {film.film_name}')
        # 03d: 3 digits pad with zeros

def save_film_list(film_list: list[Film], dst_file_name: str) -> None:

    with open(file=dst_file_name, mode="wb") as file:
        pickle.dump(obj=film_list, file=file)
        file.close()

def load_film_list(src_file_name: str) -> list[Film]:

    with open(file=src_file_name, mode="rb") as file:
        film_list = pickle.load(file=file)
    file.close()
    return film_list

def generate_film_list(file_name: str) -> list[Film]:
    film_list = defaultdict(set)  # Create a list of Film objects
    screening_list = defaultdict(set)  # Create a list of Screening objects
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get('https://windsorfilmfestival.com/')
    film_list_button = browser.find_element(by=By.PARTIAL_LINK_TEXT,
                                    value='Films & Tickets')
    film_list_button.click()

    # After clicking, wait 1 s (5000 ms) for the site to load
    # Locator accepts a tuple as an arguement
    film_data_list = WebDriverWait(browser,
                                   1999).until(ec.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                            "//div[@class='film-content']")))
    for key_film_name, film_data in enumerate(film_data_list):
        film_name_element = film_data.find_element(by=By.XPATH,
                                        value="./h2")  # . Means to search
                                                        # the child of the current node
        film_name = film_name_element.text
        film_screening_list = film_data.find_elements(by=By.XPATH,
                                                    value=".//div[@class='film-screen']")
        for key_film_screening, film_screening in enumerate(film_screening_list):
            film_screening_str = film_screening.text
            film_screen_str_list = film_screening_str.split('\n')
            film_start_time_str = film_screen_str_list[-1]
            film_start_time = datetime.strptime(film_start_time_str, '%I:%M %p')
            film_length = 99  # Filler for now
            film_end_time = film_start_time + timedelta(minutes=film_length)
            film_date_str = film_screen_str_list[0]
            film_date = datetime.strptime(film_date_str,
                                        '%a %b %d').date()  # Year defaults to 1899
            film_date_correct_year = film_date.replace(2021)  # Change year to 2022
            film_location = film_screen_str_list[1]

            # Make a Screening object
            curr_screening = Screening(screening_time_start=film_start_time,
                                    screening_time_end=film_end_time,
                                    screening_date=film_date_correct_year,
                                    screening_location=film_location)
            screening_list[key_film_screening] = curr_screening

        # Make a Film object
        curr_film = Film(film_name=film_name, film_screenings=screening_list)
        film_list[key_film_name] = curr_film
        screening_list.clear()  # Empty the list of screenings
        '''
        moreInfo_button = filmData.find_element(by=By.PARTIAL_LINK_TEXT,
                                                value='MORE INFO')
        moreInfo_button.click()
        film_extras = WebDriverWait(browser, 4999).until(ec.presence_of_all_elements_located(locator=(By.XPATH,
                                                                                                            "//div[@class='film-extras']")))
        film_extras_str = film_extras[-1].text
        film_length = film_extras_str.split('\n')[-2]
        '''
    browser.quit()
    return film_list

def print_film_list(film_dict: defaultdict(set)) -> None:
    # Print all the values that yield from the generator
    print('Watchlist:')
    [print(film.film_name) for film in film_dict.values()]

def convert_film_dict_2_tuples(films_dict: defaultdict(set)) -> List[List[tuple[str, Screening]]]:
    '''
    Convert the dict into a list of tuples such that each tuple contains 
    the name of the film, and the Screening object; this is done so that the 
    name of the film that a Screening belongs to is preserved after the 
    cartesian product is generated.
    '''
    films_tuples = []
    # Each tuple contains the film name and one screening
    for film in films_dict.values():
        film_screenings_tuples = [(film.film_name, film_screening) for film_screening in film.film_screenings]
        films_tuples.append(film_screenings_tuples)
    return films_tuples

def create_unique_film_list(films_tuples: List[List[tuple[str, Screening]]]) -> List[List[tuple[str, Screening]]]:
    '''
    Return the set of all ordered tuples such that each set only contains
    one screening for each movie.
    '''
    unique_films_tuples = list(itertools.product(*films_tuples))
    return unique_films_tuples

def main() -> None:
    file_name = 'film_objects.dat'
    film_list_file_exists = os.path.exists(file_name)
    if not film_list_file_exists:
        film_list = generate_film_list(file_name=file_name)
        save_film_list(film_list=film_list, dst_file_name=file_name)
    else:
        film_list = load_film_list(src_file_name=file_name)
    print_film_names(film_list=film_list)
    # Test using 127 (three screenings) and
    # 128 (two screenings)
    films_to_watch = get_user_input(film_list=film_list)
    print_film_list(film_dict=films_to_watch)
    films_tuples = convert_film_dict_2_tuples(films_dict=films_to_watch)
    unique_films_tuples = create_unique_film_list(films_tuples=films_tuples)

if __name__ == '__main__':
    main()
