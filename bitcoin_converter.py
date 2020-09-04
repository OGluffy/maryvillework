#for converting BTC in USD
#current BTU rate 11000 per 1$ USD
exchangeRate = 11000.0
print ( "As of Aug. 31, 2020, 12:35 AM UTC, Bitcoin is currently trading at {0} per bitcoin.".format(exchangeRate))
BTC = float(input("enter the BTC amount "))
currentBTC = BTC * exchangeRate
print ("that is worth", currentBTC, "dollars")
