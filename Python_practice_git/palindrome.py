# check if a number is a palindrome
from utils import is_palindrome

if __name__ == "__main__":
    number = int(input("Enter the number: "))
    if is_palindrome(number):
        print(number , "is palindrome")
    else:
        print(number, "is not a palindrome")


