class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer_array = 0
        pointer_zeroes = 0
        while pointer_array < len(nums):
        	if nums[pointer_array] != 0:
        		nums[pointer_zeroes], nums[pointer_array] =\
        			nums[pointer_array], nums[pointer_zeroes]
        		pointer_zeroes += 1
        	pointer_array += 1
def main():
	x = [0, 1, 0, 3, 12]
	# x = [0, 0, 1]
	Solution().moveZeroes(x)
	print(x)

if __name__ == '__main__':
	main()
        