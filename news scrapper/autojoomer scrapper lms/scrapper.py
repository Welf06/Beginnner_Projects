import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

def Login():
      print("Login page reached")
      try:
         username = driver.find_element(by=By.ID, value="username")
         username.send_keys("2021bcs0104")
         password = driver.find_element(by=By.ID, value="password")
         password.send_keys("Redlions@1234")
         submit_Button = driver.find_elements(by=By.ID, value="loginbtn")[0]
         submit_Button.click()
         time.sleep(1)
      except:
         print("Login Failed")
         quit
   
def getAssignments(url):
   
   driver.get(url)

   # check the current link of the page
   if driver.current_url == "https://lms.iiitkottayam.ac.in/login/index.php" or "https://lmsone.iiitkottayam.ac.in/login/index.php":
      Login()


   driver.get(url)
   # Finding the event list which contains all the Assignments
   # code to check if the event list has loaded or not
   try:
      element = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, "calendarwrapper"))
      )
      
      #  cards contain all the info on the assignment
      
      cards = driver.find_elements(by=By.CLASS_NAME, value="card")
      for card in cards:
         assignment = {}
         # finding the title
         card_header = card.find_element(by=By.CLASS_NAME, value="card-header")
         if card.text == '':
            continue
         assignment['heading'] = card_header.text

         # The body of card which contains info
         description = card.find_element(by=By.CLASS_NAME, value="description")
         
         # finding date time
         url_containing_datetime = description.find_element(by=By.TAG_NAME, value="a").get_attribute('href')
         assignment['datetime'] = str(url_containing_datetime[-10: ])
         
         # finding description if any
         desc = description.find_elements(by=By.CLASS_NAME, value="mt-1")[-2].text
         if desc != 'Course event':
            assignment['description'] = desc
         # finding course name
         assignment['course name'] = description.find_elements(by=By.CLASS_NAME, value="mt-1")[-1].text
         # Finding submission link
         card_footer = card.find_element(by=By.CLASS_NAME, value="card-footer")
         assignment['submission link'] = card_footer.find_element(by=By.TAG_NAME, value="a").get_attribute('href')
         return assignment
   finally:
      driver.close()

calendarLinkLMS = "https://lms.iiitkottayam.ac.in/calendar/view.php"
calendarLinkLMSOne = "https://lmsone.iiitkottayam.ac.in/calendar/view.php"
assigments = getAssignments(calendarLinkLMS)
print(assigments)