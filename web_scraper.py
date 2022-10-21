import os
from selenium import webdriver

driver = webdriver.Firefox()

driver.get('https://windsorfilmfestival.com/')


# Check if file exists in directory 
wiffSite_filename = 'wiffSite_data.txt'
fileExists_flag = os.path.exists(wiffSite_filename)

if fileExists_flag:
    pass 