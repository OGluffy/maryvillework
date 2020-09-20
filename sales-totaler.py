inputFileName = input('Enter sales file name: ')
outputFileName = input('Enter the name for total sales files: ')

inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'w')

readSales = inputFile.readlines()

for number in readSales:
    splitDollar = numbers.strip('\n').replace('$', '').split(' ')
    firstSales = float(slpitDollar[0])
    secondSales = float(splitDollar[1])

    total = firstSales + secondSales

    order_Total_Message = '${:7.2f} ${:7.2f} ${:7.2f}\n'.format(firstSales, secondSales, total)
    outputFile.write(order_Total_Message)

inputFile.close()
outputFile.close()

print("\n Done writing total to: {0}".format(outputFile))
