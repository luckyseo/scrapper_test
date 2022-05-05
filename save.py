import csv

def saveToFile(jobs):
    file = open("jobs.csv",mode="w",encoding="UTF-8")
    writer = csv.writer(file)
    writer.writerow(["title", "company","locatoin", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return