# _*_ coding: utf-8 _*_
# coding: utf-8
# @Author : waylanpunch
# @Time : 2021/7/18 22:56
# @File : SpiderCrawler.py
# @Software : PyCharm
import json

import bs4  # 网页解析
import re  # 正则表达式，文字匹配
import urllib.request, urllib.parse, urllib.error  # url请求，获取网页数据
import xlwt  # 进行Excel操作
import sqlite3  # 进行sqlite数据库操作
from bs4 import BeautifulSoup  # html 文档解析
from SQLite3Utils import checkIfSQLitePrepared, removeAllDataFromSQLite, storeDataToSQLite, readDataFromSQLite


def getDataByKeywordAndPageNo(keyword, pageNo):
    try:
        # url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html" #上海
        # url = "https://search.51job.com/list/180200,000000,0000,00,9,99,python,2,1.html" #武汉
        url = "https://search.51job.com/list/080200,000000,0000,00,9,99," + keyword + ",2," + str(pageNo) + ".html"

        response = urllib.request.urlopen(url, timeout=10)
        print(response.status)
        if 200 == response.status:
            # print("resolve response")
            htmlContent = response.read().decode("gbk")
            # print(result)
        else:
            print("network error")
    except urllib.error.URLError as e:
        print(e.reason)
    # else:
    #     print("network failure")
    finally:
        print("request end")
    return htmlContent


def getDataByKeywordAndPageNo2(keyword, pageNo):
    try:
        # url = "https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html" #上海
        # url = "https://search.51job.com/list/180200,000000,0000,00,9,99,python,2,1.html" #武汉
        url = "https://search.51job.com/list/080200,000000,0000,00,9,99," + keyword + ",2," + str(pageNo) + ".html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59",
            # "Accept": "text/html, application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "Accept-Encoding": "gzip,deflate,br",
            # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive"
        }
        request = urllib.request.Request(url=url, headers=headers, method="POST")
        response = urllib.request.urlopen(request)
        print(response.status)
        if 200 == response.status:
            # print("resolve response")
            htmlContent = response.read().decode("gbk")
            # print(result)
        else:
            print("network error")
    except urllib.error.URLError as e:
        print(e.reason)
    # else:
    #     print("network failure")
    finally:
        print("request end")
    return htmlContent


def resolveHtmlContent(htmlContent):
    bs = BeautifulSoup(htmlContent, "html.parser")
    # jobList = bs.select(".j_joblist")
    # if jobList is None or 0 == len(jobList):
    #     return None
    # print(jobList)
    # searchResult = json.loads(bs.find('script', {'type': 'text/javascript'}).get_text())#.get("window.__SEARCH_RESULT__")
    dataScript = bs.find_all('script', {'type': 'text/javascript'})[2]
    # dataScriptStr = str(dataScript)
    if dataScript is None or 0 == len(dataScript):
        return None
    reg = re.compile(r'<script type="text/javascript">(.*?)window.__SEARCH_RESULT__ = (.*?)</script>', re.S)
    # dataScriptStr = dataScriptStr.replace(r'<script type="text/javascript">', "")
    # dataScriptStr = dataScriptStr.replace('</script>', "")
    jsonStr = re.findall(reg, str(dataScript))[0]
    # print(jsonStr[1])
    if jsonStr is None or 0 == len(jsonStr):
        return None
    searchResult = json.loads(jsonStr[1]).get("engine_search_result")
    print(type(searchResult))
    return searchResult


def crawler():
    key = "python"
    keyword = urllib.parse.quote(urllib.parse.quote(key))
    print(keyword)
    pageNo = 1

    databasePath = "51job.db"
    checkIfSQLitePrepared(databasePath)
    removeAllDataFromSQLite(databasePath)

    while True:
        htmlContent = getDataByKeywordAndPageNo2(keyword, pageNo)
        searchResult = resolveHtmlContent(htmlContent)
        if searchResult is None or 0 == len(searchResult):
            break
        else:
            storeDataToSQLite(searchResult, databasePath)
        pageNo = pageNo + 1


if __name__ == "__main__":
    crawler()
    # databasePath = "51job.db"
    # readDataFromSQLite(databasePath)
