import scrapy
from scrapy import Field
from itemloaders.processors import Compose, TakeFirst,MapCompose,Compose

import urllib.parse as urlparse 
from urllib.parse import parse_qs 
from bs4 import BeautifulSoup

def parse_text(s):
    if(s):
        s = s[0]
        soup = BeautifulSoup(s,'html.parser')
        days = ['Sun','Mon','Tue','Wed','Fri','Sat','Thu']
        txt = soup.getText()
        for d in days:
            txt = txt.replace(d,f'\n{d}')
        return txt.replace('Open Now','').replace('Closed now','')

def parse_reviews(rev):
    print(rev)
    if(rev):
        return rev[0].strip('reviews')

def parse_lat(url):
    if(url):
        parsed = urlparse.urlparse(url[0])
        latlon = parse_qs(parsed.query)['center'] 
        lat = latlon[0].split(',')[0]
        return lat

def parse_lon(url):
    if(url):
        parsed = urlparse.urlparse(url[0])
        latlon = parse_qs(parsed.query)['center'] 
        lon = latlon[0].split(',')[-1]
        return lon

def parse_rev(rev):
    if(rev):
        return rev[0].strip("star rating")

def parse_cats(cat):
    if(cat):
        return ", ".join(cat)
class DrifterFoodItem(scrapy.Item):
    url = Field(output_processor=TakeFirst())
    g_restaurantID = Field()
    g_addressID = Field()
    competitor = Field(output_processor=TakeFirst())
    source = Field(output_processor=TakeFirst())
    restaurant_name = Field(output_processor=TakeFirst())
    country = Field(output_processor=TakeFirst())
    country_code = Field(output_processor=TakeFirst())
    city = Field(output_processor=TakeFirst())
    city_code = Field()
    address_street = Field(output_processor=TakeFirst())
    address_lat = Field(output_processor=TakeFirst(),input_processor=Compose(parse_lat))
    address_lon = Field(output_processor=TakeFirst(),input_processor=Compose(parse_lon))
    postal_code = Field()
    contact_phone = Field(output_processor=TakeFirst())
    contact_email = Field()
    contact_website = Field()
    average_basket_value = Field()
    tags = Field()
    g_reviews = Field()
    g_grade = Field()
    source_grade = Field(output_processor=TakeFirst(),input_processor=Compose(parse_rev))
    source_reviews = Field(output_processor=TakeFirst(),input_processor=Compose(parse_reviews))
    competitor_score = Field()
    opening_hours = Field(output_processor=TakeFirst(),input_processor=Compose(parse_text))
    social_facebook = Field()
    social_instagram = Field()
    categories = Field(output_processor=TakeFirst(),input_processor=Compose(parse_cats))
    promotion = Field()
    promotion_type = Field()
    scraping_time = Field(output_processor=TakeFirst())
    scraping_date = Field(output_processor=TakeFirst())
