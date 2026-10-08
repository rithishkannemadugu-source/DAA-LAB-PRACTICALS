n = int(input("Enter number of items: "))

w = list(map(int, input("Enter weights: ").split()))
v = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

dp = [0] * (capacity + 1)

for i in range(n):
    for j in range(capacity, w[i] - 1, -1):
        dp[j] = max(dp[j], v[i] + dp[j - w[i]])

print("Maximum value:", dp[capacity])
