#for converting BTC in USD
#current BTU rate 11000 per 1$ USD
BTC = int(input("enter amount to convert"))
exchangeRate = float(input("current BTU rate:"))
USD = 1 
BTC = USD//exchangeRate
print ( "As of Aug. 31, 2020, 12:35 AM UTC, Bitcoin is currently trading at {0} per bitcoin.". format(USD))