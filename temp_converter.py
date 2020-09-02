for tempConversions in range(3):
    inputCelsiusString = input("Enter the Temperature in C: ")
    tempInC = float(inputCelsiusString)
    tempInF = 1.8 * tempInC + 32
    print( "The Temperature in F is", tempInF, "degrees" )