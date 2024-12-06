def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5
    d = 2

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(*[i for i in range(50) if is_prime(i)])
primes = []
not_primes = []
for i in range(len(numbers)):
    if is_prime(numbers[i]):
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)
