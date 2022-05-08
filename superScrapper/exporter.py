import csv
from readline import write_history_file


def save_to_file(jobs):
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["tite", "company", "locatoin", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
