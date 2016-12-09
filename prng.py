# -*- coding: utf-8 -*-
import math
from datetime import datetime
from r4nd0m.SourceCode.RandomnessTests import RandomnessTester


def get_primes_in_range(size):
    def _is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    prime_list = []
    num = 0
    while len(prime_list) < size:
        num += 1
        if _is_prime(num):
            prime_list.append(num)
    return prime_list


def get_time_us_seed():
    return datetime.now().microsecond


def get_bbs_prandom_number(prime):
    seed = get_time_us_seed()
    return int(math.pow(seed, 2) % (prime))


def generate_prandom_sequence(size):
    prime_list = get_primes_in_range(size)
    list_1 = prime_list[:size]
    return [get_bbs_prandom_number(x) for x in list_1]


def main():
    random_sequence = generate_prandom_sequence(6)

    randtest = RandomnessTester(None)
    p_value = randtest.monobit(random_sequence)
    print(', '.join(map(str, random_sequence)))
    if p_value < 0.01:
        print(str(p_value) + ' not random')
    else:
        print(str(p_value) + ' is random')


if __name__ == '__main__':
    main()
