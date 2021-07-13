from datetime import datetime
from itemloaders import ItemLoader
import scrapy
from Drifter_Food.config_func import FileNaming, config_import_reader, remove_duplicates
import os 
import csv
from ..items import DrifterFoodItem
from datetime import datetime


class YelpCrawlerSpider(scrapy.Spider):
    name = 'yelp_scraper'
    competitor = "yelp"
    now = datetime.now()
    config_import = config_import_reader(competitor)

    code = config_import["code"]

    filenaming = FileNaming(code)

    custom_settings = {'FEED_URI': f"2-raw-data/{filenaming.scraper_output_raw()}",
                       'FEED_EXPORT_FIELDS': [field for field in config_import['xpaths'][0].keys()],
                       'ROBOTSTXT_OBEY': False}

    def start_requests(self):
        if os.path.isfile(f"3-clean-data/{self.filenaming.spider_output_raw()}"):
            remove_duplicates(self.filenaming.spider_output_raw(),
                              self.filenaming.spider_output_final())

        with open(f"1-target-urls/{self.filenaming.spider_output_final()}", newline='', encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for restaurant in reader:

                yield scrapy.Request(url=restaurant["link"],meta=restaurant ,callback= self.parse)
                # yield scrapy.Request('http://checkip.dyndns.org/', callback=self.check_ip)
    def check_ip(self, response):
        pub_ip = response.xpath('//body/text()').re('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')[0]
        print ("My public IP is: " + pub_ip)
        
    def parse(self, response):
        xpaths = self.config_import["xpaths"][0]

        meta = response.request.meta

        loader = ItemLoader(item=DrifterFoodItem(), selector= response, response=response)

        loader.add_value("url",response.request.url)
        loader.add_value("competitor","yelp")
        loader.add_value("source","sourcing_yelp")
        loader.add_xpath("restaurant_name","//h1[@class='css-11q1g5y']/text()")
        loader.add_xpath("country",meta['country_name'])
        loader.add_xpath("country_code",meta['country_code'])
        loader.add_xpath("city",meta['city_name'])
        loader.add_xpath("city_code",meta['city_code'])
        loader.add_xpath("address_street","//a[text()='Get Directions']/parent::p/parent::div/p[@class=' css-chtywg']/text()")

        loader.add_xpath("address_lat","//img[contains(@src,'https://maps.googleapis.com')]/@src")
        loader.add_xpath("address_lon","//img[contains(@src,'https://maps.googleapis.com')]/@src")
        loader.add_xpath("contact_phone","//div[1]/div/div/p[@class=' css-1h1j0y3']/text()")
        loader.add_xpath("source_grade","//h1/parent::div/parent::div//div[contains(@class,'i-stars__373c0__1T6rz')]/@aria-label")
        loader.add_xpath("source_reviews","//div/span[@class=' css-bq71j2']/text()")


        loader.add_xpath("opening_hours","//table[contains(@class,'hours-table__373c0__1S9Q_')]")
        loader.add_xpath("categories","//span[@class=' css-bq71j2']/a[@class='css-166la90']/text()")
        loader.add_value("scraping_time",self.now.strftime("%m/%d/%Y"))
        loader.add_value("scraping_date",self.now.strftime("%H:%M:%S"))

        yield loader.load_item()
