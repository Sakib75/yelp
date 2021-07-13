# -*- coding: utf-8 -*-

# Scrapy settings for Drifter_Food project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Drifter_Food'

SPIDER_MODULES = ['Drifter_Food.spiders']
NEWSPIDER_MODULE = 'Drifter_Food.spiders'

FEED_FORMAT = 'csv'
FEED_EXPORT_ENCODING = 'utf-8-sig'

PROXY_USERNAME = 'mikedrifter'
PROXY_USER_PASS = 'b29358-c1963e-f0bd5e-d7db63-d0e632'
PROXY_POOL = ["209.205.212.34:222",
              "209.205.212.34:1200",
              "209.205.212.34:1201",
              "209.205.212.34:1202",
              "209.205.212.34:1203",
              "209.205.212.34:1204",
              "209.205.212.34:1205",
              "209.205.212.34:1206",
              "209.205.212.34:1207",
              "209.205.212.34:1208"]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Drifter_Food (+http://www.yourdomain.com)'


# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
#     'Drifter_Food.middlewares.RandomUserAgentMiddleware': 400,
#     'Drifter_Food.middlewares.CustomProxyMiddleware': 350,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
# }

USER_AGENT_LIST = 'user-agents.txt'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
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
#    'Drifter_Food.middlewares.DrifterFoodSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Drifter_Food.middlewares.RandomUserAgentMiddleware': 150,
   'Drifter_Food.middlewares.CustomProxyMiddleware': 350,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# ITEM_PIPELINES = {
#    'Drifter_Food.pipelines.DrifterFoodPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
