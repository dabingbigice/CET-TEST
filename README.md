1.pip install scrapy

2.cd 进入当前工程 D:\cet6-scrapy\cet\cet

3.配置 [settings.py]中的文件夹存储路径 FILES_STORE 为自己指定的，也可以不修改使用默认的

4.运行工程 scrapy crawl cet-spider

5.下载4级和6级的路径不同，注意修改cet_spider.py中path的路径，改为/Learn/CET/CET4或者/Learn/CET/CET6

6.sleep函数是必须的建议不要修改，如果过快会被封ip。