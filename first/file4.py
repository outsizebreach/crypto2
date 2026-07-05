import yfinance as yf
print ("@@@@@@@@........@@@@ start")


#data = yf.Ticker('SOL-USD')

the_price=yf.Ticker("SOL-USD").history("1d")
['Close'].iloc[-1]

#['Close'].iloc[-1]

print(the_price)


print ("@@@@@@@@@@@@ end")