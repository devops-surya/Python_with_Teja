# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. FInd the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1
result = 0 
index = 1 
while index < 1000:
    if index % 3 == 0 or index % 5 == 0:
        result = result + index 
    index = index + 1
print(result)
