# _*_ coding: utf-8 _*_
# coding: utf-8
# @Author : waylanpunch
# @Time : 2021/7/18 22:56
# @File : SpiderCrawler.py
# @Software : PyCharm
from flask import Flask, render_template, request
from SQLite3Utils import readDataFromSQLite

app = Flask(__name__)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


@app.route('/')
def index():
    # databasePath = "51job.db"
    # jobs = readDataFromSQLite(databasePath)
    return render_template("index.html")


@app.route('/index')
def index2():
    # databasePath = "51job.db"
    # jobs = readDataFromSQLite(databasePath)
    return render_template("index.html")


@app.route('/tables')
def table():
    databasePath = "51job.db"
    jobs = readDataFromSQLite(databasePath)
    return render_template("tables.html", jobs=jobs)


if __name__ == '__main__':
    app.run(debug=True)
