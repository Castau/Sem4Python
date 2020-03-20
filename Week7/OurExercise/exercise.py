from time import sleep
from selenium import webdriver
import re
import bs4
import requests
import matplotlib.pyplot as plt

browser = webdriver.Chrome()
base_url = 'https://www.merchbar.com/search?q=breaking%20benjamin&p=1'

browser.get(base_url)
browser.implicitly_wait(1)


# 1) Hvor mange produkter kommer frem, når man søger på 'breaking benjamin' (se URL'en)
def first():
    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
    cell = soup.find_all('div', {'class': 'd-none d-md-block col-md-3'})[0]
    text = cell.select("span")[0].text
    amount = re.compile(r'\d*')
    match = amount.search(text)
    return match.group(0)


# 2) Hvor mange TRACKs er der i det første produkt, som ligger i kategorien CDs?
def second():
    checkbox = browser.find_elements_by_class_name(
        'ais-RefinementList-labelText')[2]
    checkbox.click()
    sleep(1.0)
    firstCD = browser.find_element_by_xpath('//div[@data-id="759745"]')
    firstCD.click()
    sleep(1.0)
    trackList = browser.find_element_by_class_name('track-list')
    tracks = trackList.find_elements_by_class_name('track')
    return len(tracks)


# 3) Vis et bar chart der viser:
# - Procentdel af de viste produkter, der rent faktisk indeholder Breaking Benjamin merch
# - Procentdel af den merch, der er på tilbud
# - Procentdel af den merch, der ikke er på lager
def scrolldown():
    SCROLL_PAUSE_TIME = 1.0
    scrollheight = browser.execute_script("return document.body.scrollHeight")

    while True:
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        newheight = browser.execute_script(
            "return document.body.scrollHeight")
        if newheight == scrollheight:
            break
        scrollheight = newheight
    return True


def third():
    done_scrolling = scrolldown()
    allItems = 0
    bbItems = 0
    onsale = 0
    out_of_stock = 0
    if done_scrolling:
        merch_items = browser.find_elements_by_xpath(
            '//div[@class="col-md-4 col-6"]')
        allItems = len(merch_items)

        for item in merch_items:
            sale_element = False
            name_element = item.find_element_by_class_name(
                'MerchTile\.module__brandName')
            stock_element = item.find_element_by_class_name(
                'MerchTile\.module__status')
            if name_element.text.upper() == "BREAKING BENJAMIN":
                bbItems += 1
                try:
                    item.find_element_by_class_name(
                        'MerchTile\.module__overlayCode')
                    sale_element = True
                except:
                    pass
                if sale_element:
                    onsale += 1
                if not stock_element.text.upper() == "IN STOCK":
                    out_of_stock += 1

    BB_div_all = bbItems/allItems * 100
    BB_on_sale = onsale/bbItems * 100
    BB_out_of_stock = out_of_stock/bbItems * 100

    data = {'BB': BB_div_all, 'BB sale': BB_on_sale,
            'BB not in stock': BB_out_of_stock}

    plt.bar(data.keys(), data.values(), width=0.35, align='center')
    plt.axis([-1, len(data.values()), 0, 100])
    plt.title('Breaking Benjamin merchandise', fontsize=12)
    plt.ylabel('Percentage', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)
    plt.xticks(rotation=10)
    plt.show()


if __name__ == '__main__':
    # print(first())
    # print(second())
    third()
