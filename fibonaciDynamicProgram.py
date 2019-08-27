import sys

max = sys.maxsize
lookup = []


def populate_lookup(x: int):
    for i in range(0, x+1):
        lookup.append(-1)


def fib(x: int):
    if lookup[x] == -1:
        if(x == 0):
            lookup[x] = 0
        elif(x == 1):
            lookup[x] = 1
        else:
            lookup[x] = fib(x-1) + fib(x-2)
    return lookup[x]


if __name__ == "__main__":
    x = int(input("Please enter x:"))
    populate_lookup(x)
    fib(x)
    for i in range(0, x+1):
        print(lookup[i], sep=' ')
