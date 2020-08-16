import scrapy


class OffersSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['www.tinydeal.com']
    start_urls = ['https://www.tinydeal.com/specials.html']

    def parse(self, response):
        
        for product in response.xpath("//ul[@class='productlisting-ul']/div/li"):

            yield{
                'title':product.xpath(".//a[2]/text()").get(),
                'url':product.xpath(".//a[1]/@href").get(),
                'discount':product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'actual':product.xpath(".//div[@class='p_box_price']/span[2]/text()").get()
            }
        page=response.xpath("//a[@class='nextPage']/@href").get()

        if page:
            yield scrapy.Request(url=page,callback=self.parse)