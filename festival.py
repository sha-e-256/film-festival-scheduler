"""This package contains classes used to store information on films.

A Film object stores the name of a film and a list of Screening objects. A
Screening object stores information on a particular screening such as start/end
time, date, and location. This package is used in the 'scheduler' module which
is the module used to develop a schedule for a user.
"""
from collections import defaultdict
from datetime import date, datetime
from textwrap import dedent


class Screening:
    """This class stores information on a screening.

    Attributes:
    -----------
    screening_time_start: datetime
        The time the screening starts.
    screening_time_end: datetime
        The time the screening ends.
    screening_date: date
        The date of the screening.
    screening_locaton: str
        The location of the screening.
    """

    def __init__(self, screening_time_start: datetime,
                 screening_time_end: datetime,
                 screening_date: date,
                 screening_location: str) -> None:
        """Create an object of the Screening class.

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
        """
        self.screening_time_start = screening_time_start
        self.screening_time_end = screening_time_end
        self.screening_date = screening_date
        self.screening_location = screening_location


    def __str__(self) -> str:
        """Return a string that displays the information on a Screening object.

        Returns:
        --------
            text: str
                A string that displays the information on a Screening object.
        """
        text = dedent(f'''\
        -> Start Time: {self.screening_time_start.time()}
        -> End Time: {self.screening_time_end.time()}
        -> Date: {self.screening_date}
        -> Location: {self.screening_location}\
        ''')
        return text


class Film:
    """This class stores information on a film.

    Attributes:
    -----------
    film_name: str
        The name of the film.
    film_screenings: defaultdict(set)
        A dict of all the Screening objects for the particular film.
    """

    def __init__(self, film_name: str,
                 film_screenings: defaultdict(set)) -> None:
        """Create an object of the Film class.

        Parameters:
        ----------
        film_name: str
            Name of the film.
        film_screenings: defaultdict(set)
            A dict of all the Screening objects for the particular film.
        """
        self.film_name = film_name
        self.film_screenings = film_screenings


    def __str__(self) -> str:
        """Return a string that displays the information on a Film object.

        Returns:
        --------
            text : str
                A string that displays the information on a Film object.
        """
        text = f'\nFilm Name: {self.film_name}\nList of Screenings:\n'
        # List comprehension using a string
        text = text.join(screening.__str__() for screening in \
            self.film_screenings.values())
        return text
