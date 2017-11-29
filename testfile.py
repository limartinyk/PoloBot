import requests
import time
from poloniex import poloniex

def testfunc(req={}):
    return requests.get('https://poloniex.com/public?command=' + 'returnOrderBook' + '&currencyPair=' + str("BTC_XMR")).json()

def get_time():
    return time.time()


def test_chart():
    return requests.get('https://poloniex.com/public?command=returnChartData&currencyPair=BTC_XMR&start=1511867800&end=1511911000&period=1800').json()

def test_historical():
    pair = "BTC_XMR"
    startTime = 1511867800 #set to a value in seconds if using historical data, False if real-time
    endTime = 1511911000 #False if real-time, value in seconds if historical data
    period = 1800
    connect = poloniex('API key', 'Secret')
    return connect.api_query("returnChartData",{"currencyPair":pair,"start":startTime,"end":endTime,"period":period}).json()
