import requests
from bs4 import BeautifulSoup

# Check if file exists in directory 
# and sit this boolean accordingly
file_exists = True  

if not file_exists:
    wiffSite_request = requests.get('https://windsorfilmfestival.com/about/')
    wiffSite_request.raise_for_status()  # Throw an error if cannot access link
    wiffSite_file = open('wiffSite.html', 'wb')
    for data in wiffSite_request.iter_content(100000):
        wiffSite_file.write(data)

# If file exists, call this section; otherwise; generated file
# then class this section
filmList_soup = BeautifulSoup(wiffSite_file, 'html.parser')
filmNames = filmList_soup.find_all(attrs={"class": "festival-schedule-films-list-item"})
wiffSite_file.close()
