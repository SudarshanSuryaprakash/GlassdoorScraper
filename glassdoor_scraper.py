#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 05:38:11 2020

@author: sudarshan
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#/html/body/div[15]/div[2]
#/html/body/div[15]/div[2]/span/svg
#modal_main salaryInfoContainer
#SVG_Inline modalcloseIcon


def get_jobs(keyword, num_jobs, verbose, place):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    #driver = webdriver.Chrome(executable_path="/Users/omersakarya/Documents/GitHub/scraping-glassdoor-selenium/chromedriver", options=options)
    driver = webdriver.Chrome()
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.co.uk/Job/web-developer-jobs-SRCH_KO0,13.htm"
    
    driver.get(url)
    jobs = []
    time.sleep(3)
    
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    time.sleep(3)
        

    
    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.
        #try:
            time.sleep(2)
            job_buttons = driver.find_elements_by_class_name("jobHeader")  #jl for Job Listing. These are the buttons we're going to click.
            for job_button in job_buttons:
                if len(jobs) >= num_jobs:
                    break
                print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
                time.sleep(1)
                try:
                    job_button.click()
                except (ElementClickInterceptedException, StaleElementReferenceException):
                    break
                time.sleep(0.5)
                collected_successfully = False
        
                while not collected_successfully:
                    try:
                        company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                        location = driver.find_element_by_xpath('.//div[@class="location"]').text
                        job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                        job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                        collected_successfully = True
                    except:
                        
                        #######time.sleep(5)
                        pass

                try:
                        #salary_estimate = driver.find_element_by_xpath('.//span[@class="gray salary"]').text
                        salary_estimate = driver.find_element_by_xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[4]/span').text
                except NoSuchElementException:
                        salary_estimate = -1 #You need to set a "not found value. It's important."
                    
                try:
                        rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
                except NoSuchElementException:
                        rating = -1 #You need to set a "not found value. It's important."
        
                    #Printing for debugging
                if verbose:
                    print("Job Title: {}".format(job_title))
                    print("Salary Estimate: {}".format(salary_estimate))
                    print("Job Description: {}".format(job_description[:500]))
                    print("Rating: {}".format(rating))
                    print("Company Name: {}".format(company_name))
                    print("Location: {}".format(location))
        
                    #Going to the Company tab...
                    #clicking on this:
                    #<div class="tab" data-tab-type="overview"><span>Company</span></div>
                try:
                    driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
                    try:
                                #<div class="infoEntity">
                                #    <label>Headquarters</label>
                                #    <span class="value">San Francisco, CA</span>
                                #</div>
                        headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                    except NoSuchElementException:
                        headquarters = -1
            
                    try:
                        size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                    except NoSuchElementException:
                        size = -1
            
                    try:
                        founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                    except (NoSuchElementException, StaleElementReferenceException):
                        founded = -1
            
                    try:
                        type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                    except NoSuchElementException:
                        type_of_ownership = -1
            
                    try:
                        industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                    except NoSuchElementException:
                        industry = -1
            
                    try:
                        sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                    except NoSuchElementException:
                        sector = -1
            
                    try:
                        revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                    except NoSuchElementException:
                        revenue = -1
            
                    try:
                        competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                    except NoSuchElementException:
                        competitors = -1
                        
                    time.sleep(0.5)
        
                            
        
                except (NoSuchElementException,ElementClickInterceptedException,StaleElementReferenceException):  #Rarely, some job postings do not have the "Company" tab.
                      if NoSuchElementException:
                          time.sleep(1)       
                          headquarters = -1
                          size = -1
                          founded = -1
                          type_of_ownership = -1
                          industry = -1
                          sector = -1
                          revenue = -1
                          competitors = -1
                      else:
                          #driver.find_element_by_class_name("selected").click()
                          #driver.find_element_by_class_name("SVG_Inline modal_closeIcon").click()
                          #element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "SVG_Inline-svg modal_closeIcon-svg")))
                          #element.click()
                          pass
                    
        
                #time.sleep()
                        
                if verbose:
                    print("Headquarters: {}".format(headquarters))
                    print("Size: {}".format(size))
                    print("Founded: {}".format(founded))
                    print("Type of Ownership: {}".format(type_of_ownership))
                    print("Industry: {}".format(industry))
                    print("Sector: {}".format(sector))
                    print("Revenue: {}".format(revenue))
                    print("Competitors: {}".format(competitors))
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        
                jobs.append({"Job Title" : job_title,
                "Salary Estimate" : salary_estimate,
                "Job Description" : job_description,
                "Rating" : rating,
                "Company Name" : company_name,
                "Location" : location,
                "Headquarters" : headquarters,
                "Size" : size,
                "Founded" : founded,
                "Type of ownership" : type_of_ownership,
                "Industry" : industry,
                "Sector" : sector,
                "Revenue" : revenue,
                "Competitors" : competitors})
                time.sleep(1)
                            #You might 
                            #time.sleep(0.5)
                            
        #except (ElementClickInterceptedException, StaleElementReferenceException):
            #driver.find_element_by_class_name("jobHeader").click()
            #driver.find_element_by_class_name("selected").click()
            #driver.find_element_by_class_name("SVG_Inline modal_closeIcon").click()
            #element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "SVG_Inline-svg modal_closeIcon-svg")))
            #element.click()
            
        
        
                    
                        
                        #add job to jobs
        
                #Clicking on the "next page" button
               # try:
                 #   driver.find_element_by_xpath('.//li[@class="page"]//a').click()
               # except NoSuchElementException:
                 #   print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                #    break
               # time.sleep(5)

            try:
                driver.find_element_by_xpath('.//li[@class="next"]//a').click()
            except (NoSuchElementException, ElementClickInterceptedException):
            #print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
                #driver.find_element_by_class_name("SVG_Inline modal_closeIcon").click()
           # element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "SVG_Inline-svg modal_closeIcon-svg")))
           # element.click()
            #print(element.text)
                
            
                break

        
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.


#This line will open a new chrome window and start the scraping.
#df = get_jobs("data scientist", 5, False)






