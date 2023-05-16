from waikiki_crawler.spiders.waikiki import WaikikiSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    settiings=get_project_settings()
    process = CrawlerProcess(settings=settiings)
    process.crawl(WaikikiSpider)
    process.start()
    
if __name__ == '__main__':
    main()
