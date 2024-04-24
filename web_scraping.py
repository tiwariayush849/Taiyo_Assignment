#!/usr/bin/env python
# coding: utf-8

# In[115]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd


# In[116]:


service = Service("C:/Users/piyus/Downloads/selenium/chromedriver.exe")

driver =webdriver.Chrome(service = service)
driver.get("https://www.tendersinfo.com/esearch/process?search_text=California+bids")

time.sleep(5)


# In[117]:


tender_Sector = driver.find_elements(By.XPATH, "//tbody/tr/td[2]/a")

# Process each link
for link in tender_Sector:
    print(link.text)  # Print the text of each link


# In[118]:


tender_Summary = driver.find_elements(By.XPATH, "//tbody/tr/td[3]/a")

# Process each link
for link in tender_Summary:
    print(link.text)


# In[119]:


tender_Date = driver.find_elements(By.XPATH, "//tbody/tr/td[4]/a")

# Process each link
for link in tender_Date:
    print(link.text)


# In[120]:


tender_Deadline = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/a")

# Process each link
for link in tender_Deadline:
    print(link.text)


# In[121]:


Tender_result = []
for i in range(len(tender_Date)):
    temporary_data = {
        'tender_Sector': tender_Sector[i].text,
        'tender_Summary': tender_Summary[i].text,
        'tender_Date': tender_Date[i].text,
        'tender_Deadline': tender_Deadline[i].text
    }
    Tender_result.append(temporary_data)
    

    


# In[125]:


df_data = pd.DataFrame(Tender_result)
df_data.to_csv('Tender_scraping_result.csv')


# In[126]:


df_data


# In[ ]:




