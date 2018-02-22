import requests
from lxml import html



def main():

    sesssion_requests = requests.session()

    login_url = "LOGIN PAGE URL"
    result = sesssion_requests.get(login_url)

    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0] # XPATH of hidden token

    payload = {
        "NAME TAG FOR LOGIN": "<USERNAME>",
        "NAME TAG FOR PASSWORD": "<PASSWORD>",
        "NAME OF THE TOKEN e.g : authenticity_token": "<TOKEN CODE>"
    }

    result = sesssion_requests.post(login_url, data=payload, headers=dict(referer=login_url))

    url = "URL TO SCRAP INFO FROM"
    result = sesssion_requests.get(url, headers=dict(referer=url))

    tree = html.fromstring(result.content)
    names = tree.xpath("XPATH TO INFORMATION TO SCRAP")

    print(names)

if __name__ == '__main__':
    main()