from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from config import TWITTER_USERNAME, TWITTER_PASSWORD

# Setting up Selenium

PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_driver_path = "C:\Development\chromedriver.exe"
