from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Website
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Verify login successful
assert "inventory" in driver.current_url

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Go to cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(2)

# Click Checkout
driver.find_element(By.ID, "checkout").click()

# Fill checkout form
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")

driver.find_element(By.ID, "continue").click()

time.sleep(2)

# Finish Purchase
driver.find_element(By.ID, "finish").click()

time.sleep(2)

# Verify Success Message
success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
assert success_message == "Thank you for your order!"

print("Test Passed: Checkout completed successfully")

time.sleep(3)
driver.quit()