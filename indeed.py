import requests
from bs4 import BeautifulSoup as bs

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"


def extract_indeed_pages():
    result = requests.get(URL)
    soup = bs(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.find("span").string))  # link.string is fine!

    max_page = pages[-1]
    return max_page

def extract_job(soup):
    title=  soup.find("h2",{"class":"jobTitle"}).find("span",title=True).string
    company= soup.find("span",{"class":"companyName"})
    if company.find("a") == None:
        companyN=company.string
    else:
        companyN=company.find("a").string
    location=soup.find("div",{"class":"companyLocation"})
    if location.string ==None:
        location='Remote'
    else:
        location=location.string
    jobId=soup.select('a')[0]['data-jk']
    return {'title':title, 'company':companyN,'location':location,'link':f"https://www.indeed.com/viewjob?jk={jobId}&from=web&vjs=3"}

def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("a",{"class":"fs-unmask"})
        for re in results:
            job=extract_job(re)
            jobs.append(job)
    return jobs

