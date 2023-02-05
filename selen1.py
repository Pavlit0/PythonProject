from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('c:\intel\chromedriver.exe')
edge = webdriver.Edge('c:\intel\msedgedriver.exe')

driver.get('http://google.com')
edge.get('http://google.com')


driver.find_element(By.NAME, 'q').send_keys('pavel was here')
edge.find_element(By.NAME, 'q').send_keys('pavel was here')

chrome_text = driver.find_element(By.NAME, 'q').get_attribute('value')
edge_text = edge.find_element(By.NAME, 'q').get_attribute('value')

if chrome_text == edge_text:
    print("Same selectors")
else:
    print("Different Selectors")


