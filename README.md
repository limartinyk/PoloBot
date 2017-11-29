# PoloBot

About the bot:

Trading Strategy:

When price on chart drops below the moving average, potential buy position.  
when price starts increasing again, enter long position  
when price starts decreasing, exit long position  

When price on chart rises above the moving average, potential sell position.  
When price starts decreasing, enter short position  
when price starts increasing, exit short position  

##### Bare minimum bot components:  
- feedback to command line as trades happen or something
- connect to api
- calculate moving average as it goes
- backtest data for testing purposes
- make trades

BOT STOPS WHENEVER THERE IS A POTENTIAL ERROR

##### Files

SMATrader.py is bot with historical testing using SMA

SMATrader-returns.py assumes input of 1 bitcoin and returns resulting bitcoin from trading decisions at bottom, 
prints btc resulting from using bot, btc from holding btc, and btc from holding opposing currency

Testfile.py was used to test functions


##### Potential additions:

secondary, shorter period moving average, look at when moving averages cross over  
example: 5 8 13 day triple moving average, common technical analysis, 13 day is general trend, 8 is medium, 5 is short term, when they cross gives different indications for trading

stop losses in crisis


##### Long term:  

machine learning trading lol
