for _ in range(int(input())):
    input()
    health_vals = sorted(list(map(int, input().split())), reverse=True)
    cumulative_sum = max_experience = 0
    for i, val in enumerate(health_vals):
        cumulative_sum += val
        max_experience = max(max_experience, (len(health_vals) - i) * cumulative_sum)
    print(max_experience)
