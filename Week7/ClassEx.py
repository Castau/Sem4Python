# In the following text find all the family names of everyone with first name Peter:
import re
import bs4
import requests

txt = 'Peter Hansen was meeting up with Jacob Fransen for a quick lunch, but first he had to go by Peter Beier to pick up some chokolate for his wife. Meanwhile Pastor Peter Jensen was going to church to give his sermon for the same 3 people in his parish. Those were Peter Kold and Henrik Halberg plus a third person who had recently moved here from Norway called Peter Harold'

pattern = re.compile(r'(Peter \w+)')
match = pattern.findall(txt)
print(match)


# txt2 = 'F:\\Developer\\4semester\\Python\\Afleveringer\\Sem4Python\\Week7\\txt2.txt'
# txtinfile = ''


# pattern2 = re.compile(r'\n\n(.+)')
# match2 = pattern.findall(txtinfile)
# print(match2)

# Use BeautifulSoup to extract all titles on all radio programs https: // www.dr.dk/radio/programmer

# First find how many pages there are
# Then find all titles on https: // www.dr.dk/radio/programmer?side = 1
# Then find all titles on all pages


url = 'https://www.dr.dk/radio/programmer'
r = requests.get(url)
r.raise_for_status()

soup = bs4.BeautifulSoup(r.text, 'html.parser')
buttons = soup.select('button.pagination_item')
programs = soup.select('ul.spot-list-search__spots li a div.spot-content h3')
titles = [p.text for p in programs]

print(titles)


from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.krak.dk')

