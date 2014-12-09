#!/usr/bin/python


def fizzbuzz(n):
    ret = ""
    if (n % 3) == 0:
        ret += "fizz"
    if (n % 5) == 0:
        ret += "buzz"
    if ret:
        return ret
    return n


def printfizzbuzz1(n):
    for fb in range(1, n + 1):
        print fizzbuzz(fb)


def fizzbuzzgen(n):
    i = 1
    while(i<=n):
        yield fizzbuzz(i)
        i += 1


def printfizzbuzz2(n):
    print list(fizzbuzzgen(n))


def printfizzbuzz3(n):
    print '\n'.join(map(str, fizzbuzzgen(n)))


def main():
    printfizzbuzz1(15)
    printfizzbuzz2(15)
    printfizzbuzz3(15)


if __name__ == "__main__":
    main()
