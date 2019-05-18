import json
import requests

from bs4 import BeautifulSoup

def realpython():
    url = 'https://realpython.com/team/rwhite/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    h2 = soup.find('h2')
    ul = h2.find_next('ul')

    with open('real_python_tuts.json', 'w') as tuts:

        tutorial_list = []
        for item in ul.find_all('li'):
            link = 'https://realpython.com' + item.a['href']
            title = item.text

            item_dict = { "title": title, "link": link }
            tutorial_list.append(item_dict)

        json.dump(tutorial_list, tuts)


if __name__ == "__main__":
    realpython()