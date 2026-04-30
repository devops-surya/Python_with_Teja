
def is_prime(number:int) -> bool:
    """This function checks the number is prime or not

    Args:
        number (int): number to be verified

    Returns:
        bool: return true -  if it is prime, false - if it is not prime
    """
    index = 2 
    is_prime_result = True
    if number < 2:
        is_prime_result = False
    else:
        while index < number:
            if number % index == 0:
                is_prime_result = False
                break
            index += 1
    return is_prime_result


#response = is_prime(7)

#print(response)



def is_palindrome(number:int)-> bool:
    """This function checks whether the number is palindrome or not

    Args:
        number (int): number to be verified
    Returns:
        bool: True - if it is palindrome, False - if it is not palindrome
    """

    #number = 151
    original = number
    reverse = 0
    while number > 0:
        remainder = number % 10 
        reverse = reverse * 10 + remainder
        number = number // 10
    if reverse == original:
        is_palindrome_result = True
    else:
        is_palindrome_result = False

    return is_palindrome_result


#response = is_palindrome(456)

#print(response)