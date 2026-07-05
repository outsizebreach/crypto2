print("Start*********************************************")
from tradingview_ta import TA_Handler,Interval, Exchange

time = ""
thelist=["BTCUSDT","PEPEUSDT","SHIBUSDT","ETHUSDT","AVAXUSDT"]
go=True
if go==True:
 for thesymbol in thelist:
   output= TA_Handler(symbol=thesymbol,screener='Crypto',exchange='Binance',interval="5m")
   output.get_analysis().summary
   print(thesymbol +" : "+ str(output.get_analysis().summary))
   
   time=output.interval
   

print("TimeFrame: "+time)
print("*********************************************END")