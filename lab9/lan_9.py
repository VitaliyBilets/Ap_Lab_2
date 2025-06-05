import math

def max_wire_length(w, heights):
    n = len(heights)
    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        dp[i][0] = max(
            dp[i - 1][0] + math.hypot(w, 0),
            dp[i - 1][1] + math.hypot(w, abs(1 - heights[i - 1]))
        )
        dp[i][1] = max(
            dp[i - 1][0] + math.hypot(w, abs(heights[i] - 1)),
            dp[i - 1][1] + math.hypot(w, abs(heights[i] - heights[i - 1]))
        )

    return round(max(dp[n - 1][0], dp[n - 1][1]), 2)

w = 4
heights = [100, 2, 100, 2, 100]
print(max_wire_length(w, heights))
