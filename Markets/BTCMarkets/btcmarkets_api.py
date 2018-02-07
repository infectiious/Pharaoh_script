#!/usr/bin/env python3
import argparse
import requests
import time
import datetime
import random
# import pymysql
from connections import hostname, username, password, portnumber, database


class MarketBTCMarkets(object):
    # Set variables for API String.
    domain = "https://api.btcmarkets.net"
    url = ""
    uri = ""

    # Function to build API string.
    def __init__(self, uri, name, market):
        super(MarketBTCMarkets, self).__init__()
        self.name = name
        self.uri = uri
        self.url = self.domain + uri
        self.market = market
        dbstr = market.lower() + "_" + name.lower()

    # Function to query API string and write to mysql database.
    def update_data(self):
       # db = pymysql.connect(host=hostname, user=username,
       #                      passwd=password, port=portnumber, db=database)
       # db.autocommit(True)
       # cur = db.cursor()
       r = requests.get(self.url, verify=True)
       ask = str(r.json()["bestAsk"])
       bid = str(r.json()["bestBid"])
       last = str(r.json()["lastPrice"])
       tstamp = r.json()["timestamp"]
       ltime = time.ctime(tstamp)
       utime = time.asctime(time.gmtime(tstamp))
       print (ask)
       print (str(r.json()))
       # query = "INSERT INTO " + dbstr + "(ask,bid,lastsale,recorded_time) " \
       #         "VALUES(%s,%s,%s,FROM_UNIXTIME(%s))" % (ask, bid, last, tstamp)
       # print (query)
       # cur.execute(query)
       # cur.close()
       # db.close()
