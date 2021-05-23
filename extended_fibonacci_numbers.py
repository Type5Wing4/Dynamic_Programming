def fibonacci_numbers_o(n):

    memo = {0:1, 1:1}
    for i in range(2,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo

def fibonacci_numbers_001(n):

    memo = {0:1, 1:1}
    for i in range(2,n+1):
        memo[i] = memo[i-1] - 2 * memo[i-2]

    return memo

def fibonacci_numbers_002(n):

    memo = {0:1, 1:1, 2:2}
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo

if __name__ == '__main__':

    print(fibonacci_numbers_o(100))
    print(fibonacci_numbers_001(100))
    print(fibonacci_numbers_002(100))
