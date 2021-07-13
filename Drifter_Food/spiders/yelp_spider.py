import scrapy
import os
import urllib.parse as urlparse
from scrapy.http import JsonRequest
from Drifter_Food.config_func import FileNaming, config_import_reader, remove_duplicates
import pandas as pd
import os
import urllib

df =  pd.read_csv('Cities.csv',sep=",", encoding='utf-8')       

class WoltLatlonSpider(scrapy.Spider):
    
    name = 'yelp_spider'
    competitor = 'yelp'
    config_import = config_import_reader(competitor)
    code = config_import["code"]
    filenaming = FileNaming(code)

    tags=['restaurants','burgers','japanese','chinese','mexican','italian','thai']

    custom_settings = {'FEED_URI': f"1-target-urls/{filenaming.spider_output_final()}",
                       'FEED_EXPORT_FIELDS': ["link","city_code","city_name","country_code","country_name"],
                       'ROBOTSTXT_OBEY': False}
    def start_requests(self):
        if os.path.isfile(f"3-clean-data/{self.filenaming.spider_output_raw()}"):
            remove_duplicates(self.filenaming.spider_output_raw(),
                              self.filenaming.spider_output_final())
        
        all_urls = []
        for i in range(0,len(df)):
            input_city_data = df.loc[i].to_dict()
            for tag in self.tags:
                quer = dict()
                quer['find_loc'] = input_city_data.get('city_name')
                quer['cflt'] = tag

                # quer['start'] = 10  
                f = dict()

                f['city_search_url'] = "https://www.yelp.com/search?" + urllib.parse.urlencode(quer) 
                f['city_code'] = input_city_data.get('city_code')
                f['city_name'] = input_city_data.get('city_name')
                f['country_code'] = input_city_data.get('country_code')
                f['country_name'] = input_city_data.get('country_name')
                all_urls.append(f)

        for u in all_urls:
            url = u['city_search_url']
            
            yield scrapy.Request(url = url, meta = u,callback= self.parse_last_page)
            # yield scrapy.Request('http://checkip.dyndns.org/', callback=self.check_ip)

    def check_ip(self, response):

        pub_ip = response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
        print ("My public IP is: " + pub_ip)
        
 
    def parse_last_page(self, response):

        last_page = response.xpath("//div[@role='navigation']/div/span/text()").get()
        if(last_page):
            last_page = int(last_page.split('of')[-1]) 
        
        print(f'Last Page No is {last_page}')

        for i in range(0, last_page):
            search_page_url = response.request.url + f"&start={i*10}"


            yield scrapy.Request(url=search_page_url, meta=response.request.meta, callback= self.parse_restaurant_links)
        
    def parse_restaurant_links(self, response):
        data = response.request.meta
        restaurant_links = response.xpath("//h4/span/a/@href").getall()
        if(restaurant_links):
            restaurant_links = ["https://www.yelp.com" + rl for rl in restaurant_links]
        
        unwanted = ["city_search_url","download_timeout","download_slot","download_latency","depth"]
        for uw in unwanted:
            data.pop(uw)
        for restaurant_link in restaurant_links:
            data['link'] = restaurant_link

            yield data

    
