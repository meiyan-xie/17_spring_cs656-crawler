import json
import re
import requests
import scrapy


class StartupCrawler(scrapy.Spider):
    name = 'glassdoor'
    start_urls = []

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    def __init__(self):
        # Generate ajax urls
        pp = PreProcessor()
        self.start_urls = pp.ajaxURLList()

    def parse(self, response):
        # Extract HTML from JSON
        obj = json.loads(response.text)

        # Create new selector from extracted html
        selector = scrapy.Selector(text=obj['html'], type="html")

        for company in selector.css('div.startup'):
            details_url = response.urljoin(company.css('a.startup-link::attr("href")').extract_first())
            yield {'url': details_url}

        # for  in response.css('div.panel-heading'):
        #     details_url = response.urljoin(company.css('a::attr("href")').extract_first())

        #     if details_url is not None:
        #         yield scrapy.Request(details_url, callback=self.parse_company)


class PreProcessor():
    # Headers
    req_headers = {}

    def ajaxURLList(self):
        url_list = []

        # Get headers
        self.getHeaders()

        for page in range(1, 5):
            search_req_body = {'filter_data[company_types][]': 'Startup',
                               'filter_data[stage][]': 'Seed',
                               'filter_data[stage][]': 'Series A',
                               'filter_data[stage][]': 'Series B',
                               'filter_data[stage][]': 'Series C',
                               'sort': 'Total Raised',
                               'page': page}

            # Get parameters for next request
            res = requests.post('https://angel.co/company_filters/search_data',
                                headers=self.req_headers,
                                data=search_req_body)

            # Parse parameters from json
            params = json.loads(res.text)

            # Generate url
            gen_url = ''

            # Add parameters
            for key in params:
                if key != 'ids':
                    gen_url += '&' + key + '=' + str(params[key])

            # Add ids
            gen_url_ids = ''
            for _id in params['ids']:
                gen_url_ids = gen_url_ids + '&ids%5B%5D=' + str(_id)

            gen_url += gen_url_ids

            # Append hostname
            gen_url = 'https://angel.co/companies/startups?' + gen_url[1:]

            # Append to result
            url_list.append(gen_url)

        return url_list

    def getHeaders(self):
        # Send request
        res = requests.get('https://angel.co/companies')

        # Get cookie
        self.req_headers['cookie'] = '_angellist=' + res.cookies['_angellist']

        # Get CSRF token
        self.req_headers['X-CSRF-Token'] = re.search('<meta content="(.+?)" name="csrf-token" />', res.text).groups()[0]
