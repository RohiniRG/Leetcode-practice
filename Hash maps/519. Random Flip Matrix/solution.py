import random

class Solution:
    def __init__(self, m: int, n: int):
        self.select = list()
        self.m = m
        self.n = n
        
    def flip(self) -> List[int]:
        while True:
            i = random.randint(0, self.m-1)
            j = random.randint(0, self.n-1)
            if [i, j] not in self.select:
                break
        self.select.append([i, j])
        return [i, j]
        
    def reset(self) -> None:
        self.select = list()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()

