import time
from datetime import date
import typing


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
    def __init__(self, screening_time_start: time,
                 screening_time_end: time,
                 screening_date: date,
                 screening_location: str) -> None:
        '''
        The constructor of the Screening class.

        Parameters:
        ----------
        screening_time_start: time
            The time the screening starts.
        screening_time_end: time
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
    '''
    def __init__(self, film_name: str,
                 film_screenings: [Screening]) -> None:
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
