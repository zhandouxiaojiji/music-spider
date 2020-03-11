"""使用模块线程方式实现网络资源的下载
# 实现文件下载, 期间显示文件信息&下载进度
# 控制台运行以显示进度
"""
import requests
import os.path as op
import os
from sys import stdout
 
 
def downloadfile(url, path):
  """下载文件并显示过程
  :param url: 资源地址
  :param path: 保存目录
  """
 
  with open(path, "wb") as fw:
    with requests.get(url, stream=True) as r:
      # 此时只有响应头被下载
      # print(r.headers)
      print("下载文件基本信息:")
      print('-' * 30)
      print("文件类型:", r.headers["Content-Type"])
      filesize = r.headers["Content-Length"]
      print("文件大小:", filesize, "bytes")
      print("下载地址:", url)
      print("保存路径:", path)
      print('-' * 30)
      print("开始下载")
 
      chunk_size = 128
      times = int(filesize) // chunk_size
      show = 1 / times
      show2 = 1 / times
      start = 1
      for chunk in r.iter_content(chunk_size):
        fw.write(chunk)
        if start <= times:
          stdout.write(f"下载进度: {show:.2%}\r")
          start += 1
          show += show2
        else:
          stdout.write("下载进度: 100%")
      print("\n结束下载")
 
 
if __name__ == "__main__":
  downloadfile("https://code.jquery.com/jquery-3.4.1.js", "a.js")