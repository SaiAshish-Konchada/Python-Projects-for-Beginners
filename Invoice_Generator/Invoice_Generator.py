#take care of spacing when character of product increase

# create a product and price for three items
product1_name, product1_price = 'Pen', 2.00
product2_name, product2_price = 'Car', 500.00
product3_name, product3_price = 'Pad', 15.00

# create a company name and information
company_name = 'The Insightful Coder, inc.'
company_address = '292 New Lane'
company_city = 'Mumbai'

# declare ending message
message = 'Thanks for shopping with us today!'

# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\t\tProduct Price')

# create a print statement for each item
print('\t{}\t\t\t\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t\t\t\t\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t\t\t\t${}'.format(product3_name.title(), product3_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))

# print a line between sections
print('=' * 50)

# output thank you message
print('\n\t{}\n'.format(message))

# create a bottom border
print('*' * 50)