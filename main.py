import requests
from bs4 import BeautifulSoup as bs
indeed_result=requests.get("https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=676599852a737304")

indeed_soup = bs(indeed_result.text, 'html.parser')

pagination = indeed_soup.find("div",{"class":"pagination"})
page1 = pagination.find_all("b")
pages = pagination.find_all("a")
spans=[]
for page in pages:
    spans.append(page.find("span"))