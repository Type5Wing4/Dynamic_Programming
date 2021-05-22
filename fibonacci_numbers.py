# Compare the three following methods for calculating Fibonacci numbers.
# 1. recursive
# 2. memoization and recursive (a kind of dynnamic programming)
# 3. Dynamic Programming which uses memization (calculation from smaller numbers)


def fibo_r(n):

    # Calculate fibonacci number recursively.
    # This is not efficient compared with the following methods.

    if n == 0:
        val = 0
    elif n == 1:
        val = 1
    else:
        val = fibo_r(n-1) + fibo_r(n-2)

    return val


memo={0:1, 1:1}
def fibo_r_and_m(n):

    # Calculate fibonacci number recursively with memorandum.
    # This is much faster than the previous one.

    if n in memo.keys():
        return memo[n]
    else:
        val = fibo_r_and_m(n-2) + fibo_r_and_m(n-1)
        memo[n] = val

    return val

def fibo_dynamic_programming(n):

    # Calculate fibonacci number by dynamic programming.
    # This is the most efficient in the three method.

    memo = {0:1, 1:1}
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]

if __name__ == '__main__':

    print('Recursive algorithm')
    for n in range(0, 10):
        print(fibo_r(n))

    print()
    print('Memoization and Recursive algorithm')
    for n in range(0, 100):
        print(fibo_r_and_m(n))

    print()
    print('Dynamic Programming algorithm')
    for n in range(0, 100):
        print(fibo_dynamic_programming(n))
