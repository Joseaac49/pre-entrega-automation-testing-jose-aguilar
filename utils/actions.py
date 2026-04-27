from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import *

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def login(driver, username, password):
    wait_for_element(driver, USERNAME_INPUT).send_keys(username)
    wait_for_element(driver, PASSWORD_INPUT).send_keys(password)
    wait_for_element(driver, LOGIN_BUTTON).click()

def get_products(driver):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(INVENTORY_ITEMS)
    )

def add_first_product_to_cart(driver):
    wait_for_element(driver, ADD_TO_CART_BUTTON).click()

def go_to_cart(driver):
    wait_for_element(driver, CART_ICON).click()
    WebDriverWait(driver, 10).until(
        EC.url_contains("cart")
    )
    
def get_cart_count(driver):
    return wait_for_element(driver, CART_BADGE).text