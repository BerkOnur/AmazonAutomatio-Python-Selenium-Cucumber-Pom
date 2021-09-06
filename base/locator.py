from typing import ClassVar
from selenium.webdriver.remote.webdriver import WebDriver
from abc import abstractmethod
from time import sleep
import base.elements as elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.command import Command
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException



class Locator:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def goTo(self, url):
        self.driver.get(url)


    def goToAmazon(self):
        self.driver.get('https://www.amazon.com')

    def clickSignInButton(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.SIGN_IN_BUTTON))).click()

    def fillUsernameInput(self, username):
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.USER_BY_NAME))).send_keys(username)
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.CONTINUE_BUTTON))).click()
        sleep(1)
    
    def fillPasswordInput(self, password):
        sleep(1)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.USER_BY_PASSWORD))).send_keys(password)
        sleep(1)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.CLICK_SIGNUP_BUTTON))).click()

    def fillSearchField(self, brand):
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.SEARCH_FIELD))).send_keys(brand + Keys.ENTER)
        
    def searchResult(self):
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.XPATH, elements.SEARCH_RESULT)))
        
    def secondPage(self):
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.XPATH, elements.CLICK_SECOND_PAGE))).click()

    def thirdProduct(self):
        sleep(2)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.XPATH, elements.CLICK_THIRD_PRODUCT))).click()
    
    def addList(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.CLICK_ADD_LIST))).click()
    
    def closeAddList(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.CLOSE_ADD_LIST))).click()

    def hover(self):
        sleep(2)
        mouse = self.driver.find_element(By.CSS_SELECTOR, elements.MOUSE_HOVER)
        webdriver.ActionChains(self.driver).move_to_element(mouse).perform()

    def shoppingList(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, elements.SHOPPING_LIST).click()

    def confirmm(self):
        sleep(1)
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.CSS_SELECTOR, elements.SEE_PRODUCT)))

    def deleteProduct(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, elements.DELETE_PRODUCT).click()
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, elements.DELETED_ALERT)

    
