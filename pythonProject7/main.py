# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def post_example():
    data_dict = {
        "comments": "",
        "custemail": "evor@fac.ocm",
        "custname": "Esther",
        "custtel": "0251659",
        "delivery": "13:15",
        "size": "small",
        "topping": ["bacon","cheese"]
    }

    r = requests.post('https://httpbin.org/post', data = data_dict)
    print(r.text)

def get_exmaple():
    f = requests.get('http://api.facebook.com', timeout = 6)
    print(f.status_code)

    r = requests.get('http://httpbin.org/basic-auth/Esther/123',
                     auth=("Esther", "1233"), timeout=6)
    print(r.status_code)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    r = requests.get('https://xkcd.com/353/')
    #print(r.text)

    im = requests.get(' https://imgs.xkcd.com/comics/python.png')
    #print(r.content)
    with open('comic.png', 'wb') as f:
        f.write(im.content)

    #check status response - 200 is good
    print(r.status_code)
    print(r.ok)

    payload = {'page': 2, 'count': 25}
    rr = requests.get('http://httpbin.org/get', params = payload)
    print(rr.text)
    print(rr.url)
    payload = {'username': 'corey', 'password': 'testing'}
    rr = requests.post('http://httpbin.org/post', data=payload)
    r_dist = rr.json()
    print(r_dist['form'])
    #print(rr.json())

    github_adapter = HTTPAdapter(max_retries=3)

    session = requests.Session()

    # Use `github_adapter` for all requests to endpoints that start with this URL
    session.mount('https://api.github.com', github_adapter)

    try:
        session.get('https://api.github.com')
    except ConnectionError as ce:
        print(ce)

    #add username to url
    rr = requests.get('http://httpbin.org/delay/1', timeout=3)
    #print(rr)

    post_example()
    get_exmaple()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
