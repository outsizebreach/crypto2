import yfinance as yf

print ("@@@@@@@@@@@@@@@ Start")


def macd_line(sesion,price_list):
    s=sesion
    some=0.0
    for i in range(12):
      some=some+price_list[s]
      s=s+1
    EMA12=float(some/12)  
    
    s=sesion
    some=0.0   
    for l in range(26):
        some=some+price_list[s]
        s=s+1
    EMA26=float(some/26)
    
    return EMA12-EMA26


def signal_line(price_list):
    some=0.0
    for i in range(9):
        some=some+macd_line(i,price_list)
    returning=float(some/9)    
    return returning

def MACD(coin,time):
    price_list=[]
    s=1
    for i in range(40):
       the_price = yf.Ticker(coin).history(period="1d", interval=time)['Open'].iloc[-1*s]    
       price_list.append(the_price)
       s=s+1
       #price_list.append(yf.Ticker(coin).history(period="1d", interval=time)['Close'].iloc[-1*(i+1)])
     
     
    macd=macd_line(0,price_list)
    signal=signal_line(price_list)
     
    print (macd)
    print(signal)
    print(macd-signal)
    if(macd>signal): return True
    elif(macd<signal): return False
    else: return "cant macd"
     
coin="PEPE24478-USD"
time="5m"
print("MACD: "+coin+" / "+time+" :")
TF=MACD(coin,time)
print(TF)
print ("@@@@@@@@@@@@@@@@@@ end")

#PEPE24478-USD