class Solution:
    MOD = 10**9 + 7

    def power(self, a: int, b: int) -> int:
        ans = 1
        a %= self.MOD

        while b > 0:
            if b & 1:
                ans = (ans * a) % self.MOD
            a = (a * a) % self.MOD
            b >>= 1

        return ans

    def dfs(self, node: int, parent: int, adj: list[list[int]]) -> int:
        ans = 0

        for child in adj[node]:
            if child != parent:
                ans = max(ans, 1 + self.dfs(child, node, adj))

        return ans

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 2
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = self.dfs(1, -1, adj)

        return self.power(2, depth - 1)