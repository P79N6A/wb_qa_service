import time

def intTimeToString(timeStamp):
    timeArray = time.localtime(timeStamp)
    stringStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return stringStyleTime

def stringTimeToInt(stringStyleTime):
    timeArray = time.strptime(stringStyleTime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp