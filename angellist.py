import json
import re
import requests
import scrapy


class StartupCrawler(scrapy.Spider):
    name = 'angellist'
    start_urls = []
    session_cookie = ''

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    }

    def __init__(self):
        # Generate ajax urls
        pp = PreProcessor()
        self.start_urls = pp.ajaxURLList()
        self.session_cookie = pp.session_cookie

    def parse(self, response):
        # Extract HTML from JSON
        obj = json.loads(response.text)

        # Create new selector from extracted html
        selector = scrapy.Selector(text=obj['html'], type="html")

        for company in selector.css('div.startup'):
            details_url = response.urljoin(company.css('a.startup-link::attr("href")').extract_first())
            # yield {'url': details_url}

            if details_url is not None:
                yield scrapy.Request(details_url, cookies={'_angellist': self.session_cookie}, callback=self.parse_company)

    def parse_company(self, response):
        result = {}
        result['company_name'] = response.css('h1.s-vgBottom0_5::text').extract_first()
        result['url'] = response.url
        result['area'] = response.css('a.tag::text').extract_first()
        result['stage'] = response.css('div.type::text').extract_first()
        result['employees'] = response.css('span.js-company_size::text').extract_first()

        '''

        here should add some code to scrapy data from details page.
        I already start scrapy the 'company_name'.

        '''
        yield result


class PreProcessor():
    # Headers
    req_headers = {}
    session_cookie = ''

    # Maximum number of pages to fetch, set 1 just for test convinent
    total_pages = 1

    def ajaxURLList(self):
        url_list = []

        # Get headers
        self.getHeaders()

        for page in range(1, self.total_pages + 1):
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

            if 'ids' not in params:
                # print(res.text)
                break

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

            # Print progress
            print('Generating AJAX url: %d / %d' % (page, self.total_pages))

        return url_list

    def getHeaders(self):
        # Send request
        # cookie 'de7af8c01bea49941f6fab2f49e79b55' should be replaced by your own cookie when you login
        res = requests.get('https://angel.co/companies', cookies={'_angellist': 'bb2eca11455d6d27e3d3fa0b1310572a'})

        # Get cookie
        self.req_headers['cookie'] = '_angellist=' + res.cookies['_angellist']
        self.session_cookie = res.cookies['_angellist']

        # Get CSRF token
        self.req_headers['X-CSRF-Token'] = re.search('<meta content="(.+?)" name="csrf-token" />', res.text).groups()[0]
