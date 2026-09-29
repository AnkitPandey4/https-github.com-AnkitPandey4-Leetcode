class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        n = len(vals)
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(vals[v])
            adj[v].append(vals[u])

        maxE = float('-inf')

        for i in range(len(adj)):
            temp = vals[i]
            adj[i].sort(reverse=True)

            for j in range(min(k, len(adj[i]))):
                if adj[i][j] > 0:
                    temp += adj[i][j]
                else:
                    break

            maxE = max(maxE, temp)

        return maxE