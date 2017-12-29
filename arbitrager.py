import time
import sys
import datetime
from poloniex import poloniex

def main():

    #initializations / customizables
    period = .5 #how often program runs in seconds

    #pairtrio = btc, xmr, zec
    #follow naming standard pair1, pair 2, pair1pair2 or IT WILL FUCK UP
    BTCpair1 = "USDT_BTC"
    BTCpair2 = "USDT_STR"
    pair1pair2 = "BTC_STR"

    tradePlaced = False #false only if back at btc, otherwise, indicate direction pair1 to pair 2 or pair2 to pair1
    direction = False
    stage = False #which stage of the pairs, be it btc, pair1, pair2, btc
    dataDate = ""
    orderNumber = ""


    #connecting to polo api
    connect = poloniex('key here', 'secret here') #plug in API key and secret for account

    #trading
    while True:
        BTCpair1info = connect.api_query("returnOrderBook", {"currencyPair":BTCpair1})
        BTCpair2info = connect.api_query("returnOrderBook", {"currencyPair":BTCpair2})
        pair1pair2info = connect.api_query("returnOrderBook", {"currencyPair":pair1pair2})

        BTCpair1lowestAsk = float(BTCpair1info["asks"][0][0])
        BTCpair1lowestAskVol = float(BTCpair1info["asks"][0][1])
        BTCpair1highestBid = float(BTCpair1info["bids"][0][0])
        BTCpair1highestBidVol = float(BTCpair1info["bids"][0][1])

        BTCpair2lowestAsk = float(BTCpair2info["asks"][0][0])
        BTCpair2lowestAskVol = float(BTCpair2info["asks"][0][1])
        BTCpair2highestBid = float(BTCpair2info["bids"][0][0])
        BTCpair2highestBidVol = float(BTCpair2info["bids"][0][1])

        pair1pair2lowestAsk = float(pair1pair2info["asks"][0][0])
        pair1pair2lowestAskVol = float(pair1pair2info["asks"][0][1])
        pair1pair2highestBid = float(pair1pair2info["bids"][0][0])
        pair1pair2highestBidVol = float(pair1pair2info["bids"][0][1])

        dataDate = datetime.datetime.now()

        #if not in a positional loop:
        if (not tradePlaced):

            # if btc_zec/btc_xmr > xmr_zec:
                #trade btc to xmr price(lowest sell order) .25%
                #trade xmr to zec price(lowest sell order) .25%
                #trade zec to btc price(highest buy order) .25%
            #elif btc_zec/btc_xmr < xmr_zec:
                #trade btc to zec price(lowest sell order) .25%
                #trade zec to xmr price(highest buy order) .25%
                #trade xmr to btc price(highest buy order) .25%

            #if loop is initiated, go through whole loop with whatever is put into first transaction, no matter what
            print ("pair1 to pair2: %s" % ((BTCpair2highestBid/(BTCpair1lowestAsk * pair1pair2lowestAsk)) * (.9975)*(.9975)*(.9975)))
            print ("pair2 to pair1: %s" % (((BTCpair1highestBid * pair1pair2highestBid)/BTCpair2lowestAsk) * (.9975)*(.9975)*(.9975)))
            if ((BTCpair2highestBid/(BTCpair1lowestAsk * pair1pair2lowestAsk)) * (.9975)*(.9975)*(.9975)) > 1:
                print("Buying BTCpair1")
                #convert all order sizes to BTCpair1
                ordersize = min(BTCpair1lowestAskVol, (pair1pair2lowestAskVol*pair1pair2lowestAsk)*(1/.9975), BTCpair2highestBidVol*pair1pair2lowestAsk*(1/.9975)*(1/.9975))
                orderNumber = connect.buy(BTCpair1, BTCpair1lowestAsk, ordersize, immediateOrCancel=1)
                tradePlaced = True
                direction = "pair1 to pair2"
                stage = "pair1"

            elif (((BTCpair1highestBid * pair1pair2highestBid)/BTCpair2lowestAsk) * (.9975)*(.9975)*(.9975)) > 1:
                print("Buying BTCpair2")
                ordersize = min(BTCpair2lowestAskVol, pair1pair2highestBidVol *(1/.9975), BTCpair1highestBidVol/pair1pair2lowestAsk*(1/.9975)*(1/.9975))
                orderNumber = connect.buy(BTCpair2, BTCpair2lowestAsk, ordersize, immediateOrCancel=1)
                tradePlaced = True
                direction = "pair2 to pair1"
                stage = "pair2"

        #in trade loop

        elif direction == "pair1 to pair2":
            if stage == "pair1":
                print("Buying BTCpair2")
                ordersize = float(orderNumber["resultingTrades"]["amount"])
                orderNumber = connect.buy(pair1pair2, pair1pair2lowestAsk*1.1, ordersize, immediateOrCancel=1)
                stage = "pair2"
            elif stage == "pair2":
                print("Buying BTC")
                ordersize = float(orderNumber["resultingTrades"]["amount"])
                orderNumber = connect.sell(BTCpair2, BTCpair2highestBid/1.1, ordersize, immediateOrCancel=1)
                stage = False
                tradePlaced = False
                direction = False
                #end loop after finishing trade

        elif direction == "pair2 to pair1":
            if stage == "pair2":
                print("Buying BTCpair1")
                ordersize = float(orderNumber["resultingTrades"]["amount"])
                orderNumber = connect.sell(pair1pair2, pair1pair2lowestAsk/1.1, ordersize, immediateOrCancel=1)
                stage = "pair1"
            elif stage == "pair1":
                print("Buying BTC")
                ordersize = float(orderNumber["resultingTrades"]["amount"])
                orderNumber = connect.sell(BTCpair1, BTCpair1highestBid/1.1, ordersize, immediateOrCancel=1)
                stage = False
                tradePlaced = False
                direction = False
                #end loop after finishing trade


        #feedback to user
        print("%s Period: %ss" % (dataDate,period))

        time.sleep(int(period))

#runs main when python trader.py is run
if __name__ == "__main__":
    main()
