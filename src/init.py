"""Initial module for UI-testing"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.execute_cdp_cmd('Network.setBlockedURLs', {"urls": ["https://pagead2.googlesyndication.com"]})           # Blocking Google AdSense unaccessible url
driver.execute_cdp_cmd('Network.enable', {})
driver.set_page_load_timeout(5)
