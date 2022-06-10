
from selenium import webdriver
import time
import pyautogui

path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)

driver.maximize_window()

driver.get(
    "https://sso.acesso.gov.br/login?client_id=login.esocial.gov.br&authorization_id=18148b9be79")

time.sleep(3)

button = driver.find_element_by_tag_name('button')

button.click()

buttonCertificadoDigital = pyautogui.locateOnScreen(
    "LoginCertificado.png", grayscale=True)

pyautogui.click(buttonCertificadoDigital)

time.sleep(3)

pyautogui.press("enter")


time.sleep(10)
