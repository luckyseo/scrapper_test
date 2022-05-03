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


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = bs(result.text, "html.parser")
        results = soup.find_all("h2", {"class": "jobTitle"})
        for re in results:
            title = re.find("span", title=True).string
            jobs.append(title)
    return jobs
