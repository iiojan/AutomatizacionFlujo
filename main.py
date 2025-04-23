from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()))
user = "standard_user" 
pwd = "secret_sauce"

personaNombre = "Johan"
personaApellido = "Rodriguez"
personaCodPostal = "116136"

driver.maximize_window()
driver.get('https://www.saucedemo.com/')



driver.find_element(By.ID, "user-name").send_keys(user)
driver.find_element(By.ID, "password").send_keys(pwd)
driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()


carrito = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_link"))
)
carrito.click()

checkout = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))
)
checkout.click()




nombre = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "firstName"))
)
nombre.send_keys(personaNombre)
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(personaApellido)
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(personaCodPostal)
driver.find_element(By.CSS_SELECTOR, "#continue").click()

driver.find_element(By.ID, "finish").click()

time.sleep(5)

driver.find_element(By.ID, "react-burger-menu-btn").click()
logout = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link"))
)
logout.click()
time.sleep(10)


driver.quit()
