from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#Path to the Chrome Driver
#Download from https://developer.chrome.com/docs/chromedriver/downloads
path = "D:\Programas\chrome-win64\chrome-win64"
service =  Service(executable_path=path)
website = "https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ"
driver = webdriver.Chrome(service=service)

driver.get(website)