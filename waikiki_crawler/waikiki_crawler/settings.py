# Scrapy settings for waikiki_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "waikiki_crawler"

SPIDER_MODULES = ["waikiki_crawler.spiders"]
NEWSPIDER_MODULE = "waikiki_crawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT =  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
LOG_FILE = "logs.txt"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 300

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
# DEFAULT_REQUEST_HEADERS = {
#     "cookie": "ak_bmsc=218060B88CD725B077C1376A3A679B45~000000000000000000000000000000~YAAQL77XF89h8+CHAQAA/GZ34xP20xJxrPunsf4X+ZzUtTBnm6qGSdBI4uK97mHRlozAUX3cm/RawsfcUbJPVLi7Ih6yImdrYcHqHXpOjb4HbNVqjbcS3qfjNT49G9BRitVnX56r7GAbJhmBNCEMQcLFcPIDSPDtkxKzn96wXjGkbj+RQuIJRzP54pOM7t32d9RA/r8mOHtSuGTnq5yfq9SJOfFNFJSKpk7kCXAyITXpKX1ZBagf+bC48ftzjCxOeFMNCtTk86puXYE89Nbtc33S5EH6K9WoUoXplJhIP1XmIGGqaEbXzZAtoOvEyxB/WaEqEubnBjyJQNcenZDtvowpvIPRHbMlkIHIvOkYRfCuVRHR/4kJ5lHTaWqu1eaMKxbqsvWFzMVgK06c; bm_sz=462666EA5C0192BF01234DE904367155~YAAQL77XF9Bh8+CHAQAA/GZ34xPHb9XyYvWZAfzrnglxMVNHJr19WxfxqQP7eh5CYG0zeqWjo+bH0DqLzJC5DuxbS9Q3YmgxYzYipmittRXZXhoB2PEyfESYXecd6kDF/g1Py2eeyErXmNewL7YvS2tuhGKyx/uGUjgTTl7h5zubEBsntqIY8e7Gr0rdbdW+r/9tWA0Ym4h4OBarO+y4n+YfD3ebNsQAIdst4cpIc8EQx1GnsXZb79PauwsQfBWwyuiDHojjavnfDX2AIixdytksf/LmvgayBSrEDRzs8wdxBCjnk5s=~4605489~3291443; ASP.NET_SessionId=rxq4iqzxrn40bpggc0qz0qs1; visitorId=1ce30f4d-a511-4344-a41f-11ae49515386; guestSessionId=c0576056-9cdc-43cc-b7c3-4d1f3347cc41; ADRUM=s=1683148527367&r=https^%^3A^%^2F^%^2Fwww.lcwaikiki.com^%^2Ftr-TR^%^2FTR^%^3F0; _abck=8CFAC83E172DE695F5771E725C05D67A~0~YAAQL77XF9pt8+CHAQAAxEB54wmLF8XM2CLuB06JvT+BPTeadBUu8OsINqs+JAh1rM6TeYs5/vtIyUgQVkakV2peAwWT1Gd1ZveFiAEBwfxxU9cEbzvp4AbrquPTT7TdXSR2X2jxo5V2XveOG5z3EUhDYlBdQvyv95boMPcNuQKAQ9pUGkIz2NjUEDr8Ng7+a0AKDEIHkXAORvMiHhinuZMaFYPzkBqZDY1Gqijk8XVy/PPFd+f6ZkaI42wLUZjtbdfqIn/P980rV9g3SAEBpbBLAg8rQVZ4FiozTluc3fAPGdc+dSROTYJ/IMuF3hPlyCIJaqZQTuRQim18hXGgj0LoMIFSALF5AGg8VtDr52CHm5rTj7PFa4WRo0y5Uo5hDywHwEl9aASFP2j6iiPp4K57J2uQOD4xWCsb~-1~-1~-1; explorebodyinfo=true; CustomRequestVerificationToken=vbslmdZX9BIJEOrY8-Tfo5iO6twPVBjrJhenu_BEpbOAttepGo7bU3TVJsYnBqhnVYUCfQ2; bm_sv=559BEBAC98958EBEA1938E1B340E84C5~YAAQbr7XF/2+edmHAQAA0A184xNUHFCOCipaYPbi2ca3TvoOoJJtTC9jjlVYtqdhHJh+2jWyBBBLWm3iuK7+iZho2me438F89i7l0VWdGHrXNm3Q9vGTaQswJDIXdldZ71GxiIFIp+ygMA4HYn4Rr3zSqtKZZ7dmsj3IlfaknOOIiUbIGkZOotqJpjuPpztgMTl5o5t+tgKAJxnWYfRJJQgem/i5DllWce/XaGFqcXMcmvtBjjxFFA6I/jGHLSxLM3z3Jw==~1",
#     "authority": "www.lcwaikiki.com",
#     "accept": "application/json, text/plain, */*",
#     "accept-language": "en-US,en;q=0.7",
#     "adrum": "isAjax:true",
#     "cache-control": "no-cache",
#     "content-type": "application/json",
#     "customrequestverificationtoken": "L5COV8GCdB3UalFJNkJ7B1uJ0syzQVs72te2HYNnDm88xc6UKva2ct-Jvg93yovbBse4jQ2",
#     "origin": "https://www.lcwaikiki.com",
#     "pragma": "no-cache",
#     "referer": "https://www.lcwaikiki.com/tr-TR/TR/kadin/giyim?PageIndex=2",
#     "sec-ch-ua": "^\^Chromium^^;v=^\^112^^, ^\^Brave^^;v=^\^112^^, ^\^Not:A-Brand^^;v=^\^99^^",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "^\^Windows^^",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "sec-gpc": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "waikiki_crawler.middlewares.WaikikiCrawlerSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "waikiki_crawler.middlewares.WaikikiCrawlerDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "waikiki_crawler.pipelines.WaikikiCrawlerPipeline": 300,
#}

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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


FEED_EXPORT_FIELDS = [
    'scrap_url',
    'category',
    'brand',
    'name',
    'product_code',
    'group_code',
    'price',
    'list_price',
    'qty',
    'color',
    'size',
    'description',
    'image1',
    'image2',
    'image3',
    'image4',
    'image5',
    'image6',
    'image7',
    'image8',
    'image9',
    'image10',
    'image11',
    'image12',
    'image13',
    'image14',
    'image15',
]