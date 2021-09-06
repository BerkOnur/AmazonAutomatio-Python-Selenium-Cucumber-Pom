from base.locator import Locator
from behave import given, when, then
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time, math
import base.elements as elements
import base.locator
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
locator = Locator(driver)

def after_feature(context, feature):
    driver.quit()


@given('I visit Amazon')
def visit(contex):
    locator.goToAmazon()

@when('I click Sign In button')
def click(contex):
    #sleep(1)
    locator.clickSignInButton()

@when('I login Amazon with username "{username}" and password "{password}"')
def login(contex, username, password):
    sleep(1)
    locator.fillUsernameInput(username)
    sleep(1)
    locator.fillPasswordInput(password)
    
@when('I write "{brand}" in search field and click')
def search(contex, brand):
    sleep(2)
    locator.fillSearchField(brand)

@then('I check result is samsung')
def result(contex):
    sleep(2)
    locator.searchResult()

@then('I click second page')
def second(contex):
    sleep(2)
    locator.secondPage()

@when('I click third product')
def product(contex):
    sleep(1)
    locator.thirdProduct()

@then('I click add list button')
def add(contex):
    sleep(1)
    locator.addList()

@then('I close add list page')
def close(contex):
    sleep(1)
    locator.closeAddList()

@when('I click list button and later click Shopping List button')
def list(contex):
    sleep(1)
    locator.hover()
    sleep(1)
    locator.shoppingList()

@then('I see product and check')
def productConfirm(contex):
    sleep(1)
    locator.confirmm()

@then('I deleted the product and I see deleted alert')
def delete(contex):
    sleep(1)
    locator.deleteProduct()