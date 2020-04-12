class Solution:
	def groupAnagrams(self, strs):
		ana_dict = dict()
		for string in strs:
			str_pointer = "".join(sorted(string))
			if not ana_dict.get(str_pointer):
				ana_dict[str_pointer] = []
			ana_dict[str_pointer].append(string)
		return [ana_dict[key] for key in ana_dict]

def main():
	ana = ["eat", "tea", "tan", "ate", "nat", "bat"]
	print(Solution().groupAnagrams(ana))
if __name__ == '__main__':
	main()