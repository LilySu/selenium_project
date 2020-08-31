import parameters
from time import sleep
from selenium import webdriver


def login_to_linkedin():
    driver = webdriver.Chrome('C:\\Users\\lilyx\\bin\\chromedriver')
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    username = driver.find_element_by_name('session_key')
    username.send_keys(parameters.linkedin_username)
    sleep(3)

    password = driver.find_element_by_name('session_password')
    password.send_keys(parameters.linkedin_password)
    sleep(1.5)

    sign_in_button = driver.find_element_by_class_name('login__form_action_container')# sign - in -form__submit - button ')
    sign_in_button.click()
    sleep(2.5)
    return driver