numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 169, -15, 81, 121, 0]
Primes = []
notPrimes = []
for i in numbers:
    IsPrime = True
    if i < 1:
        IsPrime = False
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            IsPrime = False
            break
    if IsPrime == True:
        Primes.append(i)
    if IsPrime == False:
        notPrimes.append(i)
print('простые:', Primes)
print('не простые:', notPrimes)
