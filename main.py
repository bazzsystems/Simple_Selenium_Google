from http import server
import imp
from re import search
from selenium import webdriver # importing selenium
from selenium.webdriver.common.keys import Keys # importing keys
import time # thats time importing for sleep() command
Path = "C:\chromedriver.exe" # path of webdriver
driver = webdriver.Chrome(Path) # Path means wheres the file

driver.get("https://google.com") #site to open
print(driver.title) # print site title

search = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input") # find xpath path with search virable

search.send_keys("test") # type in the xpath if possible "test"

search.send_keys(Keys.RETURN) # click the RETURN/ENTER button
#function.click() # click at xpath

time.sleep(5) # makes the script pause for 5 sec



driver.quit() # closes the webdriver
