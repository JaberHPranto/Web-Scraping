import requests
from bs4 import BeautifulSoup
import pprint

res1 = requests.get("https://news.ycombinator.com/news")


def sortByVotes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def getHackerNewsWithVotes(links, subtext):
    hackNews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                hackNews.append({'title': title, 'link': href, 'votes': points})

    return sortByVotes(hackNews)


def main():
    for page_no in range(1, 3):
        res = requests.get("https://news.ycombinator.com/news?p=" + str(page_no))

        soupObject = BeautifulSoup(res.text, features='html.parser')
        links = soupObject.select('.storylink')
        subtext = soupObject.select('.subtext')
        pprint.pprint(getHackerNewsWithVotes(links, subtext))


if __name__ == '__main__':
    main()
