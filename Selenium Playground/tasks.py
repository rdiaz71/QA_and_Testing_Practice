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
    link = driver.find_element(By.LINK_TEXT, "click me")
    link.click()

def task_6(driver):
    # Find red box on its page find class applied to it, and enter into answer box #6
    # Find red box
    redbox = driver.find_element(By.ID, "redbox")

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
    answer = driver.execute_script("return got_return_from_js_function();")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer8")
    ans_box.send_keys(answer)

def task_9(driver):
    # Mark radio button on form for written book? to Yes
    # Find and click radio button
    driver.find_element(By.XPATH, "/html/body/form/input[2]").click()

def task_10(driver):
    # Get the text from the Red Box and place it in answer slot #10
    # Find red box
    redbox = driver.find_element(By.ID, "redbox")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer10")
    ans_box.send_keys(redbox.text)

def task_11(driver):
    # Which box is on top? orange or green -- place correct color in answer slot #11
    # Get the first [top] value from box_order list
    answer = driver.execute_script("return box_order[0]")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer11")
    ans_box.send_keys(answer)

def task_12(driver):
    # Set browser width to 850 and height to 650
    driver.set_window_size(850,650)
    
def task_13(driver):
    # Type into answer slot 13 yes or no depending on whether item by id of ishere is on the page
    # Find item by ID
    answer = driver.find_elements(By.ID, "ishere")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer13")
    if(len(answer)):
        ans_box.send_keys("yes")
    else:
        ans_box.send_keys("no")

def task_14(driver):
    # Type into answer slot 14 yes or no depending on whether item with id of purplebox is visible
    # Find item and attribute
    purplebox = driver.find_element(By.ID, "purplebox")

    # Input answer
    ans_box = driver.find_element(By.ID, "answer14")
    if(purplebox.is_displayed()):
        ans_box.send_keys("yes")
    else:
        ans_box.send_keys("no")

def task_15(driver):
    # Waiting game: click the link with link text of 'click then wait' a random wait will occur (up to 10 seconds) 
    # and then a new link will get added with link text of 'click after wait' - click this new link within 500 ms of it appearing to pass this test
    # Find and click the first link
    link = driver.find_element(By.LINK_TEXT, "click then wait")
    link.click()

    # Continuously search for new link to appear, click when it does
    while(True):
        try:
            second_link = driver.find_element(By.LINK_TEXT, "click after wait")
            second_link.click()
            break
        except:
            continue

def task_16(driver):
    # Click OK on the confirm after completing task 15
    # Switch driver to popup and click ok
    popup = driver.switch_to.alert
    popup.accept()

def task_17(driver):
    # Click the submit button on the form
    # Find and click the box
    submit = driver.find_element(By.ID, "submitbutton")
    submit.click()
