
# coding: utf-8

# In[1]:


import pandas as pd
import time
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path = 'C:\\Users\\lenovo\\Desktop\\scrapping\\chromedriver_win32\\chromedriver.exe')


# In[2]:


twi = driver.get('https://twitter.com/login')
time.sleep(3)
password = driver.find_element_by_class_name('js-password-field')
password.send_keys('*********')
user_name = driver.find_element_by_class_name('js-username-field.email-input.js-initial-focus')
user_name.send_keys('*********')
but = driver.find_element_by_class_name('submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
but.click()


# In[3]:


space_agency=['isro','nasa','spacex']
for space in space_agency:
    x=0
    y=3000
    url = 'https://twitter.com/'+space
    site = driver.get(url)
    dataset=set()
    time.sleep(8)
    for _ in range(0,6):
        m=driver.find_elements_by_class_name('css-1dbjc4n.r-18u37iz.r-thb0q2')
        for i in m:
            ul = i.text.split('\n')
            if len(ul)>=7:
                dataset.add(i.text)
        driver.execute_script("window.scrollTo("+str(x)+","+str(y)+")")
        x=y
        y+=3000
        time.sleep(8)
    con=1
    for i in dataset:
        li=i.split('\n')
        name=li[0]
        twitter_name=li[1]
        date = li[3]
        likes=li[-1]
        retweet = li[-2]
        comment = li[-3]
        content = li[4:len(li)-3]
        #print(name+ twitter_name+likes)
        text=''
        for j in content:
            text+=j
        text=text.encode("utf-8")    
        with open('twitter_data.csv',mode='a') as file:
            if con==1:
                name1=['Name','Twitter name','Tweet','Date','Likes','Comment','Retweet']
                write = csv.DictWriter(file,fieldnames = name1)
                write.writeheader()
                #print(str(name)+str(twitter_name)+str(text)+str(date)+str(likes)+str(comment)+str(retweet))
                write.writerow({'Name':name,'Twitter name':twitter_name,'Tweet':text,'Date':date,'Likes':likes,'Comment':comment,'Retweet':retweet})
                con=2
            else:
                name1=['Name','Twitter name','Tweet','Date','Likes','Comment','Retweet']
                write = csv.DictWriter(file,fieldnames = name1)
                #print(str(name)+str(twitter_name)+str(text)+str(date)+str(likes)+str(comment)+str(retweet))
                write.writerow({'Name':name,'Twitter name':twitter_name,'Tweet':text,'Date':date,'Likes':likes,'Comment':comment,'Retweet':retweet})
        file.close() 
     
    

