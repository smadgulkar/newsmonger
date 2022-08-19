from flask import Flask, render_template
import feedparser
import datetime
from dateutil import parser

app = Flask(__name__)


base_feeds = [
    "https://www.cnbc.com/id/10001147/device/rss/rss.html",
    "https://www.cnbc.com/id/15839135/device/rss/rss.html",
    "https://www.investing.com/rss/news_25.rss",
    "https://www.investing.com/rss/stock_stock_picks.rss",
    "https://www.investing.com/rss/news_25.rss",
    "https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml",
    "http://feeds.marketwatch.com/marketwatch/topstories/",
    "http://feeds.marketwatch.com/marketwatch/realtimeheadlines/",
    "http://feeds.marketwatch.com/marketwatch/bulletins",
]


@app.route("/")
def get_feeds():
    packed = []
    for url in base_feeds:
        data = feedparser.parse(url)
        for i in data["entries"]:
            pubdate = i["published"]
            tru_date = parser.parse(pubdate)
            tru_date_strip = tru_date.date()
            date_of_today = datetime.date.today()
            if date_of_today == tru_date_strip:
                result = {}
                result["title"] = i["title"]
                result["link"] = i["link"]
                # result["pubtime"] = str(tru_date)
                packed.append(result)
    return render_template("index.html", collection=packed)


if __name__ == "__main__":
    app.run(debug=True)
