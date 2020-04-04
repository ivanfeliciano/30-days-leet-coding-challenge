class Solution:
	def maxSubArray(self, nums):
		current_sum = nums[0]
		max_sum = -1000000000
		i = 1
		while i < len(nums):
			current_sum = max(nums[i], current_sum + nums[i])
			max_sum = max(max_sum, current_sum)
			i += 1
		return max_sum
def main():
	array = [-2,-1,-3,-4,-1,-2,-1,-5,-4]
	print(Solution().maxSubArray(array))
if __name__ == '__main__':
	main()




		