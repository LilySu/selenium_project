from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from parsel import Selector
import time
import rite_aid_parameter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('..\\chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.riteaid.com/pharmacy/covid-qualifier')

dateOfBirth = driver.find_element_by_id('dateOfBirth')
dateOfBirth.send_keys(rite_aid_parameter.your_date_of_birth) # parameters.linkedin_username

occupation = driver.find_element_by_name('occupationName')
occupation.click()
time.sleep(0.5)
occupation.send_keys(rite_aid_parameter.your_occupation)
time.sleep(0.5)
occupation.send_keys(Keys.TAB)

city = driver.find_element_by_name('city')
city.send_keys(rite_aid_parameter.your_city)

medicalCondition = driver.find_element_by_name('medicalConditionName')
medicalCondition.click()
time.sleep(0.5)
medicalCondition.send_keys(rite_aid_parameter.your_medical_condition)
time.sleep(0.5)
medicalCondition.send_keys(Keys.TAB)

state = driver.find_element_by_name('eligibility_state')
state.send_keys(rite_aid_parameter.your_state)
time.sleep(0.5)
state.send_keys(Keys.TAB)

zipcode = driver.find_element_by_name('zip')
zipcode.send_keys(rite_aid_parameter.your_zipcode)
zipcode.send_keys(Keys.ENTER)

# next_1 = driver.find_element_by_id('continue')
# next_1.click()

time.sleep(4)
# c = driver.find_element_by_xpath("//button[text()='Continue']")
# c = driver.find_element_by_id('learnmorebttn')
c = driver.find_element_by_class_name('error-modal___learnmrebtn')
c.click()
# WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CLASS_NAME, 'error-modal___learnmrebtn'))).click()

store = driver.find_element_by_class_name('cmp-button')
print(store)

for a in driver.find_elements_by_class_name('cmp-button'):
    print(a.get_attribute('href'))


# None
# None
# None
# None
# https://photo.riteaid.com/
# None
# None
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
# https://www.riteaid.com/pharmacy/apt-scheduler#
s