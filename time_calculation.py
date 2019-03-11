'''
python中通过datetime模块可以很方便的计算两个时间的差,datetime的时间差单位可以是天、小时、秒,甚至是微秒,下面我们就来详细看下datetime的强大功能:


from datetime import datetime 
a=datetime.now() 
b=datetime.now() 
>>>a
>>>datetime.datetime(2015, 4, 7, 4, 30, 3, 628556) 
>>>b
>>>datetime.datetime(2015, 4, 7, 4, 34, 41, 907292) 

>>>str(a) #字符串的转换，用户储存到文本或者数据库
'2015-04-07 04:30:03.628556' 
>>>datetime.strptime(str(a),"%Y-%m-%d %H:%M:%S.%f")
datetime.datetime(2015, 4, 7, 4, 30, 3, 628556) 

>>> (b-a)
Out: datetime.timedelta(0, 278, 278736) 

>>>(b-a).seconds #时间差的计算，单位为秒
278

Q:如何方便的计算两个时间的差，如两个时间相差几天，几小时等
A:使用datetime模块可以很方便的解决这个问题，举例如下：
>>> import datetime>>> d1 = datetime.datetime(2005, 2, 16)>>> d2 = datetime.datetime(2004, 12, 31)>>> (d1 - d2).days47
上例演示了计算两个日期相差天数的计算。

>>>import datetime
>>>starttime = datetime.datetime.now()
#long running
>>>endtime = datetime.datetime.now()
>>>print (endtime - starttime).seconds
上例演示了计算运行时间的例子，以秒进行显示。

>>> d1 = datetime.datetime.now()
>>> d3 = d1 + datetime.timedelta(hours=10)
>>> d3.ctime()
上例演示了计算当前时间向后10小时的时间。

其本上常用的类有：datetime和timedelta两个。它们之间可以相互加减。每个类都有一些方法和属性可以查看具体的值，
如datetime可以查看：天数(day)，小时数(hour)，星期几(weekday())等;timedelta可以查看：天数(days)，秒数(seconds)等。
'''