# import selenium
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from datetime import datetime
import time
# from helpers.SECRETS import GH_TOKEN
import re
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
# os.environ["GH_TOKEN"]=GH_TOKEN

def get_driver():
    path_to_driver = '/Users/geckodriver'
    service = Service('path_to_driver')
    options = Options()
    options.add_argument('--incognito')
    options.add_argument('start-maximized')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(3)
    return driver
