# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
string = 'Leek is ' + str(leek_price) + ' euro per kilo.'
print(string)

order_string = 'leek 4'
place_of_number = order_string.find(' ') + 1
number_of_leek = order_string[place_of_number]
sum_total = leek_price * int(number_of_leek)
print(sum_total)

broccoli_price = 2.34
broccoli_order = 'broccoli 1.6'
place_of_number_broc = broccoli_order.find(' ') + 1
amount_of_broccoli = broccoli_order[place_of_number_broc:]
total_price = float(amount_of_broccoli) * broccoli_price
rounded_total_price = round(total_price, 2)
# print(rounded_total_price)
string_broccoli = str(amount_of_broccoli) + \
    'kg broccoli costs ' + str(rounded_total_price) + 'e'
print(string_broccoli)
