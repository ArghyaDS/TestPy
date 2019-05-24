import numpy as np
#show all days in March, 2017
print("March, 2017")
print(np.arange('2017-03','2017-04',dtype='datetime64[D]'))
#show dates of yesterday, today, and tomorrow
yesterday=np.datetime64('today','D')-np.timedelta64(1,'D')
print("Yesterday: ",yesterday)
today=np.datetime64('today','D')
print("Today: ",today)
tomorrow=np.datetime64('today','D')+np.timedelta64(1,'D')
print("Tomorrow: ",tomorrow)
#show number of days in specified month
print("Number of days, February, 2016: ")
print(np.datetime64('2016-03-01')-np.datetime64('2016-02-01'))
print("Number of days, February, 2017: ")
print(np.datetime64('2017-03-01')-np.datetime64('2017-02-01'))
print("Number of days, February, 2018: ")
print(np.datetime64('2018-03-01')-np.datetime64('2018-02-01'))
#print 24 datetime objects in numpy array
import datetime
start=datetime.datetime(2000,1,1)
date_array=np.array([start+datetime.timedelta(hours=i) for i in range(24)])
print(date_array)
#find a particular day from certain month
print("first monday in may 2017:")
print(np.busday_offset('2017-05',0,roll='forward',weekmask='Mon'))
#find number of weekdays in a specified month
print("number of weekdays in march 2017: ")
print(np.busday_count('2017-03','2017-04'))
#convert datetime64 to timestamp
from datetime import datetime
dt = datetime.now()
print("Current date:")
print(dt)
dt64 = np.datetime64(dt)
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
print("Timestamp:")
print(ts)
print("UTC from Timestamp:")
print(datetime.utcfromtimestamp(ts))
