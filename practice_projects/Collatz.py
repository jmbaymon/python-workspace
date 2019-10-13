number = input("Enter a Number: ")


def collatz(number):
    try:
        number = int(number)

        if number % 2 == 0:
            new_num = number // 2
            print(new_num)
            return new_num

        elif number % 2 == 1:
            new_num = 3 * number + 1
            print(new_num)
            return new_num
    except ValueError:
        print("Error: Use an integer")
        raise


col_number = collatz(number)

while col_number != 1:
    col_number = collatz(col_number)
