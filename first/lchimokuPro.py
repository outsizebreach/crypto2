import yfinance as yf
print ("@@@@@@@@@@@@@@@ Start")

def ichimoku_def(coin,C,B,time):
    c=C
    b=B
    high_list=[]
    low_list =[]

    stop=30
    while(stop>1):
      the_price = yf.Ticker(coin).history(period="1d", interval=time)['High'].iloc[-1*stop]
      high_list.append(the_price)
      the_price = yf.Ticker(coin).history(period="1d", interval=time)['Low'].iloc[-1*stop]
      low_list.append(the_price)
      stop=stop-1
    
    high=0
    low=1000000
    while(c>=1):
      if high<high_list[c]: high=high_list[c]
      if low>low_list[c]: low=low_list[c]
      c=c-1
    c=(high+low)/2
    
    high=0
    low=1000000
    while(b>=1):
      if high<high_list[b]: high=high_list[b]
      if low>low_list[b]: low=low_list[b]
      b=b-1
    b=(high+low)/2
    
    if(c>b)  :
      return True
    elif(c<b):
      return False
    else :  return "no"
      
print("Pro!!! result: ")  

coin="PEPE24478-USD"
conversion=9
base=26
time="15m"

TF=ichimoku_def(coin,conversion,base,time)

print(coin+" / "+time+" :")
if(TF==False):    print("\033[31mSELL  \033[0m"+str(TF))
elif(TF==True):  print("\033[32mBUY  \033[0m" + str(TF))
else: print("SAME!!!!!!!!!!")

print ("@@@@@@@@@@@@@@@@@@ end")