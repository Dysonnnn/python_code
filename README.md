# python_code
normal use python3 without specitial note

---
20190314
ubuntu16.04 自带的python3 是python3.5的，各种问题。   
   
重装python3：   
    sudo apt remove python3   # 这卸载不干净。
安装教程参考   
[菜鸟教程python3](http://www.runoob.com/python3/python3-install.html)

Unix & Linux 平台安装 Python3:

以下为在 Unix & Linux 平台上安装 Python 的简单步骤：

    打开WEB浏览器访问 https://www.python.org/downloads/source/
    选择适用于 Unix/Linux 的源码压缩包。
    下载及解压压缩包 Python-3.x.x.tgz，3.x.x 为你下载的对应版本号。
    如果你需要自定义一些选项修改 Modules/Setup

以 Python3.6.1 版本为例：
```
# tar -zxvf Python-3.6.1.tgz
# cd Python-3.6.1
# ./configure    # 指定安装目录 $ ./configure --prefix=/usr/local/python3 --with-ssl  
# make && make install
```
检查 Python3 是否正常可用：
```
# python3 -V
Python 3.6.1
```

在 Unix/Linux 设置环境变量

   在 ~/.bashrc 文件内新增一行

    export PATH="$PATH:/usr/local/python3/bin" 

注意: /usr/local/python3/bin 是 Python 执行程序的所在目录。


```
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-18.1 setuptools-40.6.2

```

此时，/usr/bin 下也存在一个python3，但是指向的是python3.5
修改 /usr/bin 下的python3的软连接，让链接连接到python36 ：
```
cd /usr/bin
sudo mv python3 python35
```
然后系统就会识别到 /usr/local/python3/bin 路径下的python3.6


默认使用python3 而不是 python2，修改 /usr/bin 下的 python 软链接，使其指向python3.6
```
cd /usr/bin
sudo mv python python_backup # 备份一下、
sudo ln -s  /usr/local/python3/bin/python3 /usr/bin/python   # 为python3 创建软连接
ls -l | grep # 效果如下：
lrwxrwxrwx 1 root root   30 Mar 13 19:06 python -> /usr/local/python3/bin/python3
```

```
$ whereis pip3  
pip3: 
/usr/local/bin/pip3.5 
/usr/local/bin/pip3 
/usr/local/python3/bin/pip3.6 
/usr/local/python3/bin/pip3 
/usr/share/man/man1/pip3.1.gz

# 修改 /usr/bin 下的pip3
$ cd /usr/bin
$ sudo mv pip3 pip3_backup 
# 
# 修改 /usr/local/bin/ 下的pip3
$ cd /usr/local/bin/
$ ls
easy_install  easy_install-3.5  pip  pip3  pip3.5
$ sudo mv pip pip_backup
$ sudo mv pip3 pip3_backup   

# 使其只有一个pip3 ,在/usr/local/python3/bin pip3 


```



---

---

[菜鸟教程_Python命令行参数](http://www.runoob.com/python/python-command-line-arguments.html)
## Python 命令行参数

**Python 基础语法 Python 基础语法**

Python 提供了 getopt 模块来获取命令行参数。
```
$ python test.py arg1 arg2 arg3
```
Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：

- sys.argv 是命令行参数列表。

- len(sys.argv) 是命令行参数个数。

**注**：sys.argv[0] 表示脚本名。

**实例**

test.py 文件代码如下：
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)
```
执行以上代码，输出结果为：
```
$ python test.py arg1 arg2 arg3
参数个数为: 4 个参数。
参数列表: ['test.py', 'arg1', 'arg2', 'arg3']
```
## getopt模块

getopt模块是专门处理命令行参数的模块，用于获取命令行选项和参数，也就是sys.argv。命令行选项使得程序的参数更加灵活。支持短选项模式（-）和长选项模式（--）。

该模块提供了两个方法及一个异常处理来解析命令行参数。

**getopt.getopt 方法**

getopt.getopt 方法用于解析命令行参数列表，语法格式如下：
```
getopt.getopt(args, options[, long_options])
```
方法参数说明：

- args: 要解析的命令行参数列表。

- options : 以字符串的格式定义，options 后的冒号 : 表示如果设置该选项，必须有附加的参数，否则就不附加参数。

- long_options : 以列表的格式定义，long_options 后的等号 = 表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。

- 该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有 - 或 -- 的参数。

另外一个方法是 getopt.gnu_getopt，这里不多做介绍。

**Exception getopt.GetoptError**

在没有找到参数列表，或选项的需要的参数为空时会触发该异常。

异常的参数是一个字符串，表示错误的原因。属性 msg 和 opt 为相关选项的错误信息。

**实例**

假定我们创建这样一个脚本，可以通过命令行向脚本文件传递两个文件名，同时我们通过另外一个选项查看脚本的使用。脚本使用方法如下：
```
usage: test.py -i <inputfile> -o <outputfile>
```

test.py 文件代码如下所示：
```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print '输入的文件为：', inputfile
   print '输出的文件为：', outputfile

if __name__ == "__main__":
   main(sys.argv[1:])
```

执行以上代码，输出结果为：
```
$ python test.py -h
usage: test.py -i <inputfile> -o <outputfile>

$ python test.py -i inputfile -o outputfile
输入的文件为： inputfile
输出的文件为： outputfile
```
---





---
python3 使用串口 需要安装 pip36 install serial pyserial
---




---

python36 无法使用 方向键

sudo apt-get install libreadline-dev

pip install readline 

都无效。
---
