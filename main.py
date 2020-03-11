import os
import urllib.request
from selenium import webdriver
from time import sleep
from download import downloadfile

url = 'http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=林俊杰'
path = './data'

if not os.path.exists(path):
  os.mkdir(path)

dr = webdriver.Chrome()
dr.get(url)
dr.implicitly_wait(5)

# 设置关闭自动播放
dr.find_elements_by_css_selector(".am-btn.am-round")[1].click()
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

arr = dr.find_elements_by_css_selector(".aplayer-list-download.am-icon-download")

tasks = []
for download_btn in arr:
  dr.implicitly_wait(5)
  try:
    download_btn.click()
    elem = dr.find_element_by_id("name")
    name = elem.get_attribute('value')
    print(name)
    elem_flac = dr.find_element_by_id("url_flac")
    elem_320 = dr.find_element_by_id("url_320")
    elem_128 = dr.find_element_by_id("url_128")
    elem_m4a = dr.find_element_by_id("url_m4a")
    if elem_flac:
      tasks.append({
        "name":name+".flac", 
        "url":elem_flac.get_attribute('value')
      })
    elif elem_320:
      tasks.append({
        "name":name+".mp3", 
        "url":elem_320.get_attribute('value')
      })
    elif elem_128:
      tasks.append({
        "name":name+".mp3", 
        "url":elem_128.get_attribute('value')
      })
    elif elem_m4a:
      tasks.append({
        "name":name+".mp3", 
        "url":elem_m4a.get_attribute('value')
      })
    dr.find_element_by_css_selector("body>#m-download>.am-modal-dialog>.am-modal-footer").click()
    sleep(0.2)
  except:
    print("无法下载")

print(tasks)

for task in tasks:
  print("download:"+task["name"]);
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

dr.close()