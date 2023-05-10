import scrapy
from urllib.parse import urlencode
import requests
import json
from .test import get_verification_token
from ..items import WaikikiCrawlerItem

class WaikikiSpider(scrapy.Spider):
    name = "waikiki"
    allowed_domains = ["lcwaikiki.com"]

    def get_pages(self):
        url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/CategoryGroup/CategoryGroupPageData/?"

        querystring = {"xhrKeys":"CountryCode,CategoryGroup,IsOutletCategoryGroup,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","CategoryGroup":"giyim","IsOutletCategoryGroup":"False","ProductGroup":"2","ProductGender":"2","PageIndex":"1"}
        headers = {
            #"cookie": "_abck=8CFAC83E172DE695F5771E725C05D67A~-1~YAAQGtJ6XB4EMPCHAQAAmmOa9QlGsixYXdMqSScHQAzjX33jV%2FFGJEAA5JAxr5plh9WREwz5FSuRIjrBs52OD9b%2BE1hGAgTvKYII2rU7ZiXssx8k3Mm0%2Fc39k2v6mqx0wCmjjNQgohrgyqbJwEaGbDscw8ECKl0X5zvoDQO8vUlX0gTvBRlWumS8R82gI21lP%2Fi0nTe0tuG8URyH%2F8%2B20MSdXFLvKEw6JBhuWpuCGSucrzstffKIM0r13xI9xpYDqB8FcZYyp5lwZ6eGRtwl8pqyV88pNMjIHYGNbCo1WSUnykuOiwuOVxmpllW39U8AjRMspMExaveSrG8SPBe9ilLOpkbddKlKnn9lsp433bRpavUI2ssBtYhIJoiJpf6y%2B%2FJJNR37FOEvkb1Ix3n1YKCCsKgZQvA%2BWx12UQ%3D%3D~-1~-1~-1; ak_bmsc=AB5BE64194387B432EEBB256A9287F03~000000000000000000000000000000~YAAQGtJ6XFodMPCHAQAAiMyd9RPJsztxtNE6mBBC79qfi49ZxIms6b7UpuXSaQDqvZ4yXcG8Os%2B%2F5qcvYJwaTZV3WDsB4YN34urg1iP9SryVMjrueY3qXT%2BI7dJu%2BXzjnI6JSLKQJAx3gkIFGpmZJdT62WVa0AUM32Qa8W621bCcvC9PNQ%2BXrbgPjVxFMamQ35o%2BAjnUat5ADib%2By8xhNKIsO46RewFmb1MXLIdU9ED8qSs6%2BrNVA9tmCw1i16LAdDiP3TaAikcHxs6kfHoXsayCJfyHojX3hRXZ4UJTX4cmS9xo2I3rdi%2FoSst5V4Bmk%2F3kXtjfX0ypS1eShz1BRf8DqmFN0syYKgbdDt07D7ONPF%2BPcr2sa%2FD7hNknehuYWfFmbm9BnJDBxomAHy%2BPt9pojHBuo7DLoCKz0A%3D%3D; CustomRequestVerificationToken=Cmprw0FLCQvqjuB87kLW8Xt4DpQv21sGd0qqv0B9Y7O-Wi37-WWsvz-oWEAlFZnlKLcuPA2; ASP.NET_SessionId=rgkixpx4sx2zruerpcp4z4iv; visitorId=bcb28855-861f-47d4-9cce-6788c9077bba; guestSessionId=1c71679e-53dc-4add-8eaf-c23c83108645; bm_sz=E933ABF6A46C4C33EB457DC6C06DE95C~YAAQGtJ6XCAEMPCHAQAAmmOa9RMLqnfBCzkz1tEwVx1kLnd3mKEX91Suy3oWO95CBMDwn89HUyQmrXPvKFgfZwu1ONDesp9sFG%2B1Mbn9KG533EcW0zcdwaI7rUTgCo2YjIEtjI2%2BRNc%2FNfwk8aw0e1%2Bglg8T59aiZoomwtp2z1sDGn89X%2Fi7vbHGPztRhe14hFoTUCARGfOQixirVgoPpPka%2BIMvq88eLyLM41w3otNeH2KGfM9%2F%2FygL5iNIempLXngijSQAfilhxtYvEDLov1Xrj73Yi39CljM3CcRvbNJ3k8rTc00%3D~3293494~3616838",
            "authority": "www.lcwaikiki.com",
            "accept": "application/json, text/plain, */*",
            "adrum": "isAjax:true",
            "content-type": "application/json",
           #"customrequestverificationtoken": "qe7FxOpa9sHwZzT0hmoq-Z6itUGyoIbbcJXYfAq5jmpCHcpHITQDxSAS74O34CR0ZLyXWA2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }
        link = url + urlencode(querystring)
        r = requests.post(link,headers=headers)
        print(r.status_code)
        #r = scrapy.Request(link,method='POST')
        page_data = r.json()
        
        total_pages=page_data['PageView']['PageCount']
            
        #current_page=page_data['PageView']['CurrentPageIndex']

        return total_pages


    def start_requests(self):
        total_pages = self.get_pages()

        for i in range(1,total_pages+1):
            
        
            url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/CategoryGroup/CategoryGroupPageData/?"

            querystring = {"xhrKeys":"CountryCode,CategoryGroup,IsOutletCategoryGroup,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","CategoryGroup":"giyim","IsOutletCategoryGroup":"False","ProductGroup":"2","ProductGender":"2","PageIndex":f"{i}"}
        
            link = url + urlencode(querystring)

            request = scrapy.Request(method ="POST", url=link, callback= self.parse_api)
            

            
            yield request
    def parse_api(self, response):
        data = response.json()
        total_items=data['CatalogList']['ItemCount']
        current_page=data['PageView']['CurrentPageIndex']
        self.logger.info(f'----CURRENT PAGE INDEX--- {current_page}')
        for i in data['CatalogList']['Items']:
            url = i['ModelUrl']
            #print(url)
            old_price = i['Price']
            old_price=old_price.replace('TL','').replace(',','.').strip()
            list_price = i['OldPrice'].replace('TL','').replace(',','.').strip()
            
            brand =i['BrandPropertyDescription']
            store = 'LC Waikiki'
            color_counts = i['OptionColorCount']
            option_id = i['OptionId']
            model_id =i['ModelId']
            product_code =i['OzelKodRenkKod']
            qty = i['AvailableStock']
            product_group= i['ProductGroup']
            category =i['Category']
            description=i['ProductDescription']
            brand_description = i['BrandPropertyDescription']
            name = brand_description + ' ' + description
            meta = {
                
                'category': product_group + "/" + category,
                'group_code':product_code.split('-')[0],
                'name': name,
                'product_code':product_code,
                'price':old_price,
                'list_price':list_price,
                'brand':brand,
                'description':description,
                
                }

            yield scrapy.Request(url='https://www.lcwaikiki.com'+url, callback=self.parse_product_color_sizes,meta=meta)

    def parse_product_color_sizes(self,response):
        item_yield = WaikikiCrawlerItem()
        items = response.meta
        current_color=response.xpath("//a[@class='color-option active']/div/div/@alt").get()
        item_yield['color'] = current_color
        color_count=response.meta.get('color_counts')
        item_yield['scrap_url'] = response.url
        
        item_yield['description'] = items['description']
        item_yield['category'] = items['category']
        item_yield['group_code'] = items['group_code']
        item_yield['name'] = items['name']
        item_yield['price'] = items['price']
        item_yield['list_price'] = items['list_price']
        item_yield['brand'] = items['brand']
        sizes=response.xpath('//meta[@name="Size"]/@content').get()
        size_list=sizes.split(',')  
        size_id = response.xpath('//meta[@name="SizeId"]/@content').get()
        if size_id == None:
            size_id = response.xpath('//meta[@name="SizeHeightId"]/@content').get()
            
        size_id_list = size_id.split(',')
        for counter,id_ in enumerate(size_id_list):
            id_ = id_.replace('-','_')
            stock_qty=response.xpath(f'//meta[@name="StockInfos_{id_}"]/@content').get()
            size=size_list[counter]
            
            item_yield['size'] = size
            item_yield['product_code'] = items['product_code'] + '-' + current_color + ',' + size
            
            item_yield['qty'] = stock_qty
            
            for counter,img in enumerate(response.xpath('//div[@class="col-xs-6"]/img/@data-large-img-url').getall(),start=1):
                if counter <= 15:
                    item_yield[f'image{counter}'] = img
            
            yield item_yield
            
            
            
        colors=response.xpath('//a[@class="color-option"]/@href').getall()
        for color_url in colors:
            
          
  
            yield scrapy.Request(url="https://www.lcwaikiki.com" + color_url,callback=self.parse_product_color_sizes,meta=items)

            

    # def parse_color_options(self,response):
    #     items = response.meta
        