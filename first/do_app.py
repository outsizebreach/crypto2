from pystruuct import struct
from TheMaccd import pos_def
import yfinance as yf
import time


pepe_15=struct(1,1,1,1)
pepe_5=struct(1,1,1,1)
ETH_list=[]
shib_list=[]
BTC_list=[]

#benefit=0
pepe_15_benefit=0
pepe_5_benefit=0
while pepe_15_benefit<100:
  pos=pos_def("PEPE24478-USD", "15m")
  price=yf.Ticker("PEPE24478-USD").history(period = "1d", interval = "15m")['Close'].iloc[-1]
  
  if pepe_15.coin==1:
    if pos== True or pos== False:
      pepe_15=struct("PEPE24478-USD",pos,price,2) # coin  position  price_now  percent%
      
  elif pepe_15.position != pos:
    pepe_15_benefit=pepe_15_benefit+pepe_15.where_is_benefit
    if pos==True or pos==False:
        pepe_15=struct("PEPE24478-USD",pos,price,2)
    else:
        pepe_15=struct(1,1,1,1)
   
  else:
    high=yf.Ticker(pepe_15.coin).history(period = "1d", interval = "15m")['High'].iloc[-1]
    low=yf.Ticker(pepe_15.coin).history(period = "1d", interval = "15m")['Low'].iloc[-1]
    if pepe_15.position==True :
      if high>=pepe_15.tp :
        pepe_15_benefit=pepe_15_benefit+pepe_15.percent
        pepe_15=struct("PEPE24478-USD",pos,price,2)
      elif low<=pepe_15.sl :
        pepe_15_benefit=pepe_15_benefit - pepe_15.percent/2
        pepe_15=struct("PEPE24478-USD",pos,price,2)
   
    elif pepe_15.position==False :
      if low<=pepe_15.tp :
        pepe_15_benefit=pepe_15_benefit+pepe_15.percent
        pepe_15=struct("PEPE24478-USD",pos,price,2)
      elif high>=pepe_15.sl :
        pepe_15_benefit=pepe_15_benefit - pepe_15.percent/2
        pepe_15=struct("PEPE24478-USD",pos,price,2)
    
    
  print(pepe_15.position)
  print(pepe_15_benefit)
  time.sleep(250)
  current_time = time.localtime()         # دریافت زمان حال حاضر
  formatted_time = time.strftime("%H:%M:%S", current_time)   # فرمت کردن زمان به صورت ساعت:دقیقه:ثانیه
  if formatted_time=="09:11:11" : break