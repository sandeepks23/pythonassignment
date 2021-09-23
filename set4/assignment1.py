import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(
    requests.get("https://realpython.github.io/fake-jobs/").content,
    "html.parser")
# print(soup)
titles = []
company=[]
img=[]
location=[]
time=[]
head = soup("div", class_="card-content", limit=10)


for td in head:
    titles.append(td.find("h2").contents[0])
    company.append(td.find("h3").contents[0])
    img.append(td.find("img").get('src'))
    location.append(td.find("p").get_text())
    time.append(td.find('time').get_text())



for i in range(0,10):
    print("Image URL : ",img[i])
    print("Title : ",titles[i])
    print("Company : ",company[i])
    print("Time : ",time[i])
    print("Location : ", location[i])
    print()
