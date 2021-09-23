# from urllib import request,parse
# # response=request.urlopen("https://www.w3schools.com/xml/simple.xml")
# # print(response.read())
# response=parse.urlparse("https://www.w3schools.com/xml/simple.xml")
# print(response)

import requests
import xmltodict
response=requests.get("https://www.w3schools.com/xml/simple.xml")
foods=xmltodict.parse(response.content)
# print(foods)
for food in foods['breakfast_menu']['food']:
    print("Name:",food['name'],",price:",food['price'])

