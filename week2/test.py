# Python3 program to find sum of squares
# of Fibonacci numbers in O(Log n) time.
MAX = 1000000000

# Create an array for memoization
f = [0 for i in range(MAX)]


# Returns n'th Fibonacci number using
# table f[]
def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    # If fib(n) is already computed
    if f[n]:
        return f[n]

    if n & 1:
        k = (n + 1) // 2
    else:
        k = n // 2

    # Applying above formula[Note value
    # n & 1 is 1 if n is odd, else 0].
    if n & 1:
        f[n] = (fib(k) * fib(k) +
                fib(k - 1) * fib(k - 1))
    else:
        f[n] = ((2 * fib(k - 1) +
                 fib(k)) * fib(k))
    return f[n]


# Function to calculate sum of
# squares of Fibonacci numbers
def calculateSumOfSquares(n):
    return fib(n) * fib(n + 1)


# Driver Code
n = 1234567890
print("Sum of Squares of "
      "Fibonacci numbers is :",
      calculateSumOfSquares(n))

# This code is contributed by Gaurav Kumar Tailor