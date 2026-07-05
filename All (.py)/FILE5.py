
import yfinance as yf
print ("@@@@@@@@........@@@@ start")


data = yf.Ticker("")
the_price = yf.Ticker("PEPE24478-USD").history(period="1d", interval="5m")['Close'].iloc[-1]

print ("@@@@@@@@@@@@ end")


#PEPE24478-USD