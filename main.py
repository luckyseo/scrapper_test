from indeed import getJobs as get_indeed_jobs
from save import saveToFile
indeed_jobs=get_indeed_jobs()

jobs=indeed_jobs

#csv = comma seperated val

saveToFile(jobs)