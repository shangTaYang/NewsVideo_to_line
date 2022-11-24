import requests
import datetime
import csv
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

today = datetime.date.today()
ettday = "https://www.ettoday.net/news" 

def get_ettoday_social_news_url():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    social_news_url = f'{ettday}/news-list-{today}-6.htm'
    resp = requests.get(social_news_url,headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    rows = soup.select(".part_list_2 h3")
    social_news = []
    for i in rows:
        if i.select('a i'):
            social_news_title = i.select("a")[0].text
            get_social_news_url = i.find("a").get("href")
            data = {}
            data["title"] = social_news_title
            data["news_url"] = f'{ettday}{get_social_news_url}'
            social_news.append(data)
        else:
            continue
    return social_news

def International_news_url():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    International_news_url = f'{ettday}/news-list-{today}-2.htm'
    resp = requests.get(International_news_url,headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")
    rows = soup.select(".part_list_2 h3")
    International_news = []
    for i in rows:
        if i.select('a i'):
            International_news_title = i.select("a")[0].text
            get_International_news_url = i.find("a").get("href")
            data = {}
            data["title"] = International_news_title
            data["news_url"] = f'{ettday}{get_International_news_url}'
            International_news.append(data)
        else:
            continue
    return International_news


headers = ["title", "news_url"]
with open('social_news.csv',"w",encoding="utf8") as f1:
    dict_writer = csv.DictWriter(f1,headers)
    dict_writer.writeheader()
    social_news = get_ettoday_social_news_url()
    dict_writer.writerows(social_news)
with open('International_news.csv',"w",encoding="utf8") as f2:
    dict_writer = csv.DictWriter(f2,headers)
    dict_writer.writeheader()
    International_news = International_news_url()
    dict_writer.writerows(International_news)

# 可否合併為單一方法? 回傳影片類型以及網址
#     Local_news_url = f'{ettday}/news-list-{today}-7.htm'
#     China_news_url = f'{ettday}/news-list-{today}-3.htm'














# # def save_data_to_csv(row_list):
# #     # CSV 檔案第一列標題記得要和 dict 的 key 相同，不然會出現錯誤
# #     headers = ['title', 'news_url']
# #     with open('project.csv',"w") as f:
# #         dict_writer = csv.DictWriter(f,headers)
# #         dict_writer.writeheader()
# #         dict_writer.writerows(row_list)

# # 創建一個 Scheduler 物件實例
# sched = BlockingScheduler({'apscheduler.timezone': 'Asia/Taipei'})
# # decorator 設定 Scheduler 的類型和參數，例如 interval 間隔多久執行
# @sched.scheduled_job('interval',seconds=20)
# def timed_job():
#     print('每20S執行一次程式工作區塊')
#     # url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314"
#     # data = get_api_data(url)
#     # row_list = get_parse_data(data)
#     # save_data_to_csv(row_list)
#     row_list = get_ettoday_soup()
#     print(row_list)
#     # save_data_to_csv(row_list)

# sched.start()

