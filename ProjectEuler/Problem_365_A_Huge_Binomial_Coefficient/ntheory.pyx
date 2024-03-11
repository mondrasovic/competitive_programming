# cython_module.pyx
from libc.stdlib cimport malloc, free

cpdef unsigned long long int n_choose_r_mod_p_pascal(unsigned long long int n, unsigned long long int r, unsigned long long int m):
    if r == 0 or r == n:
        return 1
    if r > n:
        return 0

    cdef unsigned long long int* n_choose_r = <unsigned long long int*>malloc((r + 1) * sizeof(unsigned long long int))
    cdef unsigned long long int i, j

    for i in range(r + 1):
        n_choose_r[i] = 0
    n_choose_r[0] = 1

    for i in range(1, n + 1):
        for j in range(min(r, i), 0, -1):
            n_choose_r[j] = (n_choose_r[j] + n_choose_r[j - 1]) % m

    result = n_choose_r[r]
    free(n_choose_r)
    return result

cpdef unsigned long long int n_choose_r_mod_p_lucas(unsigned long long int n, unsigned long long int r, unsigned long long int m):
    if r == 0:
        return 1
    if r > n:
        return 0
     
    return (
        n_choose_r_mod_p_lucas(n // m, r // m, m) * n_choose_r_mod_p_pascal(n % m, r % m, m)
    ) % m

cpdef unsigned long long int inv(unsigned long long int a, unsigned long long int m):
    cdef unsigned long long int m0 = m  
    cdef unsigned long long int x0 = 0
    cdef unsigned long long int x1 = 1
  
    if m == 1:
        return 0
  
    cdef unsigned long long int q, t
    while a > 1:
        q = a // m  
        t = m

        m = a % m  
        a = t  

        t = x0  
        x0 = x1 - q * x0  
        x1 = t  
      
    if x1 < 0:
        x1 = x1 + m0  
  
    return x1  

cpdef unsigned long long int chinese_remainder(list nums, list rems):
    cdef unsigned long long int prod = 1
    cdef unsigned long long int result = 0
    cdef unsigned long long int pp
    cdef unsigned long long int i

    for i in range(len(nums)):
        prod *= nums[i]  
  
    for i in range(len(nums)):
        pp = prod // nums[i]  
        result += <unsigned long long int>(rems[i]) * <unsigned long long int>(inv(pp, nums[i])) * <unsigned long long int>(pp)
      
      
    return result % prod 
