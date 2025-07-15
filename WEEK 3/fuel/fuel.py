'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''


def main():

    while True:
        try:
            fraction = input("Fraction: ")
            parts = fraction.split("/")

            x = int(parts[0])
            y = int(parts[1])

            if x > y or y <= 0 or x < 0:
                continue

            result = fuel(x, y)

            if result <= 1:
                print("E")
            elif result >= 99:
                print("F")
            else:
                print(f"{round(result)}%")

            break

        except (ValueError, IndexError):
            continue


def fuel(x, y):
    return (x/y) * 100


main()
