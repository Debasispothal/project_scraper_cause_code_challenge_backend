
# coding: utf-8

# In[1]:


import pandas as pd
import time
from selenium.webdriver.common.keys import Keys


# In[2]:


from bs4 import BeautifulSoup


# In[3]:


from selenium import webdriver


# In[4]:


driver = webdriver.Chrome(executable_path = 'chromedriver.exe')


# In[5]:


driver.get('https://www.linkedin.com')
sign_in = driver.find_element_by_class_name('nav__button-secondary')
sign_in.click()
time.sleep(5)
user = driver.find_element_by_id('username')
user.send_keys('debasihpothal@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('*********')
but = driver.find_element_by_xpath('//*[@type="submit"]')
but.click()


# In[82]:


driver.get('https://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys('site:linkedin.com/in/ AND "Software developer" AND "India"')


# In[83]:


search.send_keys(Keys.RETURN)


# In[86]:


url=[]
div = driver.find_elements_by_class_name('r')
for i in div:
    m=i.find_element_by_css_selector('a').get_attribute('href')
    #print(m)
    url.append(m)


# In[85]:


from parsel import Selector
import csv


# In[12]:


con=1
for m in range(0,5):
    #con=1
    for i in url:
        x=i
        site = driver.get(x)
        sel = Selector(text = driver.page_source)
        name = sel.xpath('//*[starts-with(@class,"inline t-24 t-black t-normal break-words")]/text()').extract_first()
        designation = sel.xpath('//*[starts-with(@class,"mt1 t-18 t-black t-normal")]/text()').extract_first()
        location = sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal inline-block")]/text()').extract_first()
        with open('solution.csv',mode='a') as file:
            if con==1:
                con=4
                name1 = ['Name','Designation','Location','Linkedin url']
                write = csv.DictWriter(file,fieldnames = name1)
                write.writeheader()
                if name and designation!="" and location!="":
                    write.writerow({'Name':name,'Designation':designation,'Location':location,'Linkedin url':x})
            #print(con)
            else:
                name1 = ['Name','Designation','Location','Linkedin url']
                write = csv.DictWriter(file,fieldnames = name1)
                if name and designation!="" and location!="":
                    write.writerow({'Name':name,'Designation':designation,'Location':location,'Linkedin url':x})
        file.close()
    driver.get('https://www.google.com')    
    search = driver.find_element_by_name('q')
    search.send_keys('site:linkedin.com/in/ AND "Software developer" AND "India"')
    search.send_keys(Keys.RETURN)
    p=0
    while p<=m:
        link = driver.find_element_by_link_text('Next')
        link.click()
        p+=1
    url=[]
    div = driver.find_elements_by_class_name('r')
    for i in div:
        m=i.find_element_by_css_selector('a').get_attribute('href')
        #print(m)
        url.append(m)

