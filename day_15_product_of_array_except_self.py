class Solution():
    def productExceptSelf(self, nums):
        prod_prefix = [0 for _ in nums]
        prod_suffix = [0 for _ in nums]
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[- i - 1]
            prod_prefix[i] = prefix
            prod_suffix[-1 -i] = suffix
        ans = []
        for i in range(len(nums)):
            prefix = prod_prefix[i-1] if i > 0 else 1
            suffix = prod_suffix[i + 1]\
                    if i  < len(nums) - 1 else 1
            ans.append(prefix *  suffix)
        return ans
def main():
    x = [1,2,3,4]
    print(Solution().productExceptSelf(x))
if __name__ == '__main__':
    main()