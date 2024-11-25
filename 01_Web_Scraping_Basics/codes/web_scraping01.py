from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/login/?next=/dashboard')
    return driver

def clean_text(text):
    """Extract Number from the text"""
    output = text.split(": ")[1]
    return float(output)

def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    
    time.sleep(2)
    
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated'  + Keys.RETURN)
    
    print(driver.current_url)
    
    time.sleep(2)
    
    element = clean_text(driver.find_element(by='xpath', value='/html/body/div[1]/h1[2]').text)
    
    driver.find_element(by='xpath', value='/html/body/nav/div/div/div[1]/a').click()
    
    print(driver.current_url)
    
    time.sleep(2)
    
    return element
    

print(main())
