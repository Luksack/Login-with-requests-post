import requests
from lxml import html



def main():

    sesssion_requests = requests.session()

    login_url = "https://ezakupy.tesco.pl/groceries/pl-PL/login"
    result = sesssion_requests.get(login_url)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0] # XPATH of hidden token

    payload = {
        "email": "<USERNAME>",
        "password": "<PASS>",
        "_csrf": "<f2Ybad5q-89AHsTYLqQXuQMUk4ybo2sC0o9A>"
    }

    result = sesssion_requests.post(login_url, data=payload, headers=dict(referer=login_url))

    url = "https://ezakupy.tesco.pl/groceries/pl-PL/shop/napoje/napoje-gazowane/cola"
    result = sesssion_requests.get(url, headers=dict(referer=url))

    tree = html.fromstring(result.content)
    names = tree.xpath("//*[@id='product-list']/div[2]/div[4]/div[1]/div[2]/div/div/div/ul/li/div/div/div/div/div[1]/div/a/text()")

    print(names)

if __name__ == '__main__':
    main()