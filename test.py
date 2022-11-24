# 當爬取的網頁為 JavaScript 網頁前端（非伺服器端）生成，需引入 selenium 套件來模擬瀏覽器載入網頁並跑完 JavaScript 程式才能取得資料
# 引入套件
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time

url = "https://www.ettoday.net/news/20220720/2298576.htm?redirect=1"
r = requests.get(url)
soup11 = BeautifulSoup(r.text,'html.parser')
# a = soup11.find("div","class_=BH-lbox_MSG-list8")
# print(a.find("div","class_=MSG-list8C"))

# legal = input("想找誰(英文):")

# # ./chromedriver.exe 為 chrome 瀏覽器驅動引擎檔案位置（注意 MacOS/Linux 沒有 .exe 副檔名），也可以使用絕對路徑，例如： C:\downloads\chromedriver.exe
# driver = webdriver.Chrome('./chromedriver.exe')
# # 發出網路請求
# driver.get(r)
# soup = BeautifulSoup(page_content,'html.parser')
# 從 iframe 取出 src 影片網址
print(soup11.select(".story iframe")[0].attrs['src'])
#get("src")也可以

# 移動到 iframe 裡面
# driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".story iframe"))

# page_content = driver.page_source
# # 將 HTML 內容轉換成 BeautifulSoup 物件，html.parser 為使用的解析器
# soup = BeautifulSoup(page_content,'html.parser')

# # 透過 select 使用 CSS 選擇器 選取欲爬取新聞內的影片連結網址
# print(soup.select(".ytp-title-text"))
# # # 使用直接複製的select
# print(soup.select("#movie_player > div.ytp-chrome-top.ytp-show-cards-title > div.ytp-title > div > a"))

# # 從影片 iframe 移動回來主要網頁內容
# driver.switch_to.default_content()
