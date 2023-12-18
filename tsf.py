from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select
import time  
import unittest


def SeleniumSetUp():
    driver = webdriver.Firefox()
    #website to test
    driver.get("https://thesparksfoundationsingapore.org") 
    print("\t-"*8)
    print("\tTitle of page: ",driver.title) 
    print("\t-"*8)
    time.sleep(2)

    print("\tTest Case 1") 
    try:
        #check if the logo of homepage exist
        driver.find_element(By.XPATH,"//img[@src='/images/logo_small.png']") 
        print("\tLogo found")
    except NoSuchElementException: 
        #if Logo not exist  
        print("Logo not found")
    try:
        #check if Navbar of homepage exist
        driver.find_element(By.TAG_NAME,"nav") 
        print("\tNavBar found")
    except NoSuchElementException:
        #if NavBar not exist 
        print("\tNavBar not found")  
        time.sleep(2)
    try:
        print("\nTest Case 2")
        about_us = driver.find_element(By.LINK_TEXT,"About Us")
        about_us.click()
        #navigate to the News page remotely
        aboutus_content = driver.find_element(By.LINK_TEXT,"News")
        aboutus_content.click() 
        time.sleep(8);
        driver.back() 
    except NoSuchElementException:
        print("About-us not found") 
    try: 
        print("\nTest Case 3")
        policy_code = driver.find_element(By.LINK_TEXT,"Policies and Code") 
        policy_code.click()  
        policy_content = driver.find_element(By.LINK_TEXT,"Policies") 
        policy_content.click() 
        contents = driver.find_elements(By.TAG_NAME,"p")
        for content in contents:
            text = content.text 
        print(text)  
        time.sleep(10)
        driver.back()
    except NoSuchElementException:
        print("Policy and Code not found") 
    try:
        print("\nTest Case 4") 
        links = driver.find_element(By.LINK_TEXT,"LINKS") 
        links.click()

        link_ai = driver.find_element(By.LINK_TEXT,"AI in Education") 
        link_ai.click()  
        vist_link = driver.find_element(By.LINK_TEXT,"Visit LINKS @TSF")
        vist_link.click() 
        original_window = driver.current_window_handle
        driver.switch_to.window(original_window) 
        driver.back()

    except NoSuchElementException: 
        print("No Links found")
    try: 
        time.sleep(10)
        print("\nTest Case 5")
        join_us = driver.find_element(By.LINK_TEXT,"Join Us")
        join_us.click()
        joinus_content = driver.find_element(By.LINK_TEXT,"Why Join Us") 
        joinus_content.click()

        driver.find_element(By.NAME, "Name").send_keys("Usernametest01")
        driver.find_element(By.NAME, "Email").send_keys("usernametest01@gmail.com")  
        select_element = driver.find_element(By.CLASS_NAME, "form-control")  
        select = Select(select_element)
        select.select_by_visible_text("Intern") 

        print("\nTesting Finished!")  
        print("\nThank you!")

        time.sleep(10)
        driver.quit()
    except NoSuchElementException:
        print("Join Us not found")

#Test the function 
SeleniumSetUp()
