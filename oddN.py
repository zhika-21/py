# Python program that prints the first 100 odd numbers:

def print_odd_numbers():
    count = 0
    num = 1
    while count < 100:
        print(num)
        num += 2
        count += 1

if __name__ == '__main__':
    print_odd_numbers()