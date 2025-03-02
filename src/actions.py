"""Elements interaction module"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException as ClickException 
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from init import driver


def find_element(element_id: str = None, xpath: str = None, css_selector: str = None) -> WebElement:
    """ Finds element on page
    """
    element = None

    if xpath is not None:
        element = driver.find_element(By.XPATH, xpath)

    if css_selector is not None:
        element = driver.find_element(By.CSS_SELECTOR, css_selector)

    if element_id is not None:
        element = driver.find_element(By.ID, element_id)

    return element

def fill_element(text: str, element_id: str = None, xpath: str = None, css_selector: str = None) -> None:
    """ Fills element with *text* argument
    """
    element = find_element(
        element_id=element_id, xpath=xpath, css_selector=css_selector
    )
    element.send_keys(text)

def click_on_element(element_id: str = None, css_selector: str = None, xpath: str = None) -> None:
    """Clicks on element
    """
    element = find_element(
        element_id=element_id, xpath=xpath, css_selector=css_selector
    )
    try:
        element.click()
    except ClickException:
        driver.execute_script("arguments[0].click();", element)

def select_choose(value: str, element_id: str = None, xpath: str = None, css_selector: str = None):
    """Chooses value on select element
    """
    element = find_element(
        element_id=element_id, xpath=xpath, css_selector=css_selector
    )
    select = Select(element)
    try:
        select.select_by_value(value)
    except NoSuchElementException:
        print("Not a possible value")

def ul_to_list(element_id: str = None, xpath: str = None, css_selector: str = None):
    """Returns list for <li> elements in <ul>"""
    ul = find_element(element_id=element_id, xpath=xpath, css_selector=css_selector)
    items = ul.find_elements(By.TAG_NAME, "li")
    lst = []
    for item in items:
        lst.append(item.text)
    return lst

def is_alert_appeared(timeout_sec: int) -> bool:
    """Returns true if alert was appeared, false if not"""
    try:
        WebDriverWait(driver, timeout_sec).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
        return True
    except TimeoutException:
        print("no alert")
        return False
