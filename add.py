#def add_numbers(a, b):
  #  return a + b

# Example usage
#num1 = $1
#num2 = $2

#result = add_numbers(num1, num2)
#print(f"The sum of {num1} and {num2} is: {result}")


import sys

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 add_numbers.py <num1> <num2>")
        sys.exit(1)

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")

