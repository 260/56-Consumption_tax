#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/111

first_line          = input()
cost_and_tax_rate   = list(map(int, first_line.split(' ')))
cost                = cost_and_tax_rate[0]
tax_rate            = cost_and_tax_rate[1]

tax = int(cost * tax_rate / 100)

print(cost + tax)
