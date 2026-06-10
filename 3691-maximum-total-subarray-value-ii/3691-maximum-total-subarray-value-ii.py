from heapq import heappush, heappop


class SparseTable:
    def __init__(self, nums):
        self.n = len(nums)
        self.max_log = self.n.bit_length() + 1

        self.mx = [[0] * self.max_log for _ in range(self.n)]
        self.mn = [[0] * self.max_log for _ in range(self.n)]
        self.lg = [0] * (self.n + 1)

        for i in range(2, self.n + 1):
            self.lg[i] = self.lg[i // 2] + 1

        for i in range(self.n):
            self.mx[i][0] = nums[i]
            self.mn[i][0] = nums[i]

        for j in range(1, self.max_log):
            length = 1 << j

            for i in range(self.n - length + 1):
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + (length >> 1)][j - 1]
                )

                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + (length >> 1)][j - 1]
                )

    def get_max(self, l, r):
        k = self.lg[r - l + 1]

        return max(
            self.mx[l][k],
            self.mx[r - (1 << k) + 1][k]
        )

    def get_min(self, l, r):
        k = self.lg[r - l + 1]

        return min(
            self.mn[l][k],
            self.mn[r - (1 << k) + 1][k]
        )


class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        st = SparseTable(nums)

        pq = []

        for l in range(n):
            val = st.get_max(l, n - 1) - st.get_min(l, n - 1)

            # max heap simulation
            heappush(pq, (-val, l, n - 1))

        ans = 0

        while k:
            neg_val, l, r = heappop(pq)

            val = -neg_val
            ans += val

            if r > l:
                next_val = (
                    st.get_max(l, r - 1)
                    - st.get_min(l, r - 1)
                )

                heappush(pq, (-next_val, l, r - 1))

            k -= 1

        return ans