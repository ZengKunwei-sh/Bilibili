from Blbl.items import BlblItem
import scrapy
import requests
from lxml import etree

class BlblspiderSpider(scrapy.Spider):
    name = 'Blblspider'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://search.bilibili.com/all?keyword=机器学习']
    
    '''
    def parse_video(self, response): # 解析视频页面
        plays = response.xpath('//div[@class="video-data"]/span[@class="view"]/@title').extract()
        barrages = response.xpath('//div[@class="video-data"]/span[@class="dm"]/@title').extract()
        time = response.xpath('//div[@class="video-data"]/span[3]/text()').extract()
        likes = response.xpath('//span[@class="like"]/@title').extract()
        description = response.xpath('//div[@class="desc-info desc-v2"]/span/text()').extract()
        labels = response.xpath('//ul[@class="tag-area clearfix"]/li/div/a/span/text()').extract()
        comments = response.xpath('//span[@class="b-head-t results]/text()').extract()
        info = {
            'plays': plays,
            'barrages': barrages,
            'time': time,
            'likes': likes,
            'description': description,
            'labels': labels,
            'comments': comments,
        }
        return info'''
    def parse_video(self, url):
        response = requests.get(url)
        html = etree.HTML(response.text)
        try:
            plays = html.xpath('//div[@class="video-data"]/span[@class="view"]/@title')
        except:
            plays = ['']
        try:
            barrages = html.xpath('//div[@class="video-data"]/span[@class="dm"]/@title')
        except:
            barrages = ['']
        time = html.xpath('//div[@class="video-data"]/span[3]/text()')
        try:
            likes = html.xpath('//span[@class="like"]/@title')
        except:
            likes = ['']
        description = html.xpath('//div[@class="desc-info desc-v2"]/span/text()')
        if len(description) == 0:
            description = html.xpath('//div[@class="desc-info desc-v2 open"]/span/text()')
        labels = html.xpath('//ul[@class="tag-area clearfix"]/li/div/a/span/text()')
        labels = labels + html.xpath('//ul[@class="tag-area clearfix"]/li/a/span/text()')
        labels = labels + html.xpath('//ul[@class="tag-area clearfix"]/li/div/a/text()')
        # comments = html.xpath('//span[@class="b-head-t results"]/text()')
        info = {
            'plays': plays,
            'barrages': barrages,
            'time': time,
            'likes': likes,
            'description': description,
            'labels': labels,
            # 'comments': comments,
        }
        return info

    def parse(self, response): # 解析搜索页面
        videos = response.xpath('//ul[@class="video-list clearfix"]/li')
        for video in videos:
            item = BlblItem()
            item['title'] = video.xpath('./div/div/a[@class="title"]/@title').extract()
            item['author'] = video.xpath('./div/div/span[@title="up主"]/a/text()').extract()
            item['author_url'] = ['https:' + video.xpath('./div/div/span[@title="up主"]/a/@href').extract()[0]]
            item['length'] = video.xpath('./a/div/span[@class="so-imgTag_rb"]/text()').extract()
            # url需要稍作处理
            url = 'https:' + video.xpath('./div/div/a[@class="title"]/@href').extract()[0]
            item['url'] = [url]

            info = self.parse_video(url)

            item['plays'] = info['plays']
            item['barrages'] = info['barrages']
            item['likes'] = info['likes']
            item['description'] = info['description']
            item['labels'] = info['labels']
            item['time'] = info['time']
            # item['comments'] = info['comments']
            yield item
        
        pageNum = 50
        for page in range(2, pageNum+1):
            pageUrl = f'https://search.bilibili.com/all?keyword=python&page={page}'
            yield scrapy.Request(url=pageUrl, callback=self.parse)
