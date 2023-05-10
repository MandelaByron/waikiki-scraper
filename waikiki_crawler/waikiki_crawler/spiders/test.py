import requests
session = requests.Session
def get_verification_token(model,option):
    with session() as s:

        url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/model/quicklook"

        payload = {
            "selectedModelId": model,
            "selectedOptionId": option
        }
        headers = {
            "cookie": "_abck=8CFAC83E172DE695F5771E725C05D67A~-1~YAAQGtJ6XB4EMPCHAQAAmmOa9QlGsixYXdMqSScHQAzjX33jV%2FFGJEAA5JAxr5plh9WREwz5FSuRIjrBs52OD9b%2BE1hGAgTvKYII2rU7ZiXssx8k3Mm0%2Fc39k2v6mqx0wCmjjNQgohrgyqbJwEaGbDscw8ECKl0X5zvoDQO8vUlX0gTvBRlWumS8R82gI21lP%2Fi0nTe0tuG8URyH%2F8%2B20MSdXFLvKEw6JBhuWpuCGSucrzstffKIM0r13xI9xpYDqB8FcZYyp5lwZ6eGRtwl8pqyV88pNMjIHYGNbCo1WSUnykuOiwuOVxmpllW39U8AjRMspMExaveSrG8SPBe9ilLOpkbddKlKnn9lsp433bRpavUI2ssBtYhIJoiJpf6y%2B%2FJJNR37FOEvkb1Ix3n1YKCCsKgZQvA%2BWx12UQ%3D%3D~-1~-1~-1; ak_bmsc=AB5BE64194387B432EEBB256A9287F03~000000000000000000000000000000~YAAQGtJ6XFodMPCHAQAAiMyd9RPJsztxtNE6mBBC79qfi49ZxIms6b7UpuXSaQDqvZ4yXcG8Os%2B%2F5qcvYJwaTZV3WDsB4YN34urg1iP9SryVMjrueY3qXT%2BI7dJu%2BXzjnI6JSLKQJAx3gkIFGpmZJdT62WVa0AUM32Qa8W621bCcvC9PNQ%2BXrbgPjVxFMamQ35o%2BAjnUat5ADib%2By8xhNKIsO46RewFmb1MXLIdU9ED8qSs6%2BrNVA9tmCw1i16LAdDiP3TaAikcHxs6kfHoXsayCJfyHojX3hRXZ4UJTX4cmS9xo2I3rdi%2FoSst5V4Bmk%2F3kXtjfX0ypS1eShz1BRf8DqmFN0syYKgbdDt07D7ONPF%2BPcr2sa%2FD7hNknehuYWfFmbm9BnJDBxomAHy%2BPt9pojHBuo7DLoCKz0A%3D%3D; CustomRequestVerificationToken=Cmprw0FLCQvqjuB87kLW8Xt4DpQv21sGd0qqv0B9Y7O-Wi37-WWsvz-oWEAlFZnlKLcuPA2; ASP.NET_SessionId=rgkixpx4sx2zruerpcp4z4iv; visitorId=bcb28855-861f-47d4-9cce-6788c9077bba; guestSessionId=1c71679e-53dc-4add-8eaf-c23c83108645; bm_sz=E933ABF6A46C4C33EB457DC6C06DE95C~YAAQGtJ6XCAEMPCHAQAAmmOa9RMLqnfBCzkz1tEwVx1kLnd3mKEX91Suy3oWO95CBMDwn89HUyQmrXPvKFgfZwu1ONDesp9sFG%2B1Mbn9KG533EcW0zcdwaI7rUTgCo2YjIEtjI2%2BRNc%2FNfwk8aw0e1%2Bglg8T59aiZoomwtp2z1sDGn89X%2Fi7vbHGPztRhe14hFoTUCARGfOQixirVgoPpPka%2BIMvq88eLyLM41w3otNeH2KGfM9%2F%2FygL5iNIempLXngijSQAfilhxtYvEDLov1Xrj73Yi39CljM3CcRvbNJ3k8rTc00%3D~3293494~3616838",
            "authority": "www.lcwaikiki.com",
            "accept": "application/json, text/plain, */*",
            "adrum": "isAjax:true",
            "content-type": "application/json",
            "customrequestverificationtoken": "qe7FxOpa9sHwZzT0hmoq-Z6itUGyoIbbcJXYfAq5jmpCHcpHITQDxSAS74O34CR0ZLyXWA2",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        }

        response = s.post(url=url,json=payload,headers=headers)

        print(response.status_code)

        
        return response.json()
#print(get_verification_token())
mens_querystring = {"xhrKeys":"CountryCode,CategoryGroup,IsOutletCategoryGroup,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","CategoryGroup":"giyim","IsOutletCategoryGroup":"False","ProductGroup":"1","ProductGender":"1","PageIndex":"2"}

girl_child_querystring = {"xhrKeys":"CountryCode,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","ProductGroup":"4","ProductGender":"2","PageIndex":"2"}

boy_child_querystring = {"xhrKeys":"CountryCode,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","ProductGroup":"4","ProductGender":"1","PageIndex":"2"}

girl_baby = querystring = {"xhrKeys":"CountryCode,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","ProductGroup":"5","ProductGender":"2","PageIndex":"2"}

boy_baby_querystring = {"xhrKeys":"CountryCode,ProductGroup,ProductGender,xhrKeys","CountryCode":"TR","ProductGroup":"5","ProductGender":"1","PageIndex":"2"}

shoes_querystring = {"xhrKeys":"CountryCode,Tag,xhrKeys","CountryCode":"TR","Tag":"tum-ayakkabi-urunleri","PageIndex":"4"}
url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/Tag/TagPageData"

url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/Tag/TagPageData"

accessories_querystring = {"xhrKeys":"CountryCode,Tag,xhrKeys","CountryCode":"TR","Tag":"tum-aksesuar-urunleri-2022","PageIndex":"2"}

url = "https://www.lcwaikiki.com/tr-TR/TR/ajax/Tag/TagPageData"

ev_life_querystring = {"xhrKeys":"CountryCode,Tag,xhrKeys","CountryCode":"TR","Tag":"tum-lcw-home-urunleri","PageIndex":"2"}