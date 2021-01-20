# Необходимо написать программу, которая вычисляет простые
# числа в пределах от 1 до N. N – вводится вручную во время
# выполнения программы.
# ввод:   N
# вывод   простые числа в пределах от 1 до N
__VERSION__ = '0.0.1'

def PrimeNumbers(N):
    numbers = []
    d = True
    if N < 2:
        print("The number must be greater than 1")
        return
    elif N == 2:
        print("2")
        return
    for i in range(2, N+1):
        for j in range(2, i):
            if i % j == 0:
                d = False
                break
        if d == True:
            numbers.append(i)
        else:
            d = True
    for i in numbers:
        print(i, end="\t")


def main():
    print("A program that calculates prime numbers from 1 to N.")
    while True:
        try:
            N = int(input("input N: "))
            print("Prime Numbers: ")
            PrimeNumbers(N)
            print()
            choice = input(
                "To continue, click Y, and to exit, any other key: ")
            if choice.lower() != "y":
                break
        except:
            print("incorrect input")
    print("program completed")
