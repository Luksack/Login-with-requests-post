import requests
from lxml import html
import logging
from requests_toolbelt.utils import dump

LOGIN_URL = "https://ezakupy.tesco.pl/groceries/pl-PL/login"
SCRAP_URL = "https://ezakupy.tesco.pl/groceries/pl-PL/shop/napoje/napoje-gazowane/cola"
import json


def main():
    sesssion_requests = requests.Session()

    result = sesssion_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]
    payload = {
        "email": "sir.wons@gmail.com",
        "password": "radziogej1",
        "_csrf": authenticity_token
    }
    dupa = sesssion_requests.post(LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))
    # data = dump.dump_all(dupa)
    # print(data.decode('utf-8'))

    body = [{
        "id": "2003006799334",
        "newValue": "1",
        "oldValue": "0",
        "newUnitChoice": "pcs",
        "oldUnitChoice": "pcs"
    }]

    headers = {
        "accept": "application/json",
        "x-csrf-token": "Q2cQC2Xf-OUk4BP5aBf34UPzWBbxiy5Wrwo8",
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }

    req_url = "https://ezakupy.tesco.pl/groceries/pl-PL/trolley/items?_method=PUT"
    job = sesssion_requests.put(req_url, data=json.dumps(body), headers=headers)
    data = dump.dump_all(job)
    print(data.decode('utf-8'))

    result = sesssion_requests.get(SCRAP_URL, headers=dict(referer=SCRAP_URL))
    tree = html.fromstring(result.content)
    cart_cash = tree.xpath("//*[@id='mini-trolley']/div[1]/a/div/div[1]/div/div/span/span[1]/text()")
    print(cart_cash)


if __name__ == '__main__':
    logging.basicConfig(
        filename='login.log',
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s: %(message)s"
    )
    logging.debug(main())
