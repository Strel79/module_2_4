numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lower = numbers[0]
upper = numbers[-1]
#print(lower, upper)
primes = []
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
            #print(num)
not_primes = [x for x in numbers if x not in primes and x != 1]
print('Primes:', list(primes))
print('Not Primes:', list(not_primes))
