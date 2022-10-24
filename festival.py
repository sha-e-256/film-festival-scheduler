import time
from datetime import date
import typing


class Screening:
    '''
    This class stores information on a screening.

    Attributes:
    -----------
    film_time: time
        The time of the screening.
    film_date: date
        The date of the screening.
    film_locaton: str
        The location of the screening.
    '''
    def __init__(self, screening_time: time,
                 screening_date: date,
                 screening_location: str) -> None:
        '''
        The constructor of the Screening class.

        Parameters:
        ----------
        film_time: time
            The time of the screening.
        film_date: date
            The date of the screening.
        film_locaton: str
            The location of the screening.
        '''
        self.screening_time = screening_time
        self.screnning_date = screening_date
        self.screening_location = screening_location


class Film:
    '''
    This called stores information on a film.

    Attributes:
    -----------
    film_name: str
        Name of the film.
    film_screenings: List[Screening])
        A list of the available screenings where each
        Screening object in the list contains information on the screening such
        as the time, date, and location.
    film_length: int
        The length of a film in minutes.
    '''
    def __init__(self, film_name: str,
                 film_screenings: [Screening],
                 film_length: int) -> None:
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
        film_length: int
        '''
        self.film_name = film_name
        self.film_screenings = film_screenings
        self.film_length = film_length
