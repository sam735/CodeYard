
lookup = []


def populate_lookup(x: int):
    for i in range(0, x+1):
        lookup.append(0)


def fib(x: int):
    lookup[0] = 0
    lookup[1] = 1
    for i in range(2, x+1):
        lookup[i] = lookup[i-1] + lookup[i-2]

if __name__ == '__main__':
    x = int(input('Enter the number:'))
    populate_lookup(x)
    fib(x)
    for i in lookup:
        print(i)