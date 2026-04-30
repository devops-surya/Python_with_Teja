# This program calculates the sum of the digits of a four car number until it is reduced to a single digit.  
result = 0 
number = 9999
while number > 0:
    remainder = number % 10
    result = result + remainder 
    number = number // 10
    if number == 0 and result > 9:
        number = result
        result = 0
print(result)
