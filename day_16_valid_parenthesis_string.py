class Solution:
	def checkValidString(self, s):
		counter_max = 0
		counter_min = 0
		for i in range(len(s)):
			if s[i] == "(": counter_min += 1; counter_max += 1;
			if s[i] == ")": counter_min -= 1; counter_max -= 1;
			if s[i] == "*": counter_min -= 1; counter_max += 1
			if counter_max < 0: return False
			counter_min = max(0, counter_min)
		return counter_max == 0
def main():
	s = "(())"
	# s = "()(*)"
	# s = "(*(()))((())())*(**(()))((*)()(()))*(())()(())(()"
	s = "()*((()(((((*))))((*()((*(())()(**)()()*))((((()**((())((()()(()(()()*)()))(()))))))*(((()()()())()"
	print(Solution().checkValidString(s))
if __name__ == '__main__':
	main()
