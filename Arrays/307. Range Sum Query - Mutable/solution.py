class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum_var = [0] * len(nums)
        self.sum_var[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            self.sum_var[i] = self.nums[i] + self.sum_var[i-1]
        print(self.sum_var)

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        if index == 0:
            self.sum_var[0] = self.nums[0]
            for i in range(1, len(self.nums)):
                self.sum_var[i] = self.nums[i] + self.sum_var[i-1]
        else: 
            for i in range(index, len(self.nums)):
                self.sum_var[i] = self.nums[i] + self.sum_var[i-1]
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return (self.sum_var[right])
        else:
            return (self.sum_var[right] - self.sum_var[left-1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
