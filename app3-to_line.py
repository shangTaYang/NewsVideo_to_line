import lineTool
import requests
import datetime
import csv
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
import time


today = datetime.date.today()
ettday = "https://www.ettoday.net/news"


def get_ettoday_social_news_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select(".part_list_2 h3")
    news = []
    for i in rows:
        if i.select('a i'):
            title = i.select("a")[0].text
            news_url = i.find("a").get("href")
            data = {}
            data["title"] = title
            data["news_url"] = f'{ettday}{news_url}'
            news.append(data)
        else:
            continue
    return news


# 創建一個 Scheduler 物件實例
sched = BlockingScheduler({'apscheduler.timezone': 'Asia/Taipei'})
# # decorator 設定 Scheduler 的類型和參數，例如 interval 間隔多久執行
# @sched.scheduled_job('interval',seconds=5)
# def timed_job():
#     print('每5S執行一次程式工作區塊')
#     china_news = get_ettoday_social_news_url(f'{ettday}/news-list-{today}-3.htm')
#     #china_news是字串包字典 [{title:123,url:123},....]
#     for i in china_news: #取出每個字典 i = {title:123,url:123}
#         title = i["title"]
#         url = i["news_url"]
#         sbb = title+url
#         lineTool.lineNotify(token,sbb)
#         # for every_value in i: #取出的title與url
#         #     # print(i[every_value],end="") #取出i的title與url的value

china_news = f'{ettday}/news-list-{today}-3.htm'
social_news = f'{ettday}/news-list-{today}-6.htm'
Local_news = f'{ettday}/news-list-{today}-7.htm'
International_news = f'{ettday}/news-list-{today}-2.htm'


def china_news_job():
    china_news = get_ettoday_social_news_url(
        f'{ettday}/news-list-{today}-3.htm')
    # china_news是字串包字典 [{title:123,url:123},....]
    for i in china_news:  # 取出每個字典 i = {title:123,url:123}
        title = i["title"]
        url = i["news_url"]
        sbb = title+url
        lineTool.lineNotify(token, sbb)


def social_news_job():
    social_news = get_ettoday_social_news_url(
        f'{ettday}/news-list-{today}-6.htm')
    # china_news是字串包字典 [{title:123,url:123},....]
    for i in social_news:  # 取出每個字典 i = {title:123,url:123}
        title = i["title"]
        url = i["news_url"]
        sbb = title+url
        lineTool.lineNotify(token, sbb)


def Local_news_job():
    Local_news = get_ettoday_social_news_url(
        f'{ettday}/news-list-{today}-7.htm')
    # china_news是字串包字典 [{title:123,url:123},....]
    for i in Local_news:  # 取出每個字典 i = {title:123,url:123}
        title = i["title"]
        url = i["news_url"]
        sbb = title+url
        lineTool.lineNotify(token, sbb)


def International_news():
    International_news = get_ettoday_social_news_url(
        f'{ettday}/news-list-{today}-2.htm')
    # china_news是字串包字典 [{title:123,url:123},....]
    for i in International_news:  # 取出每個字典 i = {title:123,url:123}
        title = i["title"]
        url = i["news_url"]
        sbb = title+url
        lineTool.lineNotify(token, sbb)


def end():
    print("---------------")


china_news_job()
social_news_job()
Local_news_job()
International_news()

sched.add_job(china_news_job, 'interval', minutes=59)
sched.add_job(social_news_job, 'interval', minutes=59)
sched.add_job(Local_news_job, 'interval', minutes=59)
sched.add_job(International_news, 'interval', minutes=59)
sched.add_job(end, 'interval', minutes=59)

sched.start()
