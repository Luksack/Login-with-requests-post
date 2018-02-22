import requests
from lxml import html
import logging

login_url = "https://ezakupy.tesco.pl/groceries/pl-PL/login"
URL = "https://ezakupy.tesco.pl/groceries/pl-PL/shop/napoje/napoje-gazowane/cola"

def main():
    sesssion_requests = requests.Session()

    result = sesssion_requests.get(login_url)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    payload = {
        "email": "mail",
        "password": "pass",
        "_csrf": authenticity_token
    }

    sesssion_requests.post(login_url, data=payload, headers=dict(referer=login_url))

    result = sesssion_requests.get(URL, headers=dict(referer=URL))

    tree = html.fromstring(result.content)
    names = tree.xpath("//*[@id='content']/div/div/div[1]/div[1]/ul/li[1]/div/text()")
    print(names)


if __name__ == '__main__':
    logging.basicConfig(
        filename='login.log',
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s: %(message)s"
    )
    logging.debug(main())
