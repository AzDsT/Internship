#!/usr/bin/env python
# coding: utf-8

# 1 - Write a python program to display all the header tags from wikipedia.org

# In[53]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[54]:


from bs4 import BeautifulSoup
import requests


# In[55]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[56]:


page


# In[57]:


bs = BeautifulSoup(page.text, "html.parser")


# In[58]:


wiki = bs.find_all(['h1','h2','h3','h4','h5','h6'])
for i in wiki:
    print(i)


# 2 - Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.
# 

# In[59]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[60]:


page = requests.get("https://www.imdb.com/list/ls055592025/")
page


# In[61]:


soup = BeautifulSoup(page.content)
soup


# In[62]:


movie=[]
name = []
raiting=[]
year_of_release=[]


for i in soup.find_all('div',class_='lister-item mode-detail'):
        
#         name.append(i.h3.a.text)
#         year_of_release.append(i.h3.find('span', class_='lister-item-year').text)
#         raiting.append(i.find('span',class_='ipl-rating-star__rating').text)
        
    title = i.h3.a.text
    year = i.h3.find('span', class_='lister-item-year').text
    rate = i.find('span',class_='ipl-rating-star__rating').text
    
    movie.append([title]+[rate]+[year])
        
        

        
#         movie.append(i.h3.a.text)
#         movie.append(i.h3.find('span', class_='lister-item-year').text)
#         movie.append(i.find('span',class_='ipl-rating-star__rating').text)
        
# year_of_release
# name
# raiting
movie


# In[63]:


df=pd.DataFrame(movie,columns=['Name','Rate','Year of Release'])
df


# 3 - Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.

# In[64]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[65]:


page=requests.get("https://www.imdb.com/list/ls009997493/")
page


# In[66]:


soup=BeautifulSoup(page.content)
soup


# In[67]:


Indian_Movies=[]
name=[]
rating=[]
year_of_release=[]

for i in soup.find_all('div',class_="lister-item mode-detail"):
    name = i.h3.a.text
    rating = i.find('span',class_='ipl-rating-star__rating').text
    year_of_release = i.find('span',class_="lister-item-year").text
    Indian_Movies.append([name] + [rating] + [year_of_release])
Indian_Movies
    


# In[68]:


df=pd.DataFrame(Indian_Movies,columns=['Name','Rating','Year of Release'])
df.head(10)


# 4 - Write a python program to scrape product name, price and discounts from https://meesho.com/bagsladies/pl/p7v

# In[69]:


#from bs4 import BeautifulSoup
#import requests


# In[70]:


page = requests.get("https://meesho.com/bags-ladies/pl/p7vbp")
page


# In[71]:


soup=BeautifulSoup(page.content)
soup


# In[72]:


Product_name = []

