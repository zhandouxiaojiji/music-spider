import requests
import sys
import json
import os.path as op
import os
from sys import stdout


def downloadfile(url, path):
    """下载文件并显示过程
    :param url: 资源地址
    :param path: 保存目录
    """
    loading_path = path + ".download"
    if os.path.exists(loading_path):
        os.remove(loading_path)
    with open(loading_path, "wb") as fw:
        try:
            with requests.get(url, stream=True, timeout=5) as r:
                # 此时只有响应头被下载
                # print(r.headers)
                print('-' * 30)
                print("下载文件基本信息:")
                print("文件类型:", r.headers["Content-Type"])
                filesize = r.headers["Content-Length"]
                print("文件大小:", filesize, "bytes")
                print("下载地址:", url)
                print("保存路径:", path)
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
                fw.close()
                os.rename(loading_path, path)
                print("\n结束下载")
                print('-' * 30)
        except requests.exceptions.RequestException as e:
            print("下载失败:"+path)
            fw.close()
            if os.path.exists(loading_path):
                os.remove(loading_path)

path = sys.argv[1] or "data"
if not os.path.exists(path):
    os.mkdir(path)

f = open('tasks.json', 'r', encoding='utf-8')
tasks = json.loads(f.read())
print(type(tasks))
print(tasks)
f.close()
for task in tasks:
    print("download:"+task["name"])
    download_url = task["url"]
    download_path = path+'/'+task["name"]
    if download_url:
        if os.path.exists(download_path):
            print("skip.")
        else:
            downloadfile(download_url, download_path)
            # urllib.request.urlretrieve(download_url, download_path)
    else:
        print("url null")
