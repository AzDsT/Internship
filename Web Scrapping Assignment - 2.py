#!/usr/bin/env python
# coding: utf-8

# # Question 4 Scrape data of first 100 sunglasses listings on flipkart.com. You have to scrape four attributes:

# 1. Brand
# 
# 2. Product Description
# 
# 3. Price

# In[199]:


get_ipython().system('pip install selenium')


# In[200]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[201]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[202]:


url = "https://www.flipkart.com/"
driver.get(url)


# In[203]:


search_glasses = driver.find_element_by_class_name('_3704LK')
search_glasses


# In[204]:


search_glasses.send_keys("Sunglasses")


# In[207]:


search_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
search_btn


# In[208]:


search_btn.click()


# In[211]:


Brandname_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
len(Brandname_tags)
Brandname_tags[0:40]
brand_name1 = []
for i in Brandname_tags:
    brand_name1.append(i.text)
len(brand_name1)
brand_name1[0:40]


# In[214]:


title_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
# len(title_tags)
# title_tags#[0:40]
brand_info1 = []
for i in title_tags:
    brand_info1.append(i.text)
# len(brand_info1)
brand_info1[0:50]


# In[216]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags[0:40]
price_list1 = []
for i in price_tags:
    price_list1.append(i.text)
price_list1[0:40]


# In[217]:


len(brand_name1), len(brand_info1), len(price_list1)


# In[218]:


product1=pd.DataFrame()
product1['Brand Name'] = brand_name1
product1['Product Description'] = brand_info1
product1['Product Price'] = price_list1
product1


# In[224]:


Brandname_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
len(Brandname_tags)
Brandname_tags
brand_name2 = []
for i in Brandname_tags:
    brand_name2.append(i.text)
len(brand_name)
brand_name[0:40]


# In[225]:


title_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
len(title_tags)
title_tags[0:40]
brand_info2 = []
for i in title_tags:
    brand_info2.append(i.text)
len(brand_info)
brand_info[0:100]


# In[226]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags #[0:100]
price_list2 = []
for i in price_tags:
    price_list2.append(i.text)
price_list#[0:100]


# In[227]:


product2=pd.DataFrame()
product2['Brand Name'] = brand_name2
product2['Product Description'] = brand_info2
product2['Product Price'] = price_list2
product2


# In[228]:


Brandname_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
len(Brandname_tags)
Brandname_tags
brand_name3 = []
for i in Brandname_tags:
    brand_name3.append(i.text)
len(brand_name)
brand_name[0:20]


# In[229]:


title_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
len(title_tags)
title_tags[0:40]
brand_info3 = []
for i in title_tags:
    brand_info3.append(i.text)
len(brand_info)
brand_info[0:20]


# In[230]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags #[0:100]
price_list3 = []
for i in price_tags:
    price_list3.append(i.text)
price_list[0:20]


# In[241]:


product3=pd.DataFrame()
product3['Brand Name'] = brand_name3
product3['Product Description'] = brand_info3
product3['Product Price'] = price_list3
product3[0:20]


# In[243]:


# price_list = [price_list1,price_list2,price_list3]
# brand_info = [brand_info1,brand_info2,brand_info3]
# brand_name=[brand_name1,brand_name2,brand_name3,]
# frames = [brand_name,brand_info,price_list]

# products=pd.DataFrame()
# products['Brand Name'] = brand_name
# products['Product Description'] = brand_info
# products['Product Price'] = price_list
# products

# frames = ["product1"," product2", "product3"]
#result = pd.concat(frames)
# result = pd.concat(frames, keys=["Brand Name", "Product Description", "Product Price"])


# # Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:

# Q5: Scrape 100 reviews data from flipkart.com for iphone11 phone. You have to go the link:
# https://www.flipkart.com/apple-iphone-11-black-64-gb-includes- earpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC
# TSVZAXUHGREPBFGI&marketplace.
# 
# As shown in the above page you have to scrape the tick marked attributes.These are:
# 
# 1. Rating
# 
# 2. Review summary
# 
# 3. Full review
# 
# 4. You have to scrape this data for first 100 reviews.

# In[29]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[4]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[5]:


