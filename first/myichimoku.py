import yfinance as yf
print ("@@@@@@@@@@@@@@@ Start")

def lines_situation(name,C,B,time):
    c=C
    b=B
    high=0
    low=10000000
    while(c>1):  #conversion ring
      the_price = yf.Ticker(name).history(period="1d", interval=time)['High'].iloc[-1*c]
      if high < the_price: high = the_price
      the_price = yf.Ticker(name).history(period="1d", interval=time)['Low'].iloc[-1*c]
      if low > the_price: low = the_price
      c=c-1
      
    c=(high+low)/2
    
    high=0
    low=0
    while(b>1):  #base ring
      the_price = yf.Ticker(name).history(period="1d", interval=time)['High'].iloc[-1*b]
      if high < the_price: high = the_price
      the_price = yf.Ticker(name).history(period="1d", interval=time)['Low'].iloc[-1*b]
      if low > the_price: low = the_price
      b=b-1
    b=(high+low)/2 
    
    
    if(c>b)  :
      return True
    elif(c<b):
      return False
    else : return "no"
    
#    input 
name="PEPE24478-USD"
conversion=9
base=26
time="15m"
TF=lines_situation(name,conversion,base,time)

print(name+" / "+time+" :")
if(TF==False):    print("\033[31mSELL  \033[0m"+str(TF))
elif(TF==True):  print("\033[32mBUY  \033[0m" + str(TF))
else: print("SAME!!!!!!!!!!")

print ("@@@@@@@@@@@@@@@@@@ end")


#PEPE24478-USD