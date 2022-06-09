
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium import webdriver
import time

# import Alert


path = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(path)
options = webdriver.ChromeOptions()
options.add_argument('acceptSslCerts')

driver.maximize_window()

driver.get(
    "https://sso.acesso.gov.br/login?client_id=login.esocial.gov.br&authorization_id=18148b9be79")

try:
    button = driver.find_element_by_tag_name('button')
except TimeoutException:
    print("no button")

button.click()

buttonCertificadoDigital = driver.find_element_by_link_text(
    "Seu certificado digital")


driver._switch_to.default_content()
buttonCertificadoDigital.click()
driver._switch_to.default_content()


time.sleep(10)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
print("enter")
actions.perform()

try:

    alert = driver.switchTo().alert()
    print("OOOOOOOOOO", alert)
    alert.accept()

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    print("enter")
    actions.perform()

    print("alert accepted")
except TimeoutException:
    print("no alert")
