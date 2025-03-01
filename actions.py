from init import driver, service, By, Select


def send_keys_to_element(element_id:str, text:str) -> None:
    name_input = driver.find_element(By.ID, element_id)
    name_input.send_keys(text)

def click_on_element(element_id:str) -> None:
    checkbox = driver.find_element(By.ID, element_id)
    checkbox.click()

def choose_select_by_value(element_id:str, value:str = "undecided"):
    select_element = driver.find_element(By.ID, element_id)
    select = Select(select_element)
    select.select_by_value(value)


