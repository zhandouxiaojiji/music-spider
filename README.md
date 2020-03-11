# 无损音乐爬虫脚本
最近发现一个大神做的网站([liumingye.cn](http://tool.liumingye.cn/music/))，收集着海量的无损音乐，试着搜了一下，发现里面的歌还是挺新挺全的，但是无法批量下载，于是随手写了个批量下载的脚本，第一次写爬虫，见笑了。

# 环境
+ python3
+ chromedriver

# 运行
+ python search.py 某某歌手
+ python download.py mydir

注:第一步会收集要下载的曲目到tasks.json文件，第二步是根据tasks.json下载到指定目录，如果有下载超时的，重新执行download即可

# Warning
仅供学习交流，适度使用，严禁用于商业用途!
