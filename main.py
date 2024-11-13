from bs4 import BeautifulSoup
import requests
import re


def getHTMLDOC(url):


    response = requests.get(url)

    return response.text

# urlName ="https://docs.python.org/3/library/turtle.html"
urlName = input("Enter URL: ")

html_doc = getHTMLDOC(urlName)



soup = BeautifulSoup(html_doc, 'html.parser')


def findLinks():
    print("Links found: ")
    for link in soup.find_all('a',
                            attrs={"href": re.compile("^https://")}):
        
        print(link.get("href"))

def findElementsByClass():
    class_name = input("Enter class name: ")
    elements = soup.find_all(class_=class_name)
    print("Elements with class '" + class_name + "':")
    for element in elements:
        print(element)


def findElementsByID():
    id_name = input("Enter id name: ")
    elements = soup.find_all(id=id_name)
    print("Elements with id '" + id_name + "':")
    for element in elements:
        print(element)

# def findHeaders():
#     print("Headers found: ")
#     for header in soup.find_all(re.compile('h[1-6]$')):
#         print(header.name + ":" + header.text.split())

def findHeaders():
    print("Headers found: ")
    for header in soup.find_all(re.compile('h[1-6]$')):
        header_text = header.get_text(strip=True)
        print(f"{header.name} : {header_text}")

end = False
while end != True:


    task = int(input(
    "(1) Find header,"
    "(2) Find from ID,"
    "(3) Find from class,"
    "(4) Find all links,"
    "(5) End, Input: "))

    if task == 1:
        findHeaders()
    elif task == 2:
        findElementsByID()
    elif task == 3:
        findElementsByClass()
    elif task == 4:
        findLinks()
    elif task == 5:
        print("Program exiting")
        break


