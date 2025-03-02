"""Main module for UI-autotesting"""
from init import driver
from actions import click_on_element, fill_element, select_choose, ul_to_list, is_alert_appeared
from utils import longest_str_in_list

element_id_list = {
    "name":"name-input",
    "email":"email",
    "yellow_radio":"color3",
    "milk_checkbox":"drink2",
    "coffee_checkbox":"drink3",
}

element_xpath_list = {
    "password_input":'//*[@id="feedbackForm"]/label[2]/input',
    "message_input":'//*[@id="message"]'
}

css_selector_list = {
    "automation_select":"#automation",
    "automation_tools_ul":"#feedbackForm > ul",
    "submit_button":"#submit-btn"
}



def main():
    fill_element(text="Maxim", element_id=element_id_list["name"],)
    fill_element(text="somepassword", xpath=element_xpath_list["password_input"])
    click_on_element(element_id=element_id_list["coffee_checkbox"])
    click_on_element(element_id=element_id_list["milk_checkbox"])
    click_on_element(element_id=element_id_list["yellow_radio"])
    select_choose(value="yes", css_selector=css_selector_list["automation_select"])
    fill_element(text="ivanovmaxim39@mail.ru", element_id=element_id_list["email"])

    ul_list = ul_to_list(css_selector=css_selector_list["automation_tools_ul"])
    ul_list_lenght = len(ul_list)
    longest_tool_word = longest_str_in_list(ul_list)

    fill_element(
        text = str(ul_list_lenght) + " " + longest_tool_word,
        xpath=element_xpath_list["message_input"]
    )

    click_on_element(css_selector=css_selector_list["submit_button"])
    assert is_alert_appeared(timeout_sec=1)







if __name__ == "__main__":
    driver.get("https://practice-automation.com/form-fields/")
    main()
    driver.quit()
