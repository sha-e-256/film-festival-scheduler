import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
browser.get('https://windsorfilmfestival.com/')
browser.quit()

# Check if file exists in directory 
wiffSite_filename = 'wiffSite_data.txt'
fileExists_flag = os.path.exists(wiffSite_filename)

if fileExists_flag:
    pass 