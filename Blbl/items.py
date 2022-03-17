# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class BlblItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    url = scrapy.Field()
    plays = scrapy.Field()
    length = scrapy.Field()
    time = scrapy.Field()
    barrages = scrapy.Field()
    likes = scrapy.Field()
    #coins = scrapy.Field()
    #collects = scrapy.Field()
    #shares = scrapy.Field()
    comments = scrapy.Field()
    description = scrapy.Field()
    labels = scrapy.Field()