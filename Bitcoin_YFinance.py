import yfinance as yf

btc_current_price = yf.Ticker("BTC-USD").history(period='1d')['Close'].iloc[-1]

print(f"The current price of Bitcoin is ${btc_current_price}")
