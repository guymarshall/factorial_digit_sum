"""
n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

def factorial(number):
    result = 1
    counter = 1

    while counter <= number:
        result *= counter
        counter += 1
    return result

def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    
    return sum

def main():
    print(f"6 factorial: {factorial(6)}")
    print(f"Sum of digits in 1128: {sum_digits(1128)}")

if __name__ == "__main__":
    main()