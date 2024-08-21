def natural_sum(n):
    if n <= 1:
        return 1
    return n + natural_sum(n-1)

def eulers_formula(n):
    return int((n * (n + 1))/2)

print(eulers_formula(100))