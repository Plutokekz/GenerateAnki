from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from private import password, email


class Browser:

    def __init__(self, profile):
        self.driver = webdriver.Firefox(profile)
        self.login()

    def login(self):
        self.driver.get("https://de.forvo.com/login/")
        login_email = self.driver.find_element_by_xpath('//*[@id="login"]')
        login_email.send_keys(email)
        login_password = self.driver.find_element_by_xpath('//*[@id="password"]')
        login_password.send_keys(password)
        login_password.send_keys(Keys.RETURN)
        sleep(0.5)

    def search_word(self, word):
        search_field = self.driver.find_element_by_xpath(
            '//*[@id="word_search_header"]')  # //*[@id="word_search_header"]
        search_field.send_keys(word)
        search_field.send_keys(Keys.RETURN)
        sleep(0.5)
        try:
            word = self.driver.find_element_by_xpath('/html/body/div[1]/div[5]/div/section/article/div/ul/li/a')
        except NoSuchElementException as e:
            print("Word not available")
            return
        word.click()
        sleep(0.5)
        download = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[5]/div/section/div[1]/article[1]/ul/li[1]/div/div/p[3]')
        download.click()

    def search_list_of_words(self, words):
        for word in words:
            self.search_word(word)

    def quit(self):
        self.driver.quit()
