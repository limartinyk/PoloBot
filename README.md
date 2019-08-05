# PoloBot

SMATrader.py trades using the SMA trading strategy described below. It can also be run in a trial mode where it assumes an initial wallet of 1 BTC, and prints the amount that your BTC changes as a result of running the bot, at every time step, showing the profit/loss when using the SMA strategy, and the profit/loss when holding BTC or the opposing currency

Arbitrager.py arbitrages between three currency pairs on Poloniex. The given file arbitrages between Bitcoin, Stellar Lumens, and USDT

Gdaxapidatacollector.py writes to a csv file using GDAX's api, which is another cryptocurrency trading platform. Originally, I meant for the other bots to trade on GDAX, which is why I made this. The file can also be customized to get data from CoinMarketCap.com

Poloniex.py is the wrapper for use with Poloniex's trading api

##### Trading Bot Features

- feedback to command line as events happen
- connect to api and request information
- calculate moving average as it is running using real-time data
- connect to api and make trades

##### SMA Trading Strategy:

The SMATrader bot uses this following strategy:

When price on chart drops below the moving average, potential buy position.  
when price starts increasing again, enter long position  
when price starts decreasing, exit long position  

When price on chart rises above the moving average, potential sell position.  
When price starts decreasing, enter short position  
when price starts increasing, exit short position

I chose this trading strategy for its simple implementation, and not for it's ability to succeed.

##### Using the Bots:

Customize:
- Period in which the bots check for potential actions
- Currencies being traded
- Length of trailing moving average used in the SMA strategy

Using on the Market
- Input apikey and secret for poloniex account in poloniex.py
- Uncomment the lines that actually make trades in the decision making part of the bot
- Change startTime to False
- Change endTime to False  

Trial run:
- Comment out the lines that make trades in decision making section
- Specify startTime using unix timestamp
- Specify endTime using unix timestamp
