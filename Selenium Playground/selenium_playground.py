# http://timvroom.com/selenium/playground/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import tasks
import traceback

url = "http://timvroom.com/selenium/playground"

# Create firefox webdriver instance
driver = webdriver.Firefox()

# Navigate to url
driver.get(url)

# Complete tasks
# Make sure to quit driver if an error occurs
try:
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
    tasks.task_11(driver)
    tasks.task_12(driver)
    tasks.task_13(driver)
    tasks.task_14(driver)
    tasks.task_15(driver)
    tasks.task_16(driver)
    tasks.task_17(driver)

    # Check results
    check_results = driver.find_element(By.ID, "checkresults")
    check_results.click()

    # Wait 10 seconds so I can see results
    time.sleep(10)

    # Exit driver
    driver.quit()

except Exception:
    # Print the exception instead of just exiting
    traceback.print_exc()
