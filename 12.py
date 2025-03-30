import time

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
cost2 = [
    [0,42,32,54,81,53],
    [42,0,61,73,60,77],
    [32,61,0,69,56,85],
    [54,73,69,0,37,45],
    [81,60,56,37,0,74],
    [53,77,85,45,74,0]
]
cost3 = [
    [0,42,32,54,81,53,53,53],
    [42,0,61,73,60,77,77,77],
    [32,61,0,69,56,85,85,85],
    [54,73,69,0,37,45,45,45],
    [81,60,56,37,0,74,74,74],
    [53,77,85,45,74,0, 0, 0],
    [12,58,55,51,64,48,0,54],
    [84,38,53,85,67,59,54,0]
]

costs = [cost, cost2, cost3]
for cost in costs:
    print()
    start_time = time.time()
    res = tsp_dp(cost)
    print(res)
    print(f"DP for size {len(cost)}: {time.time() - start_time}")

    start_time = time.time()
    res, path = tsp_greedy(cost)
    print(res)
    print(path)
    print(f"Greedy for size {len(cost)}: {time.time() - start_time}")

    start_time = time.time()
    res = GeneticTSP.geneticTSP(cost)
    print(res)
    print(f"Genetic for size {len(cost)}: {time.time() - start_time}")
