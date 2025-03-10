from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import loginInfo
import time

browser = webdriver.Edge()

browser.get("https://x.com/")

time.sleep(3)

login = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div/span/span')

login.click()

time.sleep(3)

userNameInput = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
userNameInput.send_keys("Enter your username")
time.sleep(3)
next1 = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
next1.click()
time.sleep(3)


userPassword = browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
userPassword.send_keys("enter your password")
time.sleep(3)
last_login =browser.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
last_login.click()
time.sleep(5)


searchSmth = browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/div/div[2]/div/input')
searchSmth.send_keys("#search for a tag" + Keys.ENTER)
time.sleep(3)

elements = browser.find_elements(By.CSS_SELECTOR, ".class extensions such as .r-abcd.r-1q2424 vs vs")
time.sleep(3)

for element in elements:
    print("***************************************\n")
    print(element.text)




"""clickSearch = browser.find_element(By.XPATH,'//*[@id="typeaheadDropdown-4"]/div[2]/button')
clickSearch.click()
time.sleep(5)"""



browser.close()



