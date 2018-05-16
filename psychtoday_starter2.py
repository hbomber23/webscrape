from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
#from db import Review
from datetime import date
import time
import csv
import re



driver = webdriver.Chrome(r'C:\Users\Henry\Downloads\chromedriver.exe')

# Windows users need to open the file using 'wb'
# csv_file = open('reviews.csv', 'wb')
csv_file = open('BX2_therapists_11.csv', 'w')
writer = csv.writer(csv_file)

docscrape_dict={}


try:

	for i in range (1,191, 20):
		driver.get('https://www.psychologytoday.com/us/therapists/ny/bronx?sid=1526135942.8292_9444&rec_next=' + str(i))
		#driver.get('https://www.psychologytoday.com/us/therapists/ny/brooklyn?page' + str(i))
		#https://www.psychologytoday.com/us/therapists/ny/new-york-county
		#https://www.psychologytoday.com/us/therapists/ny/staten-island
		#https://www.psychologytoday.com/us/therapists/ny/bronx
		
		print('-#########################################getting page' + str(i))
		doctorslist=[]
		therapist_listing = driver.find_elements_by_xpath('//div[@class="result-row normal-result row"]')
	
		for j in range(0, len(therapist_listing)):
			doctorslist.append(therapist_listing[j].get_attribute('data-profile-url'))

		for weburl in doctorslist:
			time.sleep(1)
			driver.get(weburl)
	
			docname = driver.find_element_by_xpath('//div[2]/div[2]/div[1]/div[1]/h1')
			docscrape_dict['docname'] = docname.text
			
			emp_title=[]
			titles = driver.find_elements_by_xpath('//div[2]/div[2]/div[1]/div[1]/div/h2/span[*]/button/span')
			for title in titles:
				emp_title.append(title.text)
			title_string='#'.join(emp_title)
			docscrape_dict['titles'] = title_string
			
			emp_special=[]
			specialties = driver.find_elements_by_xpath('//div/div[2]/div[2]/div[1]/div/ul/li[.]')
			for special in specialties:
				emp_special.append(special.text)
			specialties_string='#'.join(emp_special)
			docscrape_dict['specialties'] = specialties_string
			
			emp_cost=[]
			costscale = driver.find_elements_by_xpath('//div/div[1]/div[5]/ul/li[*]')
			for cost in costscale:
				emp_cost.append(cost.text)
				break
			cost_string='#'.join(emp_cost)
			docscrape_dict['cost'] = cost_string

			
			emp_year=[]
			years = driver.find_elements_by_xpath('//div/div[1]/div[4]/ul/li[*]')
			for year in years:
				emp_year.append(year.text)
				break
			year_string='#'.join(emp_year)
			docscrape_dict['year'] = year_string
			
			
			emp_method=[]
			methods = driver.find_elements_by_xpath('//div/div[2]/div[4]/div[1]/div/ul/li[*]/button/span')
			for method in methods:
				emp_method.append(method.text)
			method_string='#'.join(emp_method)
			docscrape_dict['method'] = method_string
			
			emp_zip=[]
			#zips = driver.find_elements_by_xpath('//div/div/span[@itemprop="postalcode"]')
			
			zips = driver.find_elements_by_xpath('//div[@class="address address-rank-1"]/div[@class="location-address-phone"]/span[@itemprop="postalcode"]')
			
			#zips = driver.find_element_by_xpath('//div[@class="address address-rank-1"]/div[@class="location-address-phone"]/span[@itemprop="postalcode"]')
			
			#zips = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div/div[1]/span[3]')
			
			#zips = driver.find_elements_by_xpath('//div/div[2]/div[1]/div/div/div[1]/span[3]')
			for zip in zips:
				emp_zip.append(zip.text)
				break
			zip_string='#'.join(emp_zip)

			docscrape_dict['zip'] = zip_string
			
			writer.writerow(docscrape_dict.values())
	time.sleep(2)
	
except Exception as e:
	print(e)
	csv_file.close()
	#driver.close()
	
	