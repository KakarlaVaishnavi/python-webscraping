#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import csv

url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')


#product url
urls=[]
url=soup.findAll('div',class_='a-row a-spacing-micro')
for i in urls:
    j=i.a['href']
    urls.append(j)
print(urls)  

#product name
names=[]
name=soup.findAll('div',class_='a-size-medium a-color-base a-text-normal')
for i in names:
    j=i.a.text
    names.append(j)
print(names)

#product price
prices=[]
price=soup.findAll('div',class_='a-price-whole')
for i in prices:
    j=i.a.text
    prices.append(j)
print(prices)

#product rating
ratings=[]
rating=soup.findAll('div',class_='a-size-base puis-bold-weight-text')
for i in ratings:
    j=i.a.text
    ratings.append(j)
print(ratings)

#no. of reviews
reviews=[]
review=soup.findAll('div',class_='a-size-base s-underline-text')
for i in reviews:
    j=i.a.text
    reviews.append(j)
print(reviews)

#storing data using csv
with open('name.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(url)
    for i in urls:
        j=i.a.text
        names.append(j)
    write.writerow(urls)
    
with open('name.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(name)
    for i in names:
        j=i.a.text
        names.append(j)
    write.writerow(names)
    
with open('name.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(price)
    for i in prices:
        j=i.a.text
        names.append(j)
    write.writerow(prices)
    
with open('name.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(rating)
    for i in ratings:
        j=i.a.text
        names.append(j)
    write.writerow(ratings)
    
with open('name.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(review)
    for i in reviews:
        j=i.a.text
        names.append(j)
    write.writerow(reviews)
    
#part2

for i in urls:
    while(i<=200)
         #description
           descriptions=[]
            description=soup.findAll('div',class_='a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list')
            for i in descriptions:
                j=i.a.text
                description.append(j)
            print(descriptions)
    
         #ASIN
           asins=[]
            asin=soup.findAll('div',class_='a-text-bold')
             for i in asins:
                j=i.a.text
                asin.append(j)
            print(asins)
    
          #product description
           pdescriptions=[]
             pdescriptin=soup.findAll('div',class_='a-list-item')
                for i in pdescriptions:
                    j=i.a.text
                    pdescription.append(j)
                print(pdescriptions)
    
        #manufacturer
           manufacturers=[]
            manufacture=soup.findAll('div',class_='a-text-bold')
            for i in manufacture:
                j=i.a.text
                manufacture.append(j)
            print(manufactures)
        
 #storing data using csv
with open('description.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(description)
    for i in descriptions:
        j=i.a.text
        descriptions.append(j)
    write.writerow(descriptions) 
    
with open('asin.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(url)
    for i in asins:
        j=i.a.text
        asins.append(j)
    write.writerow(asins) 
    
with open('pdescription.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(url)
    for i in pdescriptions:
        j=i.a.text
        pdescriptions.append(j)
    write.writerow(pdescriptions)
    
with open('manufacturer.csv','w') as csv_file:
    write=csv.writer(csv_file)
    write.writerow(url)
    for i in manufacturers:
        j=i.a.text
        manufacturers.append(j)
    write.writerow(manufacturers)    


# In[ ]:




