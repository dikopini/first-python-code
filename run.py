import requests
from bs4 import BeautifulSoup


url = 'https://www.yachtworld.com/boats-for-sale/?makeModel=hunter&page='
header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

def pagination():
    res = requests.get(url, headers=header)
    soup =BeautifulSoup(res.text, 'html.parser')
    pages = soup.find('div', {'class':'search-page-nav'})
    total_page = pages.find('a')
    print(total_page)


def content():
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    contents = soup.find_all('div', {'class': 'listing-card-information'})

    boat_list = []
    for info in contents:
        name = info.find('h2').text
        price = info.find('span').text
        location = info.find('div', {'class': 'listing-card-location'}).text
        broker = info.find('div', {'class': 'listing-card-broker'}).text

        datas = {
        'name': name,
        'price': price,
        'location': location,
        'broker': broker
        }

        boat_list.append(datas)


if __name__ == '__main__':
    pagination()