url = "https://www.flipkart.com/apple-iphone-11-black-64-gb-includes-%20earpods-poweradapter/p/itm0f37c2240b217?pid=MOBFKCTSVZAXUHGR&lid=LSTMOBFKC%20TSVZAXUHGREPBFGI&marketplace."
driver.get(url)


# 1. Rating

# In[32]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list1 =[]
for i in rating_tags:
     rating_list1.append(i.text)    
rating_list1  


# In[33]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list2 =[]
for i in rating_tags:
     rating_list2.append(i.text)    
rating_list2  


# In[36]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list3 =[]
for i in rating_tags:
     rating_list3.append(i.text)    
rating_list3  


# In[37]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list4 =[]
for i in rating_tags:
     rating_list4.append(i.text)    
rating_list4


# In[38]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list5 =[]
for i in rating_tags:
     rating_list5.append(i.text)    
rating_list5


# In[39]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list6 =[]
for i in rating_tags:
     rating_list6.append(i.text)    
rating_list6


# In[40]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list7 =[]
for i in rating_tags:
     rating_list7.append(i.text)    
rating_list7


# In[41]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list8 =[]
for i in rating_tags:
     rating_list8.append(i.text)    
rating_list8


# In[42]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list9 =[]
for i in rating_tags:
     rating_list9.append(i.text)    
rating_list9


# In[44]:


rating_tags = driver.find_elements_by_xpath('//div[@class="_3LWZlK _1BLPMq"]')

rating_list10 =[]
for i in rating_tags:
     rating_list10.append(i.text)    
rating_list10


# 2. Review summary

# In[46]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list1 =[]
for i in review_summary_tags:
     review_summary_list1.append(i.text)    
review_summary_list1


# In[47]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list2 =[]
for i in review_summary_tags:
     review_summary_list2.append(i.text)    
review_summary_list2


# In[48]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list3 =[]
for i in review_summary_tags:
     review_summary_list3.append(i.text)    
review_summary_list3


# In[49]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list4 =[]
for i in review_summary_tags:
     review_summary_list4.append(i.text)    
review_summary_list4


# In[50]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list5 =[]
for i in review_summary_tags:
     review_summary_list5.append(i.text)    
review_summary_list5


# In[51]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list6 =[]
for i in review_summary_tags:
     review_summary_list6.append(i.text)    
review_summary_list6


# In[52]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list7 =[]
for i in review_summary_tags:
     review_summary_list7.append(i.text)    
review_summary_list7


# In[55]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list8 =[]
for i in review_summary_tags:
     review_summary_list8.append(i.text)    
review_summary_list8


# In[56]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list9 =[]
for i in review_summary_tags:
     review_summary_list9.append(i.text)    
review_summary_list9


# In[57]:


review_summary_tags = driver.find_elements_by_xpath('//p[@class="_2-N8zT"]')

review_summary_list10 =[]
for i in review_summary_tags:
     review_summary_list10.append(i.text)    
review_summary_list10


# 3.Full review

# In[63]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list1 =[]
for i in full_review_tags:
     full_review_list1.append(i.text)    
full_review_list1



# In[64]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list2 =[]
for i in full_review_tags:
     full_review_list2.append(i.text)    
full_review_list2


# In[65]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list3 =[]
for i in full_review_tags:
     full_review_list3.append(i.text)    
full_review_list3


# In[66]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list4 =[]
for i in full_review_tags:
     full_review_list4.append(i.text)    
full_review_list4


# In[67]:


full_review_tags = driver.find_elements_by_xpath('//div[@ class=""]')

full_review_list5 =[]
for i in full_review_tags:
     full_review_list5.append(i.text)    
full_review_list5


# In[68]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list6 =[]
for i in full_review_tags:
     full_review_list6.append(i.text)    
full_review_list6


# In[69]:


full_review_tags = driver.find_elements_by_xpath('//div[@ class=""]')

full_review_list7 =[]
for i in full_review_tags:
     full_review_list7.append(i.text)    
full_review_list7


# In[70]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list8 =[]
for i in full_review_tags:
     full_review_list8.append(i.text)    
full_review_list8


# In[71]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list9 =[]
for i in full_review_tags:
     full_review_list9.append(i.text)    
full_review_list9


# In[72]:


