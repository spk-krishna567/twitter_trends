from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from datetime import datetime
import requests
import time
import uuid

# Set up MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
if(client):
    print("database connected")
db = client.twitter_trends
collection = db.trends

# Function to get new proxy from ProxyMesh
def get_new_proxy():
    proxy_url = "http://umaa567:proxy@us-ny.proxymesh.com:31280"
    return proxy_url

def fetch_trending_topics():
    # Configure Selenium to use Chrome and ProxyMesh
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = get_new_proxy()
    proxy.ssl_proxy = get_new_proxy()

    options = Options()
    
    driver = webdriver.Chrome(service=Service("C:/chromedriver.exe"), options=options)

    try:
        # Log in to Twitter
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
        print("logged in")
        time.sleep(10)
        trends = driver.find_elements(By.XPATH, "//span[@class='r-18u37iz']//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']")
        top_trends = [trend.text for trend in trends[:5]]
        print("Current URL:", driver.current_url)
        print(top_trends)   
        end_time = datetime.utcnow()

        # Get IP address used
        ip_address = requests.get("http://api.ipify.org").text

        # Store in MongoDB
        record = {
            "_id": str(uuid.uuid4()),
            "trend1": top_trends[0] if len(top_trends) > 0 else "",
            "trend2": top_trends[1] if len(top_trends) > 1 else "",
            "trend3": top_trends[2] if len(top_trends) > 2 else "",
            "trend4": top_trends[3] if len(top_trends) > 3 else "",
            "trend5": top_trends[4] if len(top_trends) > 4 else "",
            "end_time": end_time,
            "ip_address": ip_address
        }
        collection.insert_one(record)
        
        return record
    finally:
        driver.quit()

if __name__ == "__main__":
    result = fetch_trending_topics()
    print(result)
