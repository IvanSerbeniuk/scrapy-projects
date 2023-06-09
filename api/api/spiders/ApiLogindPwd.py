import scrapy
from scrapy import FormRequest


class ApilogindpwdSpider(scrapy.Spider):
    name = "ApiLogindPwd"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/login"]

    def parse(self, response):
        csrf_token = response.xpath('//body/div/form/input[1]/@value').get()
        yield FormRequest.from_response(
            response,
            formxpath='//form',
            formdata={
                'csrf_token':csrf_token,
                'username': 'admin',
                'password': 'admin',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        if response.xpath("//a[@href='/logout']/text()").get():
            print('Successfully logged in')
