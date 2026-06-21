class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        MAX_COST = 100000

        freq = [0] * (MAX_COST + 1)

        for cost in costs:
            freq[cost] += 1

        answer = 0

        for cost in range(1, MAX_COST + 1):

            if freq[cost] == 0:
                continue

            can_buy = min(freq[cost], coins // cost)

            answer += can_buy

            coins -= can_buy * cost

        return answer