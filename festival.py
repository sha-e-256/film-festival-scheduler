import time
from datetime import date, datetime
from typing import List
from collections import defaultdict


class Screening:
    '''
    This class stores information on a screening.

    Attributes:
    -----------
    screening_time_start: time
        The time the screening starts.
    screening_time_end: time
        The time the screening ends.
    screening_date: date
        The date of the screening.
    screening_locaton: str
        The location of the screening.
    '''
    def __init__(self, screening_time_start: datetime,
                 screening_time_end: datetime,
                 screening_date: date,
                 screening_location: str) -> None:
        '''
        The constructor of the Screening class.

        Parameters:
        ----------
        screening_time_start: datetime
            The time the screening starts.
        screening_time_end: datetime
            The time the screening ends.
        film_date: date
            The date of the screening.
        film_locaton: str
            The location of the screening.
        '''
        self.screening_time_start = screening_time_start
        self.screening_time_end = screening_time_end
        self.screening_date = screening_date
        self.screening_location = screening_location

    def __str__(self):
        '''
        Creates a well-formatted string that displays the information
        on a screening
        '''
        text = f'''
    Start Time: {self.screening_time_start.time()}
    End Time: {self.screening_time_end.time()}
    Date: {self.screening_date}
    Location: {self.screening_location}\
    '''
        return text

class Film:
    '''
    This class stores information on a film.

    Attributes:
    -----------
    film_name: str
        Name of the film.
    film_screenings: List[Screening])
        A list of the available screenings where each
        Screening object in the list contains information on the screening such
        as the time, date, and location.
    '''
    def __init__(self, film_name: str,
                 film_screenings: List[Screening]) -> None:
        '''
        The constructor for the Film class

        Parameters:
        ----------
        film_name: str
            Name of the film.
        film_screenings: List[Screening])
            A list of the available screenings where each
            Screening object in the list contains information on the screening
            such as the time, date, and location.
        '''
        self.film_name = film_name
        self.film_screenings = film_screenings

    def __str__(self):
        '''
        Creates a well-formatted string that displays the information on
        a film.
        '''
        text = f'\nFilm Name: {self.film_name}\nList of Screenings:\n'
        # List comprehension using a string
        text = text.join(screening.__str__() for screening in self.film_screenings)
        return text

class User:
    '''
    This class stores information on a user's choices

    Attributes:
    -----------
    film_dict: defaultdict(set)
        A hashset of all films a user would like to see.
    avail_dates: defaultdict(set)
        A hashset of all dates a user is available
    '''
    def __init__(self, film_dict: defaultdict(set),
                 avail_dates: defaultdict(set)) -> None:
        '''
        The constructor for the User class

        Parameters:
        -----------
        film_dict: defaultdict(set)
            A hashset of all films a user would like to see.
        avail_dates: defaultdict(set)
            A hashset of all dates a user is available
        '''
        self.film_dict = film_dict
        self.avail_dates = avail_dates