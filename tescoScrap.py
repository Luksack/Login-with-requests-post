import requests
from lxml import html
import csv


class ProductScrapper:
    def scrap(self):
        with open('TescoUrls.txt', 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file]
            urls.remove('\ufeff')

        for url in urls:
            try:
                request = requests.get(url)
                content = html.fromstring(request.content.decode('utf-8', 'ignore'))
                print(url)

                name = content.xpath("//*[@id='main']/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/section/div/h1/text()")
                print(str(name[0]).strip())

                product_id = content.xpath(
                    "//*[@id='main']/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/section/div/div/form/input[3]/@value")
                print(product_id)

                price = content.xpath(
                    '//*[@id="main"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/section/div/div/form/div/div[1]/div[1]/div/div/span/span[1]/text()')
                print(price)

                image = content.xpath(
                    '//*[@id="main"]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/section/div/span/span/img/@src')
                print(image)

                with open('tesco.csv', 'a', encoding='utf-8') as output:
                    titles = ['Name', 'ID', 'Price', 'Image']
                    writer = csv.DictWriter(output, fieldnames=titles)
                    writer.writerow({
                        'Name': name[0],
                        'ID': product_id[0],
                        'Price': price[0],
                        'Image': image[0]
                    })
            except:
                pass


scrap = ProductScrapper()
scrap.scrap()
