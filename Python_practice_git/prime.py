
from utils import is_prime

if __name__ == "__main__":
    number = int(input("Enter your number :"))
    if is_prime(number):
        print(number, "is prime number")
    else:
        print(number, "is not a prime number")

