from random import randint

n_cases = 4

def gen_test_case(n_vals):
    vals = " ".join(str(randint(1, 10_000_000)) for _ in range(n_vals))
    return f"{n_vals}\n{vals}"

test_cases = "\n".join(gen_test_case(100_000) for _ in range(n_cases))
print(f"{n_cases}\n{test_cases}")