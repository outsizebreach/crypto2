import yfinance as yf
print ("@@@@@@@@@@@@@@@ Start")

def ichimoku_def(coin,C,B,time):  # c : Conversion line     B : Base line
    c=C  #9
    b=B #26
    high_list1=[]
    low_list1 =[]
    high_list2=[]
    low_list2 =[]
    stop=0
    
    while(stop<=B):
      the_price = yf.Ticker(coin).history(period="1d", interval=time)['High'].iloc[-1*stop]
      if stop<=c : high_list1.append(the_price)
      if stop<=b : high_list2.append(the_price)
      the_price = yf.Ticker(coin).history(period="1d", interval=time)['Low'].iloc[-1*stop]
      if stop<=c : low_list1.append(the_price)
      if stop<=b : low_list2.append(the_price)
      stop=stop+1
    
    high_list1.sort()
    low_list1.sort()
    high_list2.sort()
    low_list2.sort()
    c=(high_list1[-1]+low_list1[1])/2
    b=(high_list2[-1]+low_list2[1])/2
    
    #print(c)
    #print(b)
    
    if(c>b)  :
      return True
    elif(c<b):
      return False
    else :  return "no"
      
print("Pro!!! result: ")  

coin="PEPE24478-USD"
conversion=9
base=26
time="5m"
print(coin+" / "+time+" :")
TF=ichimoku_def(coin,conversion,base,time)
if(TF==False):    print("\033[31mSELL  \033[0m"+str(TF))
elif(TF==True):  print("\033[32mBUY  \033[0m" + str(TF))
else: print("SAME!!!!!!!!!!")

print ("@@@@@@@@@@@@@@@@@@ end")