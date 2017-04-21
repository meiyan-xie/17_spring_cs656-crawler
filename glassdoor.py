import scrapy


class StartupCrawler(scrapy.Spider):
    name = 'glassdoor'
    start_urls = ['https://www.glassdoor.com/Award/Best-Small-and-Medium-Companies-to-Work-For-LST_KQ0,43.htm']

    def parse(self, response):
        for company in response.css('div.panel-heading'):
            details_url = response.urljoin(company.css('a::attr("href")').extract_first())

            if details_url is not None:
                yield scrapy.Request(details_url, callback=self.parse_company)

    def parse_company(self, response):
        result = {}
        result['company_name'] = response.css('h1::text').extract_first()

        for infoEntity in response.css('div.infoEntity'):
            result[infoEntity.css('label::text').extract_first()] = infoEntity.css('span.value::text').extract_first()

        yield result
