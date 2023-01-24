#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install selenium 


# In[2]:


pip install webdriver-manager


# In[3]:


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.get("https://newgitlab.great.ufc.br/")

login_box = driver.find_element("name", "user[login]")
password_box = driver.find_element("name", "user[password]")

login_box.send_keys('marciogomes')
password_box.send_keys('#sirius084')

login_box.submit()
password_box.submit()


# In[ ]:




