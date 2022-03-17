# Scrapy settings for Blbl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import scrapy
BOT_NAME = 'Blbl'

SPIDER_MODULES = ['Blbl.spiders']
NEWSPIDER_MODULE = 'Blbl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Blbl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Blbl.middlewares.BlblSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'Blbl.middlewares.BlblDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Blbl.pipelines.BlblPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

IPPOOL = [{'ipaddr': '119.41.195.84:57114'},
        {'ipaddr': '120.41.135.127:57114'},
        {'ipaddr': '113.76.19.44:57114'},
        {'ipaddr': '59.33.136.134:57114'},
        {'ipaddr': '49.89.86.19:57114'},
        {'ipaddr': '101.18.113.242:57114'},
        {'ipaddr': '123.158.124.187:57114'},
        {'ipaddr': '117.60.24.72:57114'},
        {'ipaddr': '125.79.15.160:57114'},
        {'ipaddr': '222.211.147.210:57114'},
        {'ipaddr': '122.230.145.23:57114'},
        {'ipaddr': '123.162.202.103:57114'},
        {'ipaddr': '111.72.25.188:57114'},
        {'ipaddr': '220.160.229.238:57114'},
        {'ipaddr': '42.7.116.74:57114'},
        {'ipaddr': '59.62.127.183:57114'},
        {'ipaddr': '182.101.184.236:57114'},
        {'ipaddr': '115.207.60.194:57114'},
        {'ipaddr': '117.69.176.147:57114'},
        {'ipaddr': '113.75.149.5:57114'},
        {'ipaddr': '58.23.71.208:57114'},
        {'ipaddr': '115.226.240.211:57114'},
        {'ipaddr': '140.250.173.173:57114'},
        {'ipaddr': '122.230.153.232:57114'},
        {'ipaddr': '117.29.245.94:57114'},
        {'ipaddr': '218.1.200.110:57114'},
        {'ipaddr': '123.96.138.193:57114'},
        {'ipaddr': '180.103.18.66:57114'},
        {'ipaddr': '123.180.209.196:57114'},
        {'ipaddr': '175.10.140.80:57114'},
        {'ipaddr': '113.75.139.109:57114'},
        {'ipaddr': '113.75.134.177:57114'},
        {'ipaddr': '115.202.180.253:57114'},
        {'ipaddr': '114.218.89.230:57114'},
        {'ipaddr': '112.66.252.202:57114'},
        {'ipaddr': '223.215.75.148:57114'},
        {'ipaddr': '202.110.31.161:57114'},
        {'ipaddr': '61.154.197.200:57114'},
        {'ipaddr': '223.214.30.120:57114'},
        {'ipaddr': '42.176.135.217:57114'},
        {'ipaddr': '49.86.66.35:57114'},
        {'ipaddr': '113.124.85.156:57114'},
        {'ipaddr': '125.72.232.158:57114'},
        {'ipaddr': '144.255.250.212:57114'}]