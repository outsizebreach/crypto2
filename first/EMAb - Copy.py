import yfinance as yf

print ("@@@@@@@@@@@@@@@ Start")


def macd_line(sesion,price_list):
    s=sesion
    some=0.0
    
    value_today=price_list[0]
    value_yesterday=price_list[1]
    EMA12=value_today*(2/(1+12)) + value_yesterday*(1-(2/(1+12)))
    EMA26=value_today*(2/(1+26)) + value_yesterday*(1-(2/(1+26)))
    
    return EMA12-EMA26


def signal_line(price_list):
    some=0.0
    
    
    returning=float(some/9)    
    return returning

def MACD(coin,time):
    price_list=[]
    for i in range(3):
       the_price = yf.Ticker(coin).history(period="1d", interval=time)['Open'].iloc[-1*(i+1)]    
       price_list.append(the_price)
       #price_list.append(yf.Ticker(coin).history(period="1d", interval=time)['Close'].iloc[-1*(i+1)])
     
     
    macd=macd_line(1,price_list)
    signal=macd*(2/(1+9))
     
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