full_review_tags = driver.find_elements_by_xpath('//div[@class=""]')

full_review_list10 =[]
for i in full_review_tags:
     full_review_list10.append(i.text)    
full_review_list10


# # Q6: Scrape data for first 100 sneakers you find when you visit flipkart.com andsearch for “sneakers” in the search field
# 

# You have to scrape 4 attributes of each sneaker:
# 
# 1. Brand
# 
# 2. Product Description
# 
# 3. Price

# In[1]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


# In[2]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[3]:


url="https://www.flipkart.com/"
driver.get(url)


# In[4]:


search_sneakers = driver.find_element_by_class_name("_3704LK")
search_sneakers


# In[5]:


search_sneakers.send_keys("sneakers")


# In[6]:


search_btn = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button")        
search_btn


# In[7]:


search_btn.click()


# In[9]:


Brand_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
Brand_tags 
brand_name1 = []
for i in Brand_tags:
    brand_name1.append(i.text)
brand_name1


# In[10]:


productdescription_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
productdescription_tags 
product_description1 = []
for i in productdescription_tags:
    product_description1.append(i.text)
product_description1[0:40]


# In[11]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags 
price1 = []
for i in price_tags:
    price1.append(i.text)
price1


# In[12]:


Brand_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
Brand_tags 
brand_name2 = []
for i in Brand_tags:
    brand_name2.append(i.text)
brand_name2


# In[13]:


productdescription_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa _2-ICcC"]')
productdescription_tags 
product_description2 = []
for i in productdescription_tags:
    product_description2.append(i.text)
product_description2[0:40]


# In[14]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags 
price2 = []
for i in price_tags:
    price2.append(i.text)
price2


# In[15]:


Brand_tags = driver.find_elements_by_xpath('//div[@class="_2WkVRV"]')
Brand_tags 
brand_name3 = []
for i in Brand_tags:
    brand_name3.append(i.text)
brand_name3[0:20]


# In[17]:


productdescription_tags = driver.find_elements_by_xpath('//a[@class="IRpwTa"]')
productdescription_tags 
product_description3 = []
for i in productdescription_tags:
    product_description3.append(i.text)
product_description3[0:20]


# In[18]:


price_tags = driver.find_elements_by_xpath('//div[@class="_30jeq3"]')
price_tags 
price3 = []
for i in price_tags:
    price3.append(i.text)
price3[0:20]


# # Q7: Go to the link - https://www.myntra.com/shoes
# Set Price filter to “Rs. 7149 to Rs. 14099 ” , Color filter to “Black”
# And then scrape First 100 shoes data you get. The data should include “Brand” of the shoes , Short Shoe
# description, price of the shoe

# In[17]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[18]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[19]:


url="https://www.myntra.com/shoes"
driver.get(url)


# In[20]:


search_sneakers = driver.find_element_by_class_name("desktop-searchBar")
search_sneakers


# In[21]:


search_sneakers.send_keys("Sneakers")


# In[22]:


search_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/header/div[2]/div[3]/a/span')
search_btn


# In[23]:


search_btn.click()


# In[24]:


price_check = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[4]/ul/li[2]/label/div')


# In[25]:


price_check.click()


# In[26]:


color_check = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/main/div[3]/div[1]/section/div/div[5]/ul/li[2]/label/div')


# In[27]:


color_check.click()


# In[29]:


brand_tags = driver.find_elements_by_xpath('//h3[@class="product-brand"]')
brand_tags 
brand1 = []
for i in brand_tags:
    brand1.append(i.text)
brand1


# In[30]:


descr_tags = driver.find_elements_by_xpath('//h4[@class="product-product"]')
descr_tags 
short_descr1 = []
for i in descr_tags:
    short_descr1.append(i.text)
short_descr1


# In[31]:


price_tags = driver.find_elements_by_xpath('//div[@class="product-price"]')
price_tags 
price1 = []
for i in price_tags:
    price1.append(i.text)
price1


# In[32]:


len(brand1), len(short_descr1), len(price1)


# In[33]:


product1=pd.DataFrame()
product1['Brand Name'] = brand1
product1['Short Description'] = short_descr1
product1['Product Price'] = price1
product1


# In[34]:


