search_key = None
while True:
    search_key = input("Search by invoice id (id) or customer last name (lname)? ")
    if search_key == 'id' or search_key == 'lname':
        break
    else:
        print("ERROR: You must enter either 'id' for invoice id or search 'lname' for customer last name search")

search_term = input('Enter your search id or lname: ')
sales_file = open('sales_data.csv', 'r')
lines = sales_file.readlines()
#print(lines)

number_of_matched_records = 0

for line in lines:
#    print(line)
    line_token = line.strip().split(',')
#    print(line_token)

    target_column = 2
    if search_key =='id':
        target_column = 0
    
    if line_token[target_column] == search_term:
        print(line.strip())
        number_of_matched_records += 1

print('records found: {0}'.format(number_of_matched_records))

sales_file.close()
