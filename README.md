# film-festival-scheduler

## About the project
The purpose of this script is to produce an optimal schedule for viewing
films being displayed at a local film festival.

## Components of the project
The `scheduler` script is a Python script which scrapes the information on
films being displayed at the local film festival found in the DOM of the
film festival's website. 

The information is then saved in a .dat file so that when the user is 
developing a schedule, they do not need to rescrap the content of the website.
The information is stored in the .dat file as Film and Screening objects. The
`festival.py` package is a Python package which contains the Film and Screening
classes used to make the Film and Screening objects.

The user can use the `scheduler` script to develop an optimal schedule for
viewing films by inputting the films they would like to see, and the dates and
times they are available. The optimal schedule is developped using a greedy
algorithm which determines the optimal schedule by always selecting
non-overlapping films and removing films that end later and may possibly
interfere with a future film.  

## How to use the project to develop a schedule
To create a schedule, clone the project into a directory of your choice using:
```
https://github.com/sha-e-256/film-festival-scheduler.git
```
To execute the script, type the following into the terminal in the same 
directory the project has been cloned into:
```
chmod +x web_scraper
./web_scraper
```
The first line `chmod +x web_scraper` turns the script into an executable.
The second line executes the script; since the script has not been exported
to the PATH variable, `./` must be included in front of the script's name. 
