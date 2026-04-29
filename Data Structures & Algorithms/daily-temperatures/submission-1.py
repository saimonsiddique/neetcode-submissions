class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop_idx = stack.pop()
                answer[pop_idx] = i - pop_idx
            stack.append(i)
        return answer 