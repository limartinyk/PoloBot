# PoloBot

##### SMA Trading Strategy:

When price on chart drops below the moving average, potential buy position.  
when price starts increasing again, enter long position  
when price starts decreasing, exit long position  

When price on chart rises above the moving average, potential sell position.  
When price starts decreasing, enter short position  
when price starts increasing, exit short position  

Known that this strategy is awful

##### Bare minimum bot components:  
- feedback to command line as trades happen or something
- connect to api
- calculate moving average as it goes
- backtest data for testing purposes
- make trades

BOT STOPS WHENEVER THERE IS A POTENTIAL ERROR

##### Files

poloniex.py is wrapper for use with poloniex trading api  

SMATrader.py is bot with historical testing using SMA

SMATrader-returns.py assumes input of 1 bitcoin and returns resulting bitcoin from trading decisions at bottom, 
prints btc resulting from using bot, btc from holding btc, and btc from holding opposing currency

Testfile.py was used to test functions

gdaxapidatacollector.py writes to historical_data.csv using gdax api, the bot was originally meant to trade on gdax. File can be customized to get data from CoinMarketCap for use for backtesting.


##### Potential additions:

secondary, shorter period moving average, look at when moving averages cross over  
example: 5 8 13 day triple moving average, common technical analysis, 13 day is general trend, 8 is medium, 5 is short term, when they cross gives different indications for trading

stop losses in crisis


##### Long term:  

machine learning trading lol

##### USAGE:

both bots:
- period between code being run is customizable
- pair of currencies is customizable between all available btc-curr pairs on poloniex, 
can be modified to trade multiply pairs at once
- length of trailing moving average can be specified

to use either bot on the market:
- input apikey and secret for poloniex account
- uncomment the lines that actually make trades in the decision making part of the code
- change startTime to False
- change endTime to False  

to test either bot on historical data:
- comment out the lines that make trades in decision making section
- specify startTime using unix timestamp
- specify endTime using unix timestamp

smatrader-returns.py
- specify in accVal what initial BTC input is for historical testing
- bot third to last line outputs ending account value if using strategy
- bot second to last line outputs ending account value if holding btc without trading
- bot third to last line outputs ending account value (in BTC) if holding opposing currency of btc-curr pair without trading

https://www.unixtimestamp.com/
