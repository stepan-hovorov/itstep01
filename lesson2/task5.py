n = int(input('What your number: '))

if 1 > n:
    print('n number need to be bigger 1 ')

if n % 2 == 0:

    while 1 <= n:
        print(n)
        n -=2
else:
    n -=1
    while 1 <= n:
        print(n)
        n -=2