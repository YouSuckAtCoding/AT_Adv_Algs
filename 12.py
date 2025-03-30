import GeneticTSP

#https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/
def totalCost(mask, curr, n, cost, memo):

    if mask == (1 << n) - 1:
        return cost[curr][0]

    if memo[curr][mask] != -1:
        return memo[curr][mask]

    ans = float('inf')

    for i in range(n):
        if (mask & (1 << i)) == 0:
            ans = min(ans, cost[curr][i] +
                      totalCost(mask | (1 << i), i, n, cost, memo))

    memo[curr][mask] = ans
    return ans
def tsp_dp(cost):
    n = len(cost)

    memo = [[-1] * (1 << n) for _ in range(n)]

    return totalCost(1, 0, n, cost, memo)

def tsp_greedy(matrix):

    min_dist = 0

    visited = [False] * len(matrix)
    visited[0] = True

    path = [0]

    for i in range(len(matrix)):

        curr_min_idx = (float('inf'), -1)

        for j in range(len(matrix[i])):
            if not visited[j]:
                result = min(curr_min_idx[0], matrix[path[-1]][j])
                if result < curr_min_idx[0]:
                    curr_min_idx = (result, j)

        if not visited[curr_min_idx[1]]:
            path.append(curr_min_idx[1])
            visited[curr_min_idx[1]] = True
            min_dist += curr_min_idx[0]

        if i == len(matrix) - 1:
            min_dist += matrix[path[-1]][0]
            path.append(0)

    return min_dist, path

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
res = tsp_dp(cost)
print(res)

res, path = tsp_greedy(cost)
print(res)
print(path)

res = GeneticTSP.geneticTSP(cost)
print(res)