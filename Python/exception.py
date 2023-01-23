"""
import os

path=os.getcwd()+'/Accounts'
files=os.listdir(path)

for file in files:
    try:
        f=open(path+'/'+file,'r')
        data=f.read()
        if 'ELEVATED ACCESS DATA' in data:
            raise Exception
    except Exception:
        print("acccess denied")
    else:
        print(data)
"""

import datetime as dt
import time

start=time.time()

m=1
for i in range(1,10):
    m*=i

print(m)

end=time.time()

print('It took:'+str(end-start))


dt.date.today()


print(dt.date(1998,9,21))
print(dt.date.today())
tday=(dt.datetime.today())
print(tday)
print(tday.year)
print(tday.day)
print(tday.ctime())
print(tday.strftime('%y-%b-%d:%p'))
print(tday.strftime('%y-%b-%A:%I:%M:%p'))
print(tday.weekday())#monday=0,sun=6
print(tday.isoweekday())#monday=1,sun=7
#today-naive
#now-aware
print('UTC time:',dt.utcnow())
print('Adding time delta to todays date',dt.today()+days)




