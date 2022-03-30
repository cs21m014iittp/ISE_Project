from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

ser = Service('C:\\Users\\ACER\\Desktop\\padhai\\tirupati\\ise\\ISE_Project\\chromedriver.exe')
#op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser)
url = 'https://play.google.com/store/apps/details?id=com.cricbuzz.android.vernacular&showAllReviews=true'
driver.get(url)
sleep(5)


if __name__ == '__main__':

	mysoup = BeautifulSoup(driver.page_source, "html.parser")
	review_list = []

	"""
	while len(review_list)<10:
	    
	    review_source = mysoup.find_all('div',{'class','UD7Dzf'})

	    for review in review_source:
	        review_list.append(review.get_text())
	        
	    print(review_list)
	    
	    for i in range(0,3):
	        driver.execute_script("window.scrollTo(%d,%d)"%(696*i,696*(i+1)))
	        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	        
	    try:
	        show_more_btn = driver.find_element_by_xpath("/html/body/div[1]/div[4]/c-wiz[5]/div/div[2]/div/div/main/div/div[1]/div[2]/div[2]/div")
	        show_more_btn.click()
	        
	    except:
	        break
	    """
	i=0
	while len(review_list)<10:
		for i in range(8):
			actions= ActionChains(driver)
			actions.send_keys(Keys.END).perform()
			sleep(1)

		try: 
			#class names U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d
			driver.findElement(By.class_name("U26fgb O0WRkf oG5Srb C0oVfc n9lfJ M9Bg4d")).click()
			print("button found")
		except:
			print("button not found")
			break