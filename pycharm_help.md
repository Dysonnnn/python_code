
**pycharm**  
软件安装：
    去官网下载软件包，解压
软件启动：
```bash
./pycharm****/bin/pycharm.sh &   
# 要等一会儿才出现界面
```

设置字体  搜索 font
设置 python 包管理：
settings-project:xxxx--project intetpretet


报错：
    ImportError: No module named 'setuptools'
解决方法：
```
    sudo apt install python3-setuptools
    sudo apt install python3-pip
    sudo python3 -m pip install --upgrade pip
```
然后,还是不能装插件，
```

AttributeError: module 'setuptools.dist' has no attribute 'check_specifier'
```



手动安装吧
```
sudo python3 -m pip install serial
```
AttributeError: module 'setuptools.dist' has no attribute 'check_specifier'

还是不行


---

pip 更新源：
```
原版：

https://pypi.python.org/simple

国内目前有这几个：

http://pypi.douban.com/simple/ 豆瓣
http://mirrors.aliyun.com/pypi/simple/ 阿里
http://pypi.hustunique.com/simple/ 华中理工大学
http://pypi.sdutlinux.org/simple/ 山东理工大学
http://pypi.mirrors.ustc.edu.cn/simple/ 中国科学技术大学
https://pypi.tuna.tsinghua.edu.cn/simple 清华
--------------------- 
作者：夏微凉秋微暖 
来源：CSDN 
原文：https://blog.csdn.net/pengbin790000/article/details/72516808 
版权声明：本文为博主原创文章，转载请附上博文链接！
```