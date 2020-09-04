for tempConversions in range(3):
    inputFahrenheitString = input ("Enter the temp in F: ")
    tempinF = float(inputFahrenheitString)
    tempinC = (tempinF - 32.0) * (5.0/9.0)
    print( "The temp in C is", tempinC, "degrees" )
