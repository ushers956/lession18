import random
import time

def getRandomDate(startdate, enddate):
    print("printing random date between", startdate, "and" ,enddate)
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'

    starttime = time.mktime(time.strptime(startdate, dateformat))
    endtime = time.mktime(time.strptime(startdate, dateformat))

    randomtime=starttime + randomgenerator * (endtime - starttime)
    randomdate = time.strftime(dateformat, time.localtime(randomtime))
    return randomdate
print("random date = ", getRandomDate("1/1/2016","1/1/2025"))