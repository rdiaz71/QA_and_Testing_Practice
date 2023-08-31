# http://timvroom.com/selenium/playground/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import tasks

url = "http://timvroom.com/selenium/playground"

# Create firefox webdriver instance
driver = webdriver.Firefox()

# Navigate to url
driver.get(url)

# Complete tasks
tasks.task_1(driver)
tasks.task_2(driver)
tasks.task_3(driver)
tasks.task_4(driver)
tasks.task_5(driver)
tasks.task_6(driver)
tasks.task_7(driver)
tasks.task_8(driver)
tasks.task_9(driver)
tasks.task_10(driver)
