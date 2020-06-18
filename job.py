import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#chrome  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import json

def getData():
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	 
	driver=webdriver.Chrome(options=chrome_options)

	driver.get('https://www.indeed.co.in/jobs?q=Work+From+Home')
	jobs=driver.find_elements_by_xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')

	text=''
	for i in jobs:
		job=(i.text)
		temp=i.find_element_by_tag_name('h2')
		temp=temp.find_element_by_tag_name('a')
		link='<a href="{}">Link</a>'.format((temp.get_attribute('href')))
		job=job.replace('·Save job·More...','')
		job=job.replace('·Save job','')
		if('Work Abroad' not in job):
			text+='<br><hr>'+job+'<br>'+link+'<br><br><hr>'
	return(text)


print(getData())
