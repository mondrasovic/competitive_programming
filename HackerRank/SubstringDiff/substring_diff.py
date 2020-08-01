
for _ in range(int(input())):
    tokens = input().split()
    max_diffs_num, str_1, str_2 = int(tokens[0]), *tokens[1:]

    mismatches_count = [[0] * (len(str_1) + 1) for _ in range(len(str_2) + 1)]

    for i in range(1, len(str_1) + 1):
        for j in range(1, len(str_2) + 1):
            if str_1[i - 1] == str_2[j - 1]:
                mismatches_count[i][j] = mismatches_count[i - 1][j - 1]
            else:
                mismatches_count[i][j] = mismatches_count[i - 1][j - 1] + 1
    
    def check_substr_exists(str_len):
        for i in range(str_len, len(str_1) + 1):
            for j in range(str_len, len(str_2) + 1):
                diffs_num = mismatches_count[i][j] - mismatches_count[i - str_len][j - str_len]
                if diffs_num <= max_diffs_num:
                    return True
        return False
    
    max_valid_len = 0
    lower, higher = 0, len(str_1)
    while lower < higher:
        mid = (lower + higher + 1) // 2
        if check_substr_exists(mid):
            max_valid_len = max(max_valid_len, mid)
            lower = mid
        else:
            higher = mid - 1
    
    print(max_valid_len)
