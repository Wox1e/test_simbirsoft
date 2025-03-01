from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


service = Service(executable_path="drivers/chromedriver.exe")
driver = webdriver.Chrome(service = service)


