from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get('http://tool.liumingye.cn/music/?page=audioPage&type=migu&name=%E6%9E%97%E4%BF%8A%E6%9D%B0%20-%20%E6%9E%97%E4%BF%8A%E6%9D%B0')
dr.implicitly_wait(5)

# while True:
#   more_btn = dr.find_element_by_css_selector(".aplayer-more")
#   more_text = more_btn.get_attribute("innerHTML")
#   print("more:", more_text)
#   if more_text == "没有了":
#     break
#   if more_text == "下一页":
#     more_btn.click()
#   sleep(1)

arr = dr.find_elements_by_css_selector(".aplayer-list-download.am-icon-download")

task = {}
for download_btn in arr:
  sleep(0.2)
  download_btn.click()
  elem = dr.find_element_by_id("name")
  name = elem.get_attribute('value')
  print(name)
  elem_flac = dr.find_element_by_id("url_flac")
  elem_320 = dr.find_element_by_id("url_320")
  elem_128 = dr.find_element_by_id("url_128")
  elem_m4a = dr.find_element_by_id("url_m4a")
  if elem_flac:
    task[name+".flac"] = elem_flac.get_attribute('value')
  elif elem_320:
    task[name+".mp3"] = elem_320.get_attribute('value')
  elif elem_128:
    task[name+".mp3"] = elem_128.get_attribute('value')
  elif elem_m4a:
    task[name+".mp3"] = elem_m4a.get_attribute('value')
  dr.find_element_by_css_selector("body>#m-download>.am-modal-dialog>.am-modal-footer").click()

print(task)

# dr.find_element_by_css_selector(".aplayer-list-download.am-icon-download").click()
# elem = dr.find_element_by_id("name")
# print(elem.get_attribute('value'))

# elem = dr.find_element_by_id("url_flac")
# print(elem.get_attribute('value'))

dr.close()