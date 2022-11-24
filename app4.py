import requests
import datetime
import csv
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

today = datetime.date.today()
ettday = "https://www.ettoday.net/news" 

def get_ettoday_social_news_url():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62'
    }
    social_news_url = f'{ettday}/news-list-{today}-6.htm' #https://www.ettoday.net/news/news-list-2022-07-21-2.htm
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
            a = requests.get(data["news_url"],headers=headers)
            soup_a = BeautifulSoup(a.text,"html.parser")
            vedio_url = soup_a.select(".story iframe")[0].attrs['src']
            data["vedio_url"] = vedio_url
            social_news.append(data)   
            print(social_news)        
        else:
            continue
    return social_news


headers = ["title", "news_url","vedio_url"]
with open('11223.csv',"w",encoding="utf8") as f1:
    dict_writer = csv.DictWriter(f1,headers)
    dict_writer.writeheader()
    social_news = get_ettoday_social_news_url()
    dict_writer.writerows(social_news)