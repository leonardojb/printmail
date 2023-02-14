from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import win32com.client as win32
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

load_dotenv()

login = os.getenv("") # user on the web plataform; save it on a dotenv file and call it here
password = os.getenv("") # password on the web plataform; save it on a dotenv file and call it here
sendmail = os.getenv("") # mail to send the print to; save it on a dotenv file and call it here

# Iniciate the webdriver
driver = webdriver.Edge()
driver.maximize_window()

# Navegate to the web plataform
driver.get("") #link to the web plataform here

# Wait for the input to load
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID,"")) #ID of the login input

# find and fill the input
driver.find_element(By.ID, "").send_keys(login) #ID of the login input
driver.find_element(By.ID, "").send_keys(password) #ID of the password input
driver.find_element(By.ID, "").click() #ID of the enter button

# Wait for the input to load
WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID,"")) #ID of an element after login

# Navegate to the page that will be printed
driver.get("") # page url
driver.save_screenshot("") # folder to save the print

# Send mail
outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

anexo = "" # folder that the print is saved
email.Attachments.Add(anexo)
email.Subject = "" # mail subject
email.bcc = sendmail # Recipient
email.HTMLBody = """""" # mail body
email.Send()
print("") # success mesage

driver.quit()