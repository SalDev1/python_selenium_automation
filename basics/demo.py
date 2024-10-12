#Selenimum allows you to scrape data from many different websites allowing to create chat bots , 
# Creating excel sheets + automated scripts and many more. 

from selenium import webdriver  #A driver allowing you to play around with different web browsers
# Webdriver -- Think of it as a machine which runs a program for you. 

from selenium.webdriver.common.keys import Keys  #Gets accessed to action keys in the keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://www.geeksforgeeks.org/')  #Allows you to open up a webpage using driver.

print(driver.title) #Shows you the title of the web page.

# find_element allows to fetch html element based on unique identifiers.
search = driver.find_element(By.TAG_NAME,'input')

# print(driver.page_source) #Brings you the entire source html code of the web page.

search.send_keys('DSA')
search.send_keys(Keys.RETURN)

# Fetching all the articles of DSA from geeksforgeeks.
# Introducing Explicit Waits, handle async / dynamic responses of data.
try:
    # Got the main container
    container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "HomePageSearchModal_homePageSearchModalContainer_modal_container_content__drrYe"))
    )
    # Fetch all the articles present in the container.
    articles = container.find_elements(By.CLASS_NAME, 'SearchModalArticleCard_searchModalArticleCard__x___y')
    for article in articles:
        header = article.find_element(By.CLASS_NAME,'SearchModalArticleCard_searchModalArticleCard_content_heading__hB4a_')
        print(header.text)
finally:
    driver.quit()

# container = driver.find_element(By.CLASS_NAME,'HomePageSearchModal_homePageSearchModalContainer_modal_container_content__drrYe')
# print(container.text)

# time.sleep(5)  #Allows you to delay the execution of the program
# driver.close()