numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 169, -15]
Primes = []
notPrimes = []
for i in numbers:
    for j in (2, i):
        if i == j:
            break
        elif i == 2:
            Primes.append(i)
        elif i % j == 0 and (i != j):
            notPrimes.append(i)
        elif i < 1:
            notPrimes.append(i)
        elif i == 1:
            i += 1
        else:
            Primes.append(i)
print(f'простые:', Primes)
print(f'не простые:', notPrimes)