for i in soup.find_all('p',class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS"):
        
        Product_name.append(i.text)
Product_name


# In[73]:


Price = []

for i in soup.find_all('h5', class_="Text__StyledText-sc-oo0kvp-0 hiHdyy"):
    Price.append(i.text)
    
Price


# In[74]:


Discounts = []
for i in soup.find_all("p",class_="Text__StyledText-sc-oo0kvp-0 fCJVtz NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm NewProductCard__DiscountTextParagraph-sc-j0e7tu-16 kmYsnm"):
    Discounts.append(i.text)
Discounts


# 5 -  Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 ODI Batsmen along with the records of their team and rating.
# 
# c) Top 10 ODI bowlers along with the records of their team and rating.

# In[ ]:


# a)


# In[75]:


from bs4 import BeautifulSoup
import requests


# In[76]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[77]:


soup=BeautifulSoup(page.content)
soup


# In[78]:



overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('td',class_='rankings-block__banner--team-name').find('span',class_='u-hide-phablet').text
        matches = soup.find('td', class_='rankings-block__banner--matches').text
        points = soup.find('td', class_='rankings-block__banner--points').text 
        raitings = soup.find('td', class_='rankings-block__banner--rating u-text-right').text.replace('\n',' ').strip()
        overall.append([name]+[matches]+[points]+[raitings])
    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__team').find('span',class_='u-hide-phablet').text
   
    matches = i.find_all('td', class_='table-body__cell u-center-text')[0].text
    points = i.find_all('td', class_='table-body__cell u-center-text')[1].text
    raitings = i.find('td', class_='table-body__cell u-text-right rating').text
    
    overall.append([name]+[matches]+[points]+[raitings])


    if count == 10:
     break



overall


# In[ ]:


# b)


# In[79]:


from bs4 import BeautifulSoup
import requests


# In[80]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[81]:


soup=BeautifulSoup(page.content)
soup


# In[82]:


overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('div',class_='rankings-block__banner--name-large').text
        team = soup.find('span', class_='table-body__logo-text').text
        raitings = soup.find('td', class_='table-body__cell rating').text
        overall.append([name]+[team]+[raitings])

    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__name name').a.text
    team = i.find('span', class_='table-body__logo-text').text
    raitings = i.find('td', class_='table-body__cell rating').text
    

    overall.append([name]+[team]+[raitings])


    if count == 10:
     break


overall


# In[ ]:


# c)


# In[83]:


page=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page


# In[84]:


soup=BeautifulSoup(page.content)
soup


# In[85]:



overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('div',class_='rankings-block__banner--name-large').text
        team = soup.find('span', class_='table-body__logo-text').text
        raitings = soup.find('td', class_='table-body__cell rating').text
        overall.append([name]+[team]+[raitings])

    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__name name').a.text
    team = i.find('span', class_='table-body__logo-text').text
    raitings = i.find('td', class_='table-body__cell rating').text
    

    overall.append([name]+[team]+[raitings])


    if count == 9:
     break


overall


# 6 Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# 
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating

# In[ ]:


# a)


# In[86]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[87]:


soup=BeautifulSoup(page.content)
soup


# In[88]:


overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('td',class_='rankings-block__banner--team-name').find('span',class_='u-hide-phablet').text
        matches = soup.find('td', class_='rankings-block__banner--matches').text
        points = soup.find('td', class_='rankings-block__banner--points').text 
        raitings = soup.find('td', class_='rankings-block__banner--rating u-text-right').text.replace('\n',' ').strip()
        overall.append([name]+[matches]+[points]+[raitings])
    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__team').find('span',class_='u-hide-phablet').text
   
    matches = i.find_all('td', class_='table-body__cell u-center-text')[0].text
    points = i.find_all('td', class_='table-body__cell u-center-text')[1].text
    raitings = i.find('td', class_='table-body__cell u-text-right rating').text
    
    overall.append([name]+[matches]+[points]+[raitings])


    if count == 10:
     break



overall


# In[ ]:


# b)


# In[89]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[90]:


soup=BeautifulSoup(page.content)
soup


# In[91]:


overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('div',class_='rankings-block__banner--name-large').text
        team = soup.find('span', class_='table-body__logo-text').text
        raitings = soup.find('td', class_='table-body__cell rating').text
        overall.append([name]+[team]+[raitings])

    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__name name').a.text
    team = i.find('span', class_='table-body__logo-text').text
    raitings = i.find('td', class_='table-body__cell rating').text
    

    overall.append([name]+[team]+[raitings])


    if count == 10:
     break


overall


# In[ ]:


# c)


# In[92]:


page=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[93]:


soup=BeautifulSoup(page.content)
soup


# In[94]:


overall = []

count = 0



for i in soup.find_all('tr',class_='table-body'):
    
    if count==0:
        name = soup.find('div',class_='rankings-block__banner--name-large').text
        team = soup.find('span', class_='table-body__logo-text').text
        raitings = soup.find('td', class_='table-body__cell rating').text
        overall.append([name]+[team]+[raitings])

    
    
    count = count + 1

    name = i.find('td',class_='table-body__cell rankings-table__name name').a.text
    team = i.find('span', class_='table-body__logo-text').text
    raitings = i.find('td', class_='table-body__cell rating').text
    

    overall.append([name]+[team]+[raitings])


    if count == 9:
     break


overall


# 7 -  Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content
# and the code for the video from the link for the youtube video from the post.

# In[327]:


page=requests.get("https://coreyms.com/")
page


# In[96]:


soup=BeautifulSoup(page.content)
soup


# In[134]:


overall = []





# iframes= soup.find('iframe')
# for iframe in iframes:
#     src=iframe['src']
    


for i in soup.find_all('article'):
    heading = i.a.text
    date = i.find('time', class_='entry-time').text
    content =i.find('div',class_='entry-content').p.text
    iframes=i.find_all('iframe')
    src=[]
    for iframe in iframes:
        src.append(iframe['src'])
    
    
    overall.append([heading]+[date]+[content]+[src])
    
    
    
    
  
overall


# 8) Write a python program to scrape house details from mentioned URL. It should include house title, location,
# area, EMI and price from https://www.nobroker.in/ .Enter three localities which are Indira Nagar, Jayanagar, 
# Rajaji Nagar.

# In[216]:


from bs4 import BeautifulSoup
import requests


# In[136]:


soup=BeautifulSoup(page.content)
soup


# In[217]:


page=requests.get("https://www.nobroker.in/property/rent/chennai/Indira%20Nagar?searchParam=W3sibGF0IjoxMi45OTE2NjMsImxvbiI6ODAuMjUyNDIzMSwicGxhY2VJZCI6IkNoSUpEUWFSallwblVqb1I3cXc4eVNfUzlrQSIsInBsYWNlTmFtZSI6IkluZGlyYSBOYWdhciJ9XQ==&radius=2.0&sharedAccomodation=0&city=chennai&locality=Indira%20Nagar")
page


# In[218]:


soup=BeautifulSoup(page.content)
soup


# In[325]:


overall = []




for i in soup.find_all('article'):
    
   

    
    
    

    title = i.a.text
    location = i.find('div',class_='mt-0.5p').text
    price = i.find(id='minDeposit').span
    

    
    

    overall.append([title]+[location]+[price])


   


overall


# In[ ]:





# In[136]:


soup=BeautifulSoup(page.content)
soup


# In[ ]:





# In[ ]:





# 9) Write a python program to scrape mentioned details from dineout.co.in :
# 
# i) Restaurant name
# 
# ii) Cuisine
# 
# iii) Location
# 
# iv) Ratings
# 
# v) Image URL 

# In[ ]:


from bs4 import BeautifulSoup
import request


# In[148]:


page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[150]:


soup=BeautifulSoup(page.content)
soup


# In[180]:


overall = []




for i in soup.find_all('div',class_='restnt-main-wrap clearfix'):
    
   

    
    
    

    name = i.a.text
    cousineData = i.find('span', class_='double-line-ellipsis').find_all('a')
    cousines=[]
    for cousine in cousineData:
        cousines.append(cousine.text)
    locationData = i.find('div', class_='restnt-loc ellipsis').find_all('a')
    locations=[]
    for location in locationData:
        locations.append(location.text)
    raiting = i.find('div', class_='restnt-rating rating-4').text
    imageUrl = i.find('img', class_="no-img")['data-src']
    

    overall.append([name]+[cousines]+[locations]+[raiting]+[imageUrl])


   


overall


# In[ ]:





# 10) Write a python program to scrape first 10 product details which include product name , price , Image URL from
# https://www.bewakoof.com/women-tshirts?ga_q=tshirts .

# In[328]:


from bs4 import BeautifulSoup
import requests


# In[329]:


page=requests.get("https://www.bewakoof.com/women-tshirts?ga_q=tshirts")
page


# In[330]:


soup=BeautifulSoup(page.content)
soup


# In[331]:


overall = []


count = 0

for i in soup.find_all('div',class_='productGrid'):
    
   

    
    
    

    name = i.find('div',class_='productCardDetail').div.h3.text
    price = i.find('span', class_='discountedPriceText').b.text.r
    imageUrl = i.find('div', class_="productCardImg").div.img['src']

    overall.append([name]+[price]+[imageUrl])


    count = count + 1
    
    if count == 10:
        break

overall

