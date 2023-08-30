from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def task_1(driver):
    # Grab page title and place title text in answer slot #1
    # Get page title
    web_title = driver.title

    # Select text box to enter answer
    ans_box = driver.find_element(By.ID, "answer1")

    # Input title into text box
    ans_box.send_keys(web_title)

def task_2(driver):
    # Fill out name section of form to be Kilgore Trout
    # Select text box to enter answer
    ans_box = driver.find_element(By.ID, "name")

    # Input answer into text box
    ans_box.send_keys("Kilgore Trout")

def task_3(driver):
    # Set occupation on form to Sci-Fi Author
    # Select dropdown by ID
    occupation = Select(driver.find_element(By.ID, "occupation"))

    # Make selection by value
    occupation.select_by_value("scifiauthor")

def task_4(driver):
    # Count number of blue_boxes on page after form and enter into answer box #4
    # Find and count blue boxes
    boxes = driver.find_elements(By.CLASS_NAME, "bluebox")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer4")
    ans_box.send_keys(len(boxes))

def task_5(driver):
    # Click link that says 'click me'
    # Find and click the link
    link = driver.find_elements(By.LINK_TEXT, "click me")
    driver.click(link)

def task_6(driver):
    # Find red box on its page find class applied to it, and enter into answer box #6
    # Find red box
    redbox = driver.find_elements(By.ID, "redbox")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer6")
    ans_box.send_keys(redbox.get_attribute("class"))

def task_7(driver):
    # Run JavaScript function as: ran_this_js_function() from your Selenium script
    # Run the function
    driver.execute_script("ran_this_js_function();")

def task_8(driver):
    # Run JavaScript function as: got_return_from_js_function() from your Selenium script, take returned value and place it in answer slot #8
    # Run the function to get the value
    answer = driver.execute_script("got_return_from_js_function();")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer8")
    ans_box.send_keys(answer)

def task_9(driver):
    # Mark radio button on form for written book? to Yes
    # Find and click radio button
    driver.find_elements(By.XPATH, "/html/body/form/input[2]").click()

def task_10(driver):
    # Get the text from the Red Box and place it in answer slot #10
    # Find red box
    redbox = driver.find_elements(By.ID, "redbox")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer10")
    ans_box.send_keys(redbox.text)

def task_11(driver):
    # Which box is on top? orange or green -- place correct color in answer slot #11