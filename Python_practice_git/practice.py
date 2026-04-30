# Prime number 
number = 13
is_prime_number = True
index = 2
while index < number:
    if number % index == 0:
        is_prime_number = False
        break
    index = index + 1
if is_prime_number == True:
    print(number, 'is a prime number')
else:
    print(number, 'is not a prime number')