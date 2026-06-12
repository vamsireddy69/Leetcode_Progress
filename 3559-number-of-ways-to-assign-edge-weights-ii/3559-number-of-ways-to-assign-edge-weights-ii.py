class Solution:
    MOD = 1_000_000_007

    def assignEdgeWeights(self, edges, queries):
        n = len(edges) + 1

        self.graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.LOG = 1
        while (1 << self.LOG) <= n:
            self.LOG += 1

        self.up = [[0] * self.LOG for _ in range(n + 1)]
        self.depth = [0] * (n + 1)

        self.dfs(1, 0)

        for j in range(1, self.LOG):
            for node in range(1, n + 1):
                parent = self.up[node][j - 1]
                self.up[node][j] = 0 if parent == 0 else self.up[parent][j - 1]

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % self.MOD

        ans = []

        for u, v in queries:
            p = self.lca(u, v)

            length = self.depth[u] + self.depth[v] - 2 * self.depth[p]

            if length == 0:
                ans.append(0)
            else:
                ans.append(pow2[length - 1])

        return ans

    def dfs(self, node, parent):
        self.up[node][0] = parent

        for nxt in self.graph[node]:
            if nxt == parent:
                continue

            self.depth[nxt] = self.depth[node] + 1
            self.dfs(nxt, node)

    def lca(self, a, b):
        if self.depth[a] < self.depth[b]:
            a, b = b, a

        diff = self.depth[a] - self.depth[b]

        for j in range(self.LOG - 1, -1, -1):
            if (diff >> j) & 1:
                a = self.up[a][j]

        if a == b:
            return a

        for j in range(self.LOG - 1, -1, -1):
            if self.up[a][j] != self.up[b][j]:
                a = self.up[a][j]
                b = self.up[b][j]

        return self.up[a][0]