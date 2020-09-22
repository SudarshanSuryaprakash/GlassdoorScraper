# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import selenium
from selenium import webdriver
import webbrowser
import time
import pandas as pd
from pandas import DataFrame
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

salaries = []
job_employer_names = []
jobs=0
i=0
num_jobs = 10
flag = True



def yoyo():
    get_jobs(num_jobs,jobs,i,flag)
    
    

def progress_printer(jobs,num_jobs):
    print("Progress is {}".format(""+str(jobs) + "/" + str(num_jobs)))

    
    
    

def get_jobs(num_jobs,jobs,i,flag):
    
    url = "https://www.glassdoor.co.uk/Job/uxbridge-data-scientist-jobs-SRCH_IL.0,8_IC3283577_KO9,23.htm?srs=RECENT_SEARCHES"    
    driver.get(url)
    time.sleep(2)
    
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
    

    ######## OBTAINING EMPLOYER NAMES
    
    job_employer_namess = driver.find_elements_by_class_name('jobEmpolyerName')
    for job_employer_name in job_employer_namess:
        if i<=num_jobs:
            print(i)
            job_employer_name = job_employer_name.text
            job_employer_names.append(job_employer_name)
            print(job_employer_name)
            i=i+1
    df1 = DataFrame(job_employer_names)
    print(df1)
    
    ##################################
    
    ######## OBTAINING SALARY

    ########################
    
    job_headers = driver.find_elements_by_class_name('jobHeader')
    for job_header in job_headers:
        progress_printer(jobs, num_jobs)
        if jobs>=num_jobs:
            break
        jobs = jobs+1
        job_header.click()
################### Trying SALARY
        try:
            gray_salary = driver.find_element_by_id("text")
            salaries.append(gray_salary).text
            print(gray_salary).text
            time.sleep(0.5)
        except NoSuchElementException:
            print("FLOP")
            #####################
#MainCol > div:nth-child(1) > ul > li:nth-child(2) > div.jobContainer > div.jobFooter.flex-wrap.css-o853md.e1ewkec0 > div.salaryEstimate.mb-xxsm.css-nq3w9f.pr-xxsm > span

    
    
#a = int(input())

yoyo()

