import requests
from bs4 import BeautifulSoup


def content():
    url = 'https://www.yachtworld.com/boats-for-sale/?makeModel=hunter&page='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    contents = soup.find_all('div', {'class': 'listing-card-information'})

    for info in contents:
        name = info.find('h2').text
        print(name)



if __name__ == '__main__':
    content()