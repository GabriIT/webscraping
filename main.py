from bs4 import BeautifulSoup
import requests


# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
# Extract title of page

soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text
# Extract first <h1>(...)</h1> text
first_h1 = soup.select('h1')[0].text
second_h1 = soup.select('h1')[1].text
first_h2 = soup.select('h2')[0].text
first_h3 = soup.select('h3')[0].text
print(page_title)
"\n"
print(first_h1)
"\n"
print(second_h1)
"\n"
print(first_h2)
"\n"
print(first_h3)
