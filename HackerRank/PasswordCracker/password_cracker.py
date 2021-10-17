import sys

sys.setrecursionlimit(4_000)

for _ in range(int(input())):
    input()
    passwords = input().split()
    query = input()
    used_indices = []
    memo = set()

    def is_password_valid(password):
        if len(password) == 0:
            return True
        
        if password in memo:
            return False
        
        for i, curr_password in enumerate(passwords):
            if password.startswith(curr_password):
                used_indices.append(i)
                memo.add(password)
                
                if is_password_valid(password[len(curr_password):]):
                    return True
                used_indices.pop()
        
        return False

    print(' '.join(passwords[i] for i in used_indices) if is_password_valid(query) else 'WRONG PASSWORD')
