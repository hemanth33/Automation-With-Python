from selenium import webdriver
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
    driver.get('https://titan22.com/')
    return driver

def main():
    driver = get_driver()
    
    time.sleep(2)
    
    driver.find_element(by='xpath', value='/html/body/header/div[1]/div[1]/div/div[3]/a[2]').click()
    
    driver.find_element(by='id', value='CustomerEmail').send_keys('ikjjsdhdlxpawfhcys@nbmbb.com')
    
    time.sleep(2)
    
    driver.find_element(by='id', value='CustomerPassword').send_keys('Titan@123')
    
    time.sleep(2)
    
    driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/button').click()
    
    time.sleep(2)
    
    driver.find_element(by='xpath', value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    
main()
    