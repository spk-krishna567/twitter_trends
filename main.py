from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
import time

service=Service(executable_path='C:/chromedriver.exe')
driver=webdriver.Chrome(service=service)

driver.get("https://x.com/")
wait = WebDriverWait(driver, 30)
wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
time.sleep(10)
signin_element=driver.find_element(By.XPATH,"//div[@class='css-175oi2r r-2o02ov']//a[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-17w48nw r-a9p05 r-eu3ka r-5oul0u r-1ipicw7 r-2yi16 r-1qi8awa r-3pj75a r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21']")
driver.execute_script("arguments[0].click();", signin_element)
time.sleep(10)
print("Current URL:", driver.current_url)
input_element=driver.find_element(By.XPATH,"//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")
input_element.send_keys("[username]")
next_element=driver.find_element(By.XPATH, "//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
next_element.click()
time.sleep(5)
pass_element=driver.find_element(By.XPATH, "//input[@class='r-30o5oe r-1dz5y72 r-13qz1uu r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-fdjqy7']")
pass_element.send_keys("[password]")
time.sleep(5)
login_element=driver.find_element(By.XPATH,"//button[@class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
login_element.click()
time.sleep(5)
trends = driver.find_elements(By.XPATH, "//span[@class='r-18u37iz']//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']")
top_trends = [trend.text for trend in trends[:5]]
print("Current URL:", driver.current_url)
print(top_trends)
time.sleep(10)
driver.quit()