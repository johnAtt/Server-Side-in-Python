import json
from bottle import route, run, get, HTTPResponse, response, request
import bottle as b
import feedparser
from datetime import datetime, timedelta

feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
feed2 = feedparser.parse("http://www.dailymail.co.uk/articles.rss")
headlines_JP = []
headlines_DM = []

for number in range(len(feed["entries"])):
    headLines = {"titles": feed["entries"][number]["title"], "link": feed["entries"][number]["link"]}
    headlines_JP.append(headLines)


for article in range(len(feed2["entries"])):
    headLines2 = {"titles": feed2["entries"][article]["title"], "link": feed2["entries"][article]["link"]}
    headlines_DM.append(headLines2)


@route('/')
def index():
    request.get_cookie("last_visited")
    response.set_cookie(name="last_visited", value=str(datetime.now()), expires=datetime.now() + timedelta(days=30))
    return b.template("ex1.html")


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def javascript(filename):
    return b.static_file(filename, root='css')


@get('/api/getFeedsJP')
def users():
    return HTTPResponse({json.dumps(headlines_JP)}, 200)


@get('/api/getFeedsDM')
def users():
    return HTTPResponse({json.dumps(headlines_DM)}, 200)


def main():
    run(host="localhost", port=7000)


if __name__ == "__main__":
    main()