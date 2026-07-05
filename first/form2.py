from tradingview_ta import TA_Handler,Interval, Exchange


tesla =TA_Handler(symbol='TSLA',screener='america',exchange='NASDAQ',interval=Interval.INTERVAL_15_MINUTES)
analysis=tesla.get_analysis()
print("................1")
ichimoku_data=analysis.indicators["ichimoku"]
print("................1")
print(ichimoku_data["conversion_line"])
green=ichimoku_data["conversion_line"]
red=ichimoku_data["base_line"]
if red>green:
   print("RED")
if red<green:
   print("GREEN")
if red==green:
   print("same!") 
        