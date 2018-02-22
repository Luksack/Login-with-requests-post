import requests
from lxml import html
import logging

LOGIN_URL = "https://ezakupy.tesco.pl/groceries/pl-PL/login"
SCRAP_URL = "https://ezakupy.tesco.pl/groceries/pl-PL/shop/napoje/napoje-gazowane/cola"


def main():
    sesssion_requests = requests.Session()

    result = sesssion_requests.get(LOGIN_URL)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    payload = {
        "email": "mail",
        "password": "pass",
        "_csrf": authenticity_token
    }

    sesssion_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    result = sesssion_requests.get(SCRAP_URL, headers=dict(referer=SCRAP_URL))

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
