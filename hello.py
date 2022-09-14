def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def rem(a, b):
    return a % b


if __name__ == "__main__":
    numba1 = int(input("Enter the first number: "))
    numba2 = int(input("Enter the second number: "))
    while True:
        print(f'1: Add {numba1} and {numba2}''')
        print(f'2: Subtract {numba1} and {numba2}''')
        print(f'3: Multiply {numba1} and {numba2}''')
        print(f'4: Divide {numba1} and {numba2}''')
        print(f'5: Find Remainder {numba1} and {numba2}''')
        print(f'6: Exit')
        c = int(input("Enter your choice of operation: "))
        match c:
            case 1:
                print(f'The addition of {numba1} and {numba2} is {add(numba1, numba2)}\n')
            case 2:
                print(f'The subtraction of {numba1} and {numba2} is {sub(numba1, numba2)}\n')
            case 3:
                print(f'The multiplication of {numba1} and {numba2} is {mul(numba1, numba2)}\n')
            case 4:
                if rem(numba1, numba2) != 0:
                    print(f'The quotient obtained after dividing {numba1} and {numba2} is {int(div(numba1, numba2))} and the remainder is {rem(numba1, numba2)}\n')
            case 5:
                print(f'The remainder after dividing {numba1} and {numba2} is  {rem(numba1, numba2)}\n')
            case 6:
                break
