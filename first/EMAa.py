import yfinance as yf

coin="BTC-USD"  #"PEPE24478-USD"
time="5m"
value_today=the_price = yf.Ticker(coin).history(period="1d", interval=time)['Close'].iloc[-1]                                                               
value_yesterday=the_price = yf.Ticker(coin).history(period="1d", interval=time)['Close'].iloc[-2]
r=value_today*(2/(1+12)) + value_yesterday*(1-(2/(1+12)))
t=value_today*(2/(1+26)) + value_yesterday*(1-(2/(1+26)))
print(value_today)
print(r)
print(t)
print("EMA: "+ str(t-r))