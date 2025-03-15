import sys
def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(3 * number + 1)

try:
    while True:    
        try:
            print("Please input number: ", end='')
            num = input()
            print(collatz(int(num)))
        except ValueError:
            print("Please input NUMBER!!")
except KeyboardInterrupt:
    sys.exit()
