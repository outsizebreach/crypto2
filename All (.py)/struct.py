import yfinance as yf
class struct:
    def __init__(self,coin,position,price_now,percent):
        self.coin=coin
        self.price_now=price_now  
        self.position=position
        self.percent=percent
        if position==True :
            self.tp=price_now + (price_now*percent)/100
            self.sl=price_now - (price_now*percent)/200
        elif position==False :
            self.tp=price_now - (price_now*percent)/100
            self.sl=price_now + (price_now*percent)/200
        else:
            self.tp=0
            self.sl=0
        
    def show_info(self):
        print("coin: "+ self.coin + "\n"+"position: "+ self.position + "\n"+ "TP: "+self.tp + "\n"+"SL: "+self.sl+ "\n")
        
    def where_is_benefit(self,new_price,time):
        if self.position==True :
           high=yf.Ticker(self.coin).history(period = "1d", interval = time)['High'].iloc[-1]
           low=yf.Ticker(self.coin).history(period = "1d", interval = time)['Low'].iloc[-1]
           if low<=self.sl :
              return -self.percent/2
           #high=yf.Ticker(self.coin).history(period = "1d", interval = time)['High'].iloc[-1]
           elif high>=self.tp :
              return self.percent
           else:
              x=((new_price- self.price_now)*100)/self.price_now
              return x
        
        elif self.position==False :
           high=yf.Ticker(self.coin).history(period = "1d", interval = time)['High'].iloc[-1]
           low=yf.Ticker(self.coin).history(period = "1d", interval = time)['Low'].iloc[-1]
           if high>=self.sl :
              return -self.percent/2
           #high=yf.Ticker(self.coin).history(period = "1d", interval = time)['High'].iloc[-1]
           elif low<=self.tp :
              return self.percent
           else:
              x= -((new_price- self.price_now)*100)/self.price_now
              return x