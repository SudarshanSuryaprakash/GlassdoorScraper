#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 02:05:25 2020

@author: sudarshan
"""
import pandas as pd

df = pd.read_csv("/Users/sudarshan/Documents/Python/Data_Science_Projects/Glassdoor/glassdoor_webDev.csv")

#salary parsing


#df = df[df['Salary Estimate'] != '-1']
df = df.drop_duplicates(subset = 'Company Name', keep='first',inplace=False)

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kp = salary.apply(lambda x:x.replace('K','').replace('£',''))
emp_remove = minus_kp.apply(lambda x:x.replace("Employer Provided Salary:", ""))
dol_remove = emp_remove.apply(lambda x: x.replace('$',''))



df['min_salary'] = dol_remove.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = dol_remove.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#company name text only

df['Company_txt'] = df.apply(lambda x: x['Company Name'][:-3], axis = 1)

df.Company_txt.value_counts()


#age of company
df['age'] = df['Founded'].apply(lambda x: 2020-x if x!= -1 else -1)

#parsing of job description (python, etc)
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

def seniority(title):
    arr=['senior','sr','lead','principal']
    arr1=['junior','jr','intern']
    for ar in arr:
        if ar in title.lower().split():
            return 'senior'
    for al in arr1:
        if al in title.lower().split():
            return "junior"
    return 'na'
    
df['seniority']=df['Job Title'].apply(seniority)

#Job Description Length
df['desc-len'] = df['Job Description'].apply(lambda x: len(x))

#Competitor count
df['comp_count'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x!='-1' else 0)

df.to_csv('/Users/sudarshan/Documents/Python/Data_Science_Projects/Glassdoor/cleaned_data.csv')
    