class Solution:
    def singleNumber(self, nums):
    	return 2 * sum(set(nums)) - sum(nums)
    def best_solution(self, nums):
    	"""
    	Como XOR es conmutativo.
    	"""
    	ans = 0
    	for i in nums: ans ^= i
    	return ans
def main():
	nums = [1,2,2,3,3, 4, 1]
	print(Solution().best_solution(nums))
if __name__ == '__main__':
	main()