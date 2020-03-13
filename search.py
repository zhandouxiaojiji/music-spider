import os
import sys
import json
import urllib.request
from selenium import webdriver
from time import sleep

search = sys.argv[1]
task_path = sys.argv[2]
if not task_path:
    task_path = "tasks.json"

url = 'http://tool.liumingye.cn/music/?page=audioPage&type=migu&name='+search

dr = webdriver.Chrome()
dr.get(url)
dr.implicitly_wait(5)

# 设置关闭自动播放
dr.find_elements_by_css_selector(".am-btn.am-round")[-1].click()
dr.find_elements_by_css_selector(".am-icon-checked")[-1].click()
dr.find_elements_by_css_selector(".am-modal-btn")[-1].click()
sleep(1)

while True:
    more_btn = dr.find_element_by_css_selector(".aplayer-more")
    more_text = more_btn.get_attribute("innerHTML")
    print("more:", more_text)
    if more_text == "没有了":
        break
    if more_text == "下一页":
        more_btn.click()
    sleep(1)

arr = dr.find_elements_by_css_selector(
    ".aplayer-list-download.am-icon-download")

tasks = []
for download_btn in arr:
    dr.implicitly_wait(5)
    try:
        download_btn.click()
        elem = dr.find_element_by_id("name")
        name = elem.get_attribute('value')
        print(name)
        url_flac = dr.find_element_by_id("url_flac").get_attribute('value')
        url_320 = dr.find_element_by_id("url_320").get_attribute('value')
        url_128 = dr.find_element_by_id("url_128").get_attribute('value')
        url_m4a = dr.find_element_by_id("url_m4a").get_attribute('value')
        if url_flac != '':
            tasks.append({
                "name": name+".flac",
                "url": url_flac
            })
        elif url_320:
            tasks.append({
                "name": name+".mp3",
                "url": url_320
            })
        elif url_128:
            tasks.append({
                "name": name+".mp3",
                "url": url_128
            })
        elif url_m4a:
            tasks.append({
                "name": name+".mp3",
                "url": url_m4a
            })
        dr.find_element_by_css_selector(
            "body>#m-download>.am-modal-dialog>.am-modal-footer").click()
        sleep(0.2)
    except:
        print("无法下载")

f2 = open(task_path, 'w+', encoding='utf-8')
f2.write(json.dumps(tasks, ensure_ascii=False, indent = 4))
f2.close()
print(tasks)

dr.close()
