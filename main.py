from init import driver
from actions import send_keys_to_element, click_on_element
from time import sleep

filling_elements = {
    "name_input":"name-input"
    # "password":"password",
}

clicking_elements = {
    "milk_checkbox":"drink2",
    "coffee_checkbox":"drink3",
    "yellow_radio":"color3"
}




def main():
    for _, element_id in filling_elements.items():
        send_keys_to_element(element_id, "my text")
    
    for _, element_id in clicking_elements.items():
        click_on_element(element_id)






if __name__ == "__main__":
    driver.get("https://practice-automation.com/form-fields/")
    main()
    sleep(5)
    driver.quit()