import math
import more_itertools

import tqdm

# import pyximport
# import tqdm

# pyximport.install()

from ntheory import n_choose_r_mod_p_lucas, chinese_remainder

def main() -> None:
    primes = [prime for prime in more_itertools.sieve(5000) if prime > 1000]

    N = 10 ** 18
    K = 10 ** 9

    result = 0

    with tqdm.tqdm(total=math.comb(len(primes), 3)) as pbar:
        for i, p in enumerate(primes):
            res_p = n_choose_r_mod_p_lucas(N, K, p)

            for j in range(i + 1, len(primes)):
                q = primes[j]
                res_q = n_choose_r_mod_p_lucas(N, K, q)

                for k in range(j + 1, len(primes)):
                    r = primes[k]
                    res_r = n_choose_r_mod_p_lucas(N, K, r)
                    result += chinese_remainder([p, q, r], [res_p, res_q, res_r])
                    pbar.update()
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()