brand_tags = driver.find_elements_by_xpath('//h3[@class="product-brand"]')
brand_tags 
brand2 = []
for i in brand_tags:
    brand2.append(i.text)
brand2


# In[35]:


descr_tags = driver.find_elements_by_xpath('//h4[@class="product-product"]')
descr_tags 
short_descr2 = []
for i in descr_tags:
    short_descr2.append(i.text)
short_descr2


# In[36]:


price_tags = driver.find_elements_by_xpath('//div[@class="product-price"]')
price_tags 
price2 = []
for i in price_tags:
    price2.append(i.text)
price2


# In[37]:


len(brand2), len(short_descr2), len(price2)


# In[38]:


product2=pd.DataFrame()
product2['Brand Name'] = brand2
product2['Short Description'] = short_descr2
product2['Product Price'] = price2
product2


# # Q8: Go to webpage https://www.amazon.in/
# Enter “Laptop” in the search field and then click the search icon.
# Then set CPU Type filter to “Intel Core i7” and “Intel Core i9” 

# After setting the filters scrape first 10 laptops data. You have to scrape 3 attributesfor each laptop:
# 
# 1. Title
# 2. Ratings
# 3. Price

# In[7]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[8]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[9]:


url="https://www.amazon.in/"
driver.get(url)


# In[27]:


search_laptop = driver.find_element_by_id("twotabsearchtextbox")
     
search_laptop


# In[28]:


search_laptop.send_keys("laptop")


# In[31]:


search_btn = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_btn


# In[32]:


search_btn.click()


# In[33]:


ic7_check = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[11]/span/a/div/label/i')


# In[34]:


ic7_check.click()


# In[36]:


title_tags = driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
title_tags 
title1 = []
for i in title_tags:
    title1.append(i.text)
title1[0:10]


# In[60]:


rating_tags = driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]')
rating_tags 
rating1 = []
for i in rating_tags:
    rating1.append(i.text)
rating1[0:10]


# In[61]:


price_tags = driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
price_tags 
price1 = []
for i in price_tags:
    price1.append(i.text)
price1[0:10]


# In[62]:


ic9_check = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[6]/ul[4]/li[12]/span/a/div/label/i')


# In[63]:


ic9_check.click()


# In[64]:


title_tags = driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
title_tags 
title2 = []
for i in title_tags:
    title2.append(i.text)
title2[0:10]


# In[68]:


rating_tags = driver.find_elements_by_xpath('//div[@class="a-row a-size-small"]/span')
rating_tags 
rating2 = []
for i in rating_tags:
    rating2.append(i.text)
rating2[0:10]


# In[69]:


price_tags = driver.find_elements_by_xpath('//span[@class="a-price-whole"]')
price_tags 
price2 = []
for i in price_tags:
    price2.append(i.text)
price2[0:10]


# # Q9: Write a python program to scrape data for first 10 job results for Data Scientist Designation in Noida location. You have to scrape company name, No. of days ago when job was posted, Rating of the company.

# In[42]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[43]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[44]:


url = "https://www.ambitionbox.com/"
driver.get(url)


# In[45]:


search_job = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div/div/span/input")
search_job


# In[46]:


search_job.send_keys("Data Scientist")


# In[48]:


search_btn = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[1]/div/div/div/button/span")
search_btn


# In[49]:


search_btn.click()


# In[50]:


search_loc = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/input")
search_loc


# In[51]:


search_loc.send_keys("Noida")


# In[57]:


name_tags = driver.find_elements_by_xpath('//a[@class="title noclick"]')
name_tags 
name = []
for i in name_tags:
    name.append(i.text)
name[0:10]


# # Q10: Write a python program to scrape the salary data for Data Scientist designation.
# You have to scrape Company name, Number of salaries, Average salary, Minsalary, Max Salary.

# In[65]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[66]:


driver = webdriver.Chrome(r'C:\Users\Turgut\Desktop\chromedriver_win32\chromedriver.exe')


# In[67]:


url = "https://www.ambitionbox.com/"
driver.get(url)


# In[70]:


search_job = driver.find_element_by_xpath("/html/body/div/div/div/main/section[1]/div[2]/div[1]/span/input")
search_job


# In[71]:


search_job.send_keys("Data Scientist")


# In[ ]:




