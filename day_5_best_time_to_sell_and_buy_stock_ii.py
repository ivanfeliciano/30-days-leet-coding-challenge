class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) -  1):
            if prices[i + 1] > prices[i]:
                profit += prices[i + 1] - prices[i]
        return profit

def main():
    x = [1,2,3,4,5]
    print(Solution().maxProfit(x))
if __name__ == '__main__':
    main()

        