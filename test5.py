# from my_package import stringutils as su, numberutils as nu, dateutils as du

# print(su.reverse_string("Hello, World!"))
# print(nu.to_money(1000000))
# print(du.to_date("2024-01-01"))
# print(type(du.to_date("2024-01-01")))

import my_package as mp

print(mp.stringutils.reverse_string("Hello, World!"))
# print(mp.to_money(1000000))
# print(mp.to_date("2024-01-01"))
# print(type(mp.to_date("2024-01-01")))