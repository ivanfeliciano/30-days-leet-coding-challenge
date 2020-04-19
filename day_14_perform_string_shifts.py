class Solution:
    def stringShift(self, s, shift):
        n = 0
        for pair in shift:
            n += pair[1] if pair[0] == 0 else - pair[1] 
        for i in range(abs(n)):
            s = s[-1] + s[:-1] if n < 0 else s[1:] + s[0]
        return s
