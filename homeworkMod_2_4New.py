numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    k = 0
    for j in range(1, i+1):
        if i % j == 0 and i != j and j != 1:
            k += 1
            break
    if k == 0:
        primes.append(i)
    else: not_primes.append(i)
print(primes)
print(not_primes)
