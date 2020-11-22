from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys


import time
PATH = "/usr/bin/chromedriver"


chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(chrome_options=chrome_options)


def Glogin(mail, passw):

	driver.get('https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow')
	driver.find_element_by_id("identifierId").send_keys(mail)
	driver.find_element_by_id("identifierNext").click()
	time.sleep(3)
	driver.find_element_by_name("password").send_keys(passw)
	driver.find_element_by_id("passwordNext").click()
	time.sleep(3)

def joinMeetCall(code):
	driver.get("https://meet.google.com/" + code)
	time.sleep(5)
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'd')
	join_butt = WebDriverWait(driver, 6).until(
    	EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Partecipa')]")))
	driver.execute_script("arguments[0].click();", join_butt)

def newTab(url):
	script='window.open("' + url + '","_blank");'
	driver.execute_script(script)

def go(url):
	driver.get(url)

def fullScreen():
	driver.find_element_by_tag_name('body').send_keys(Keys.F11)

def newBackTab(url):
	script='window.open("' + url + '","_blank");'
	driver.execute_script(script)
	time.sleep(3)
	print("done")
	driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
 
def close():
	driver.quit()
