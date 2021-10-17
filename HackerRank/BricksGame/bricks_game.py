for _ in range(int(input())):
    input()
    vals = tuple(map(int, input().split()))

    dp = [(0, 0)] * (len(vals) + 3)

    for i in range(len(vals) - 1, -1, -1):
        my_max = opponent_max = -1
        for j in range(1, 4):
            sub_res = dp[i + j]
            my_new_max = sum(vals[i:i + j]) + sub_res[1]
            if my_new_max > my_max:
                my_max, opponent_max = my_new_max, sub_res[0]
        dp[i] = (my_max, opponent_max)
    
    print(dp[0][0])