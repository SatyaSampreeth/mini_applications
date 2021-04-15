#!/usr/bin/env python
# coding: utf-8

# # Desktop Notifier for COVID-19

# In[31]:


from urllib.request import urlopen,Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[32]:


header = {'User-Agent':'Mozilla'}
req = Request('https://www.worldometers.info/coronavirus/country/india/',headers= header)


# In[33]:


html =urlopen(req)


# In[34]:


html.status


# In[35]:


obj = bs(html)


# In[38]:


new_cases=obj.find("li",{"class":"news_li"}).strong.text.split()[0]


# In[45]:


death = list(obj.find('li', {'class':'news_li'}).strong.next_siblings)[1].text.split()[0]


# # Notifier

# In[52]:


notifier = ToastNotifier()


# In[53]:


message = "New Cases - "+ new_cases+"\nDeath - "+death


# In[54]:


message


# In[56]:


notifier.show_toast(title="Covid-19 Update", msg=message, duration =5,icon_path=r"C:\Users\Satya\Desktop\projects\virus.ico")


# In[ ]:




