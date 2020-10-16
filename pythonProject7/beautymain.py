# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests, os, bs4
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

def func1():
    url = 'http://xkcd.com'
    os.makedirs('image', exist_ok=True)
    while not url.endswith('#'):
        # Download the page.
        print('Downloading page %s...' % url)
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')

        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            try:
                comicUrl = 'http:' + comicElem[0].get('src')
                # Download the image.
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()
            except requests.exceptions.MissingSchema:
                # skip this comic
                prevLink = soup.select('a[rel="prev"]')[0]
                url = 'http://xkcd.com' + prevLink.get('href')
                continue
        # TODO: Save the image to ./xkcd.
        imageFile = open(os.path.join('image', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        # TODO: Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')

    print('Done.')

def func2():
    url = 'http://fabpedigree.com/james/mathmen.htm'
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    soup3 = soup.find_all('table')[1]
    list_names = []
    for summary in soup3.find_all("a"):
        list_names.append(summary.text)

    for i in range(len(list_names) - 1):
        print(list_names[i])


if __name__ == '__main__':
    print('Ciao  ^ ___________ ^')
    with open('sample.html', 'r') as h_file:
        soup = BeautifulSoup(h_file, 'lxml')

    #print(soup.prettify())
    match = soup.title.text
    #print(match)
    match = soup.find('div',class_='footer')
    #print(match)

    article = soup.find('div', class_='article')
    #print(article)
    summary = article.p.text
    #print(summary)

    print(' ')

    for summary in soup.find_all('div', class_='article'):
        headline = article.h2.text
        summary = article.p.text
       # print(headline)
        #print(summary)
       # print('')


    #new functions
    source = requests.get('http://coreyms.com').text
    soup = BeautifulSoup(source, 'lxml')
    #print(soup.prettify())

    func2()



