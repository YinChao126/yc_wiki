# crawler静态爬虫示例

作者：尹超

日期：2019-7-1

描述：给出了一个静态爬虫的示例

## 源码

```python
import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def GetPoetry(name):
    '''
    从古诗词网上爬去匹配的诗词，并返回第一篇内容
    '''
    url = 'https://so.gushiwen.org/search.aspx?value='
    url += name
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    			AppleWebKit/537.36 (KHTML, like Gecko) \
    			Chrome/61.0.3163.79 Safari/537.36'}
    html = ''
    try:
        response = requests.get(url,headers = headers)                  
        response.encoding = 'utf-8'  #解决中文乱码
        if response.status_code == 200:  #判断是否爬取网页成功
            html = response.text
        else:
            return
    except RequestException:
        return 
    soup = BeautifulSoup(html,'html5lib')
    lls = soup.select('table#BalanceSheetNewTable0 tbody tr td')
    lls = soup.select('textarea')   
    try:
        pattern = '(?<=>).*(?=https)'
        obj = re.compile(pattern)
        match = obj.findall(str(lls[0]))  
        return match[0]
    except:
        return 0

if __name__ == '__main__':
    print(GetPoetry('千树万树梨花开'))
```

