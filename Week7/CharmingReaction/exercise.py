from time import sleep
from selenium import webdriver
import re
import bs4
import requests
import matplotlib.pyplot as plt
import json
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
baseUrl = 'https://www.dba.dk/biler/biler'


def getsoup(url):
    browser.get(url)
    # browser.implicitly_wait(1)
    return bs4.BeautifulSoup(browser.page_source, 'html.parser')


# 1. Hvor mange brugte biler er der at vælge i mellem
def first():
    annoncetype_div = getsoup(baseUrl).findAll(
        "div", {"class": "navigator radioNavigator modulePanel"})
    small_tags = annoncetype_div[0].findAll("small")
    cars = small_tags[0].text
    print('Cars for Sale: ', cars)
    browser.close()


# 2. Udskriv alle biler af mærket Ford
def second():
    url = baseUrl + '/maerke-ford'
    page = '/side-'

    pagesSoup = getsoup(url)
    cars_a_tag = pagesSoup.findAll(
        "a",
        {
            "class": "trackClicks",
            "data-ga-act": "click",
            "data-ga-lbl": "paging-number",
        },
    )
    numPages = int("".join(filter(str.isdigit, cars_a_tag[-1].text)))
    for pageNum in range(1, numPages + 1):
        soup = getsoup(url + page + str(pageNum))
        cars = soup.findAll("tr", {"class": "dbaListing listing"})
        for car in cars:
            car_tag = car.findAll("a", {"class": "listingLink"})
            print(car_tag[1].text.encode('utf-8'))
            print('\n')
    browser.close()


# 3. Åben de 5 dyreste biler med selenium i decending order og vis dem med et bar chart
def third():
    # Thanks to Rúni for the tip to this exercise
    browser.get(baseUrl)
    gdrp_button = browser.find_element_by_id('gdpr-notice__accept')
    gdrp_button.click()

    def sortByPrice():
        tablehead = browser.find_element_by_class_name('sorting')
        span = tablehead.find_elements_by_class_name('human-ref')[-1]
        span.click()
    sleep(3)
    sortByPrice()
    sleep(3)
    sortByPrice()
    sleep(3)
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    data = soup.findAll('tr', {'class': 'dbaListing listing'})
    cars = []
    for item in data[:5]:
        car = item.find('script', {'type': 'application/ld+json'})
        jsoncar = json.loads(car.text)
        cars.append({'name': jsoncar['name'],
                     'price': jsoncar['offers']['price']})
    browser.close()
    return cars


def thirdBarPlot(data):
    # testData = {'Porsche 918 Spyder 4': '10125000', 'Ferrari 458 4,5 Ital': '2379900',
    # 'Ferrari F512 M 4,9 B': '1953600', 'Ferrari 458 4,5 Spec': '1949900', 'Mercedes SL65 6,0 AM': '1878600'}
    fig, ax = plt.subplots()
    ax.ticklabel_format(style='plain')
    plt.grid(axis='y', linestyle='dotted', zorder=0)
    names = []
    prices = []
    for car in data:
        names.append(car['name'][:20])
        prices.append(car['price'])
    carData = dict(zip(names, prices))
    plt.bar(carData.keys(), list(map(int, carData.values())),
            zorder=3, width=0.35, align='center', bottom=0)
    plt.title('Dyreste biler på DBA')
    plt.xlabel('Biler')
    plt.ylabel('Pris')
    plt.xticks(rotation=45, ha="right")
    plt.show()


if __name__ == '__main__':
    # first()
    # second()
    # print(third())
    thirdBarPlot(third())
