from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("c:/intel/chromedriver/chromedriver.exe"))
driver = webdriver.edge(service=Service("c:/intel/ed/chromedriver.exe"))

driver.get('https://google.com')


driver.find_element(By.NAME, 'q').send_keys('pavel was here')
edge.find_element(By.NAME, 'q').send_keys('pavel was here')

chrome_text = driver.find_element(By.NAME, 'q').get_attribute('value')
edge_text = edge.find_element(By.NAME, 'q').get_attribute('value')

if chrome_text == edge_text:
    print("Same selectors")
else:
    print("Different Selectors")




