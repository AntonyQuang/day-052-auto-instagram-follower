from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
from random import randint
from config import USERNAME, PASSWORD

# Setting up Selenium

similar_account = "grant_house_press"

chrome_driver_path = "C:\Development\chromedriver.exe"


class InstaFollower:

    def __init__(self):
        self.user = USERNAME
        self.password = PASSWORD
        self.instagram_endpoint = "https://www.instagram.com/"
        s = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        cookies_accept = self.driver.find_element(by=By.CSS_SELECTOR, value=".aOOlW, .bIiDR")
        cookies_accept.click()
        time.sleep(randint(4000, 8000) / 999)
        username_input = self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value="input[aria-label='Phone number, username or email address']")
        username_input.send_keys(USERNAME)
        time.sleep(randint(0, 4000) / 999)
        password_input = self.driver.find_element(by=By.CSS_SELECTOR,
                                                  value="input[aria-label='Password']")
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(randint(0, 4000) / 999)
        print("Logged in")

    def find_followers(self):
        print("Going to the instagram account")
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar_account}/")
        time.sleep(2)
        try:
            username_input = self.driver.find_element(by=By.CSS_SELECTOR,
                                                      value="input[aria-label='Phone number, username or email address']")
            username_input.send_keys(USERNAME)
            time.sleep(randint(1000, 4000) / 999)
            password_input = self.driver.find_element(by=By.CSS_SELECTOR,
                                                      value="input[aria-label='Password']")
            password_input.send_keys(PASSWORD)
            password_input.send_keys(Keys.ENTER)
            self.find_followers()
        except NoSuchElementException:
            print("No need to re-enter log in details")

        followers = self.driver.find_element(by=By.XPATH,
                                             value="//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div/span")
        follower_count = int(followers.get_attribute("title").replace(",", ""))
        followers.click()
        time.sleep(randint(3000, 4000) / 999)
        followers_box = self.driver.find_element(by=By.CSS_SELECTOR, value=".isgrP")
        followers_scrolled = self.driver.find_elements(by=By.CSS_SELECTOR, value=".isgrP li")
        followers_scrolled_before = 0

        while len(followers_scrolled) != followers_scrolled_before:
            followers_scrolled_before = len(followers_scrolled)
            for i in range(10):
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', followers_box)
                time.sleep(randint(0, 400) / 301)
            followers_scrolled = self.driver.find_elements(by=By.CSS_SELECTOR, value=".isgrP li")

    def follow(self):
        followers = self.driver.find_elements(by=By.CSS_SELECTOR, value="li button")
        for follow_button in followers:
            if follow_button.text == "Follow":
                follow_button.click()
                time.sleep(randint(1000, 2000) / 308)
            else:
                pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
