import requests
import datetime
import csv
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

today = datetime.date.today()
ettday = "https://www.ettoday.net/news" 

def get_ettoday_social_news_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    resp = requests.get(url,headers=headers)
    soup = BeautifulSoup(resp.text,"html.parser")


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

    
    headers = ["title", "news_url"]
    with open(f'{news_name}.csv',"w",encoding="utf8") as f:
        dict_writer = csv.DictWriter(f,headers)
        dict_writer.writeheader()
        dict_writer.writerows(news)

print("a : social_news_url\nb : International_news_url\nc : Local_news_url \nd : China_news_url\nall:輸出全部新聞\n0:結束")
while True:
    want_news = input("請輸入新聞代號:")
    if want_news == "a":
        news_name = "social_news_url"
        url = f'{ettday}/news-list-{today}-6.htm'
    elif want_news == "b":
        news_name = "International_news_url"
        url = f'{ettday}/news-list-{today}-2.htm'
    elif want_news == "c":
        news_name = "Local_news_url"
        url = f'{ettday}/news-list-{today}-7.htm'
    elif want_news == "d":
        news_name = "China_news_url"
        url = f'{ettday}/news-list-{today}-3.htm'
    elif want_news == "all":
        news_name = "social_news_url"
        url = f'{ettday}/news-list-{today}-6.htm'
        get_ettoday_social_news_url(url)
        news_name = "International_news_url"
        url = f'{ettday}/news-list-{today}-2.htm'
        get_ettoday_social_news_url(url)
        news_name = "Local_news_url"
        url = f'{ettday}/news-list-{today}-7.htm'
        get_ettoday_social_news_url(url)
        news_name = "China_news_url"
        url = f'{ettday}/news-list-{today}-3.htm'
        # get_ettoday_social_news_url(url)
    elif want_news == "0":
        break
    else :
        print("請重新輸入")
        continue
    get_ettoday_social_news_url(url)
    print("已輸出csv檔")
        
