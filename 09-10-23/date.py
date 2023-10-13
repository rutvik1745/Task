import time
print(time.time())
print(time.localtime(time.time()))


print(time.asctime(time.localtime(time.time())))

for i in range(0,5):
    print(i)
    time.sleep(1)

from datetime import datetime as dt

# print(datetime.datetime.now())
# print(datetime.datetime(2023,4,4,1,26,40))

if dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
    print("Working Hours...")
else:
    print("fun hours")


import calendar
cal = calendar.prcal(2023)
print(cal)