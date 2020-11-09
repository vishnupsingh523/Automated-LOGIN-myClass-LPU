# Program to LOGIN into the myclass lovelyprofessionaluniversity portal

#1- Firstly, from the selenium import the webdriver
from selenium import webdriver

#2- Use a "variable" to store the webdriver.Choreme()
driver = webdriver.Chrome()

#3 - You can store the URL in some Variable in the string from and then use it in the get() request
driver.get("https://myclass.lpu.in/")

#4 = This is the name of the input element of username in form of that page
# -- You can get this name of ID by searching its ID or NAME in INSPECT ELEMENT(Ctrl + Shift + I)
username = driver.find_element_by_name('i')

#5 - Enter your registration Number here for example. '11912505' ... in string form
username.send_keys('ENTER_Registration_NUMBER')

#6 - This is the name of the input element of username in form of that page
# -- You can get this name of ID by searching its ID or NAME in INSPECT ELEMENT(Ctrl + Shift + I)
password = driver.find_element_by_name('p')

#7 - Enter your PASSWORD here for example. '@Bd123' ... in string form
password.send_keys('Enter_PASSWORD_HERE')

#8 - here find_element_by_xpath() is used to find the particular element with the help of its xpath
# and if you want to get the xpath of it so you can get it by inspecting the element and then right click on the particular element
# then goto the copy and from there you can choose Xpath
loginButton = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')

#9 - this click() function is used to click the Login button 
loginButton.click()
