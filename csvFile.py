import csv
date =csv.reader(open('test.csv','r'))
for test in date:
    print (test)
    print(" test output ")
    print (test[0])
'''
注：需要先导入csv包，然后通过reader方法读取内容，最终会返回一个列表。想选择某一列数据，只需要制定列表下标即可

from 
python读取txt、csv和excel文件 
https://www.cnblogs.com/dvbbs2012/p/5462747.html
'''