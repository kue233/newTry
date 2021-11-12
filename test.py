import datetime
from dateutil.relativedelta import relativedelta

end = datetime.datetime(2020,1,1)

print ('START time is: ' + str((end+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")))
print ((end+datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
print ((end-datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))  
print((end - relativedelta(years=1)).strftime('%Y-%m-%d'))
print((end - relativedelta(months=1)).strftime('%Y-%m-%d'))
a = (end - relativedelta(months=1)).strftime('%Y-%m-%d')
print(type(a))
print(type(end))

print(end+ datetime.timedelta(days=-1))
b = end+ datetime.timedelta(days=-1)
print(type(b))

c =end - relativedelta(months=1)
print(c)
print(type(c))


print('--------------------------------------')

text = '2012-09-20'
y = datetime.datetime.strptime(text, '%Y-%m-%d')
print(y)
print(type(y))