from datetime import date, datetime
from textwrap import dedent
from typing import List

'''
This package contains two classes used to store information
on films: Film and Screening. A Film object stores the name of a film,
and a list of Screening objects. A Screening object stores information on
a particular screening such as start/end time, date, and location.
This package is used in the 'scheduler' module which is the module used to
develop a schedule for a user.
'''

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


    def __str__(self) -> str:
        '''
        Creates a well-formatted string that displays the information
        on a screening.

            Returns:
                text (str): A well-formatted string that displays information
                on a Screening object.
        '''
        text = dedent(f'''\
        -> Start Time: {self.screening_time_start.time()}
        -> End Time: {self.screening_time_end.time()}
        -> Date: {self.screening_date}
        -> Location: {self.screening_location}\
        ''')
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



    def __str__(self) -> str:
        '''
        Creates a well-formatted string that displays the information on
        a film.

            Returns:
                text (str): a well-formatted string that diisplays information
                on a Film object.
        '''
        text = f'\nFilm Name: {self.film_name}\nList of Screenings:\n'
        # List comprehension using a string
        text = text.join(screening.__str__() for screening in \
            self.film_screenings)
        return text
