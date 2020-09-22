#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:15:03 2020

@author: sudarshan
"""


import glassdoor_scraper as gs
import pandas as pd

keyword = "web-development"
place = 'london'
num_jobs = 2500
df = gs.get_jobs(keyword, num_jobs, False, place)
print(df)
df.to_csv('/Users/sudarshan/Documents/Python/glassdoor_webDev.csv')

#/Users/sudarshan/.spyder-py3/


#url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'