import json
from bottle import route, run, get, HTTPResponse, response, request, Response
import bottle as b
import feedparser
from datetime import datetime, timedelta


@route('/')
def index():
    return b.template("ex1.html")


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def javascript(filename):
    return b.static_file(filename, root='css')


@get('/api/getFeedsJP')
def users():
    now_time = str(datetime.now())
    if request.get_cookie("last_visited_JP"):
        jp_last_refresh = "your last visited was " + request.get_cookie("last_visited_JP")
        response.set_cookie("last_visited_JP", now_time)
    else:
        response.set_cookie("last_visited_JP", now_time)
        jp_last_refresh = "welcome to jerusalem post, enjoy"

    feed = feedparser.parse("https://www.jpost.com/Rss/RssFeedsHeadlines.aspx")
    headlines_JP = []
    for number in range(len(feed["entries"])):
        headLines = {"titles": feed["entries"][number]["title"], "link": feed["entries"][number]["link"]}
        headlines_JP.append(headLines)

    return {json.dumps([headlines_JP, jp_last_refresh])}


@get('/api/getFeedsDM')
def users2():
    now_time = str(datetime.now())
    if request.get_cookie("last_visited_DM"):
        dm_last_refresh = "your last visited was " + request.get_cookie("last_visited_DM")
        response.set_cookie("last_visited_DM", now_time)
    else:
        response.set_cookie("last_visited_DM", now_time)
        dm_last_refresh = "welcome to the daily mail, enjoy"

    feed2 = feedparser.parse("http://www.dailymail.co.uk/articles.rss")
    headlines_DM = []
    for article in range(len(feed2["entries"])):
        headLines2 = {"titles": feed2["entries"][article]["title"], "link": feed2["entries"][article]["link"]}
        headlines_DM.append(headLines2)

    return {json.dumps([headlines_DM, dm_last_refresh])}


def main():
    run(host="localhost", port=7001)


if __name__ == "__main__":
    main()