class Solution:
	def lastStoneWeight(self, stones):
		while len(stones) > 1:
			stones.sort()
			if stones[-1] - stones[-2] > 0: stones.append(stones.pop() - stones.pop())
			else: stones.pop(); stones.pop()
		return stones[0] if len(stones) > 0 else 0

def main():
	a = [2,7,4,1,8,1]
	a = [1,1,1,1]
	print(Solution().lastStoneWeight(a))

if __name__ == '__main__':
	main()