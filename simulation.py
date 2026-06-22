

def dp(n):
    if n == 1:
        return 3/8
    return (3/8) + (1/4) * dp(n - 1)

res = dp(10)
print(res)