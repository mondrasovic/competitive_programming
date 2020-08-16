for _ in range(int(input())):
    pile_size = int(input().split()[0])
    div_vals = tuple(map(int, input().split()))

    memo = {}

    def calc_max_steps(val):
        stored_val = memo.get(val)
        if stored_val is not None:
            return stored_val
        
        max_steps = 0
        for div in div_vals:
            if (div != val) and (val % div == 0):
                max_steps = max(
                    max_steps, 1 + calc_max_steps(div) * (val // div))
        memo[val] = max_steps
        
        return max_steps
    
    print(calc_max_steps(pile_size))
