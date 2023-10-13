# import requests 

# # Making a GET request 
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# # check status code for response received 
# # success code - 200 
# print(r) 

# # print content of request 
# print(r.content)


# import requests

# # making a GET request
# s = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

# #print request object
# print(s.url)

# #print status code
# print(s.status_code)

# import requests
# from bs4 import BeautifulSoup

# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# # check status code for response received
# # Success code - 200
# print(r)

# # Parsing the HTML
# soup = BeautifulSoup(r.content,'html.parser')
# print(soup.prettify())



# import requests
# from bs4 import BeautifulSoup

# # # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# # parsing the HTML
# soup = BeautifulSoup(r.content,"html.parser")
# # Getting the title tag
# print(soup.title)

# # Getting the name of the tag 
# print(soup.title.name) 
  
# # Getting the name of parent tag 
# print(soup.title.parent.name) 
  
# # use the child attribute to get 
# # the name of the child tag 

# import requests
# from bs4 import BeautifulSoup

# #  Making a GET Request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/') 

# # Parsing the HTML
# soup = BeautifulSoup(r.content,'html.parser')

# s = soup.find('div', class_='entry-content')
# content = s.find_all('p')

# print(content)



# from bs4 import BeautifulSoupas soup  
# from urllib.request import urlopen as uReq  
  
# # Request from the webpage  
# myurl = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  
  
  
# uClient  = uReq(myurl)  
# page_html = uClient.read()  
# uClient.close()  
  
# page_soup = soup(page_html, features="html.parser")  
  
# print(soup.prettify(containers[0]))  
  
# This variable held all html of webpage  
# containers = page_soup.find_all("div",{"class": "_3O0U0u"})  
# container = containers[0]  
# # print(soup.prettify(container))  
#  
# price = container.find_all("div",{"class": "col col-5-12 _2o7WAb"})  
# print(price[0].text)  
#  
# ratings = container.find_all("div",{"class": "niH0FQ"})  
# print(ratings[0].text)  
#  
# #  
# # print(len(containers))  
# print(container.div.img["alt"])  
  
# Creating CSV File that will store all data   
filename = "product1.csv"  
f = open(filename,"w")  
  
headers = "Product_Name,Pricing,Ratings\n"  
f.write(headers)  
  
for container in containers:  
    product_name = container.div.img["alt"]  
  
    price_container = container.find_all("div", {"class": "col col-5-12 _2o7WAb"})  
    price = price_container[0].text.strip()  
  
    rating_container = container.find_all("div",{"class":"niH0FQ"})  
    ratings = rating_container[0].text  
  
# print("product_name:"+product_name)  
    # print("price:"+price)  
    # print("ratings:"+ str(ratings))  
  
     edit_price = ''.join(price.split(','))  
     sym_rupee = edit_price.split("?")  
     add_rs_price = "Rs"+sym_rupee[1]  
     split_price = add_rs_price.split("E")  
     final_price = split_price[0]  
  
     split_rating = str(ratings).split(" ")  
     final_rating = split_rating[0]  
  
     print(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
f.write(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
  
f.close()  