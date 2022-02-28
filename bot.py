from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_NAME = YOUR_ACCOUNT_NAME
ACCOUNT_PASSWORD = YOUR_ACCOUNT_PASSWORD
SEARCH_ACCOUNT = SEARCH_ACCOUNT_NAME
CHROME_DRIVER_PATH = YOUR_CHROME_DRIVER_PATH

class Bot:

    def __init__(self):
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        username_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(ACCOUNT_NAME)

        password_input = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(ACCOUNT_PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def search_page(self):
        time.sleep(2)
        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(SEARCH_ACCOUNT)

        time.sleep(2)
        search_bar.send_keys(Keys.DOWN)
        search_bar.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(2)
        follower_link = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > header > section > ul > li:nth-child(2) > a')
        follower_link.click()
        time.sleep(1)
        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        time.sleep(1)

        for x in range(6):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            time.sleep(1)

    def follow(self):
        time.sleep(1)
        follower_buttons = self.driver.find_elements_by_css_selector("li button")

        # 2 ways:

        # 1.
        # for follower_button in follower_buttons:
        #     try:
        #         follower_button.click()
        #         time.sleep(1)
        #     except ElementClickInterceptedException:
        #         cancel_button = self.driver.find_element_by_css_selector("body > div:nth-child(20) > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        #         cancel_button.click()

        # 2.
        index = 0
        for x in range(100):

            time.sleep(2)
            button = follower_buttons[index]

            try:
                button.click()
            except ElementClickInterceptedException:
                time.sleep(2)
                cancel_button = self.driver.find_element_by_css_selector("body > div:nth-child(20) > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
                cancel_button.click()
                continue

            index += 1
            time.sleep(2)
