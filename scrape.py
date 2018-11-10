import re
import requests
from bs4 import BeautifulSoup

def getText(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "lxml")
    data = soup.findAll(text=True)

    def findText(element):
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False

        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False

        return True

    results = filter(findText, data)

    return (' '.join(list(results)))

#print(getText('https://en.wikipedia.org/wiki/William_S._Burroughs'))
