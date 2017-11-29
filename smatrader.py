import time
import sys
import datetime
from poloniex import poloniex

def main():

    #initializations / customizables
    period = 1800 #how often program runs in seconds
    if (int(period) not in [300, 900, 1800, 7200, 14400, 86400]):
        print('Poloniex requires periods in 300, 900, 1800, 7200, 14400, or 86400 second increments for charting')
        sys.exit(2)

    pair = "BTC_XMR" #Bitcoin to Monero

    lengthOfMA = 10 #how many periods (above) to use to calculate moving average
    prices = []
    currentMovingAverage = 0;

    startTime = 1511867800 #set to a value in seconds if using historical data, False if real-time
    endTime = 1511911000 #False if real-time, value in seconds if historical data
    historicalData = False
    tradePlaced = False
    typeOfTrade = False
    dataDate = ""
    orderNumber = ""

    #connecting to polo api
    connect = poloniex('API key', 'Secret') #plug in API key and secret for account

    if (startTime):
        historicalData = connect.api_query("returnChartData",{"currencyPair":pair,"start":startTime,"end":endTime,"period":period}).json()

    #trading
    while True:
        if (startTime and historicalData): #if testing on historical data (if startTime is not false, we are testing over historical data)
            if bool(historicalData): #empty lists evaluate to False
                nextDataPoint = historicalData.pop(0) #starting from oldest data
                lastPairPrice = nextDataPoint['weightedAverage']
                dataDate = datetime.datetime.fromtimestamp(int(nextDataPoint['date'])).strftime('%Y-%m-%d %H:%M:%S')
        elif (startTime and not historicalData): #if no historical data is provided
            exit()
        else:#if not trading with historical data
            currentValues = connect.api_query("returnTicker")
            lastPairPrice = currentValues[pair]["last"]
            dataDate = datetime.datetime.now()


        #implementing moving average
        if (len(prices) > 0):
            currentMovingAverage = sum(prices) / len(prices)

            #implementing logic for trading by moving averages (ONLY 1 POSITION AT A TIME)
            previousPrice = prices[-1]
            #if not in a position
            if (not tradePlaced):
                #if price rises above moving avg then decreases in value, sell order
                if ((lastPairPrice > currentMovingAverage) and (lastPairPrice < previousPrice)):
                    print("SELL ORDER")
                    # orderNumber = connect.sell(pair,lastPairPrice,.01) UNCOMMENT WHEN ACTUALLY TRADING
                    tradePlaced = True
                    typeOfTrade = "short"
                #if price goes below moving avg then increases, buy order
                elif ((lastPairPrice < currentMovingAverage) and (lastPairPrice > previousPrice)):
                    print("BUY ORDER")
                    # orderNumber = connect.buy(pair,lastPairPrice,.01) UNCOMMENT WHEN ACTUALLY TRADING
                    tradePlaced = True
                    typeOfTrade = "long"
            #if in position and price crosses over moving avg again, exit position
            elif (typeOfTrade == "short"):
                if (lastPairPrice < currentMovingAverage):
                    print("EXIT TRADE")
                    # if orderNumber not in connect.returnOpenOrders(pair): #if order was filled earlier
                        # orderNumber = connect.buy(pair,lastPairPrice,.01) UNCOMMENT WHEN ACTUALLY TRADING
                    # else:
                        # connect.cancel(pair,orderNumber) UNCOMMENT WHEN ACTUALLY TRADING
                        # cancels unfulfilled order
                    tradePlaced = False
                    typeOfTrade = False
            #if in position and price crosses over moving avg again, exit position
            elif (typeOfTrade == "long"):
                if (lastPairPrice > currentMovingAverage):
                    print("EXIT TRADE")
                    # if orderNumber not in connect.returnOpenOrders(pair): #if order was filled earlier
                        # orderNumber = connect.sell(pair,lastPairPrice,.01) UNCOMMENT WHEN ACTUALLY TRADING
                    # else:
                        # connect.cancel(pair,orderNumber) UNCOMMENT WHEN ACTUALLY TRADING
                        #cancels unfulfilled order
                    tradePlaced = False
                    typeOfTrade = False
        else:
            previousPrice = 0

        #feedback to user
        print("%s Period: %ss %s: %s Moving Average: %s" % (dataDate,period,pair,lastPairPrice,currentMovingAverage))

        #append price at this timestamp to the end of prices
        prices.append(float(lastPairPrice))

        #make sure prices is at most "lengthOfMA" long
        prices = prices[-lengthOfMA:] #keep the last "lengthOfMA" entries in prices



        #wait for length of period but only if not using historical data
        if (not startTime):
            time.sleep(int(period))

#runs main when python trader.py is run
if __name__ == "__main__":
    main()
