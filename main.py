"""Module providing a function to add 2 numbers"""
from funcs import add_numbers

def main():
    """Main function to execute the program."""
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")


if __name__ == "__main__":
    main()