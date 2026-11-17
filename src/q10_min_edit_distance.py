# 10: Write a program to implement the minimum edit distance for converting
# source string to the target string following the dynamic programming approach
# given the cost of insertion as 1, cost of deletion as 1 and cost of substation
# as 1.
# Input: i) A source string ii) A target string

def min_edit_distance(source, target, ins_cost=1, del_cost=1, sub_cost=1):
    m = len(source)
    n = len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + del_cost

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ins_cost

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + del_cost,
                    dp[i][j - 1] + ins_cost,
                    dp[i - 1][j - 1] + sub_cost,
                )

    return dp[m][n]

src = input("Enter source string (default 'intention'): ").strip() or "intention"
tgt = input("Enter target string (default 'execution'): ").strip() or "execution"
dist = min_edit_distance(src, tgt, ins_cost=1, del_cost=1, sub_cost=1)
print(f"Minimum edit distance between '{src}' and '{tgt}': {dist}")
