import collections

class Solution:
	def countElements(self, arr):
		counter_dict = collections.Counter(arr)
		counter = 0
		for k in counter_dict:
			if counter_dict.get(k + 1):
				counter += counter_dict[k]
		return counter

def main():
	arrays = [[1,2,3], [1,1,3,3,5,5,7,7], [1,3,2,3,5,0], [1,1,2,2]]
	for arr in arrays:
		print(Solution().countElements(arr))

if __name__ == '__main__':
	